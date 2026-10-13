"""Строит SVG-карту Кыргызстана из geoBoundaries ADM1 (OSM, ODbL) + контуров Бишкека и Оша (OSM)."""
import json, math, sys
# python3 tools/build_map.py tools/geo app/templates/svg/map_kyrgyzstan.html app/apps/discover/map_projection.py app/static/img/sections/discover.svg
geo, out_tpl, out_py = sys.argv[1], sys.argv[2], sys.argv[3]

ADM1 = {
    'Chuy Region': 'chuy', 'Talas Region': 'talas', 'Issyk-Kul Region': 'issyk-kul',
    'Naryn Region': 'naryn', 'Jalal-Abad Region': 'jalal-abad', 'Osh Region': 'osh-region',
    'Batken Region': 'batken',
}
shapes = {}
for f in json.load(open(f'{geo}/adm1.geojson'))['features']:
    shapes[ADM1[f['properties']['shapeName']]] = f['geometry']
shapes['bishkek'] = json.load(open(f'{geo}/bishkek.geojson'))['features'][0]['geometry']
for f in json.load(open(f'{geo}/osh.geojson'))['features']:
    p = f['properties']
    if p['type'] == 'administrative' and 'шаары' in p['display_name']:
        shapes['osh-city'] = f['geometry']

def rings(g):
    polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
    for poly in polys:
        for ring in poly:
            yield ring

pts = [pt for slug in ADM1.values() for r in rings(shapes[slug]) for pt in r]
min_lon = min(p[0] for p in pts); max_lon = max(p[0] for p in pts)
min_lat = min(p[1] for p in pts); max_lat = max(p[1] for p in pts)
k = math.cos(math.radians((min_lat + max_lat) / 2))
W = 1000.0
PAD = 8
scale = (W - 2 * PAD) / ((max_lon - min_lon) * k)
H = round((max_lat - min_lat) * scale + 2 * PAD)

def project(lon, lat):
    return (PAD + (lon - min_lon) * k * scale, PAD + (max_lat - lat) * scale)

def path(g, min_step):
    parts = []
    for r in rings(g):
        out, last = [], None
        for lon, lat in r:
            x, y = project(lon, lat)
            if last and math.hypot(x - last[0], y - last[1]) < min_step:
                continue
            out.append((x, y)); last = (x, y)
        if len(out) < 3:
            continue
        parts.append('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in out) + 'Z')
    return ''.join(parts)

def centroid(g):
    best = max(rings(g), key=len)
    xs, ys = zip(*(project(*p) for p in best))
    return sum(xs) / len(xs), sum(ys) / len(ys)

order = list(ADM1.values()) + ['bishkek', 'osh-city']
lines = [
    '{# Сгенерировано: geoBoundaries KGZ ADM1 и OpenStreetMap (© участники OpenStreetMap, ODbL). Не редактировать вручную. #}',
    '{% load i18n %}',
    f'<svg class="kg-map__svg" viewBox="0 0 {int(W)} {H}" role="group" aria-label="{{% translate \'Map of Kyrgyzstan\' %}}" xmlns="http://www.w3.org/2000/svg">',
]
for slug in order:
    kind = 'city' if slug in ('bishkek', 'osh-city') else 'oblast'
    d = path(shapes[slug], 1.4 if kind == 'oblast' else 0.3)
    cx, cy = centroid(shapes[slug])
    lines.append(
        f'  <a class="kg-map__region kg-map__region--{kind}" href="{{{{ map.links.{slug.replace("-", "_")}|default:\'#\' }}}}" '
        f'data-region="{slug}" aria-label="{{{{ map.names.{slug.replace("-", "_")} }}}}">'
        f'<path d="{d}"/>'
        + (f'<circle class="kg-map__city-dot" cx="{cx:.1f}" cy="{cy:.1f}" r="9"/>' if kind == 'city' else '')
        + '</a>'
    )
lines.append('  {% if map.pins %}<g class="kg-map__pins" aria-hidden="true">{% for pin in map.pins %}<circle class="kg-map__pin" cx="{{ pin.x }}" cy="{{ pin.y }}" r="6"><title>{{ pin.title }}</title></circle>{% endfor %}</g>{% endif %}')
lines.append('</svg>')
open(out_tpl, 'w').write('\n'.join(lines) + '\n')

open(out_py, 'w').write(f'''"""Параметры проекции SVG-карты (генерируются вместе с templates/svg/map_kyrgyzstan.html)."""
import math

WIDTH = {int(W)}
HEIGHT = {H}
_PAD = {PAD}
_MIN_LON = {min_lon!r}
_MAX_LAT = {max_lat!r}
_K = {k!r}
_SCALE = {scale!r}


def project(lat, lon):
    """Широта/долгота → координаты x, y во viewBox карты."""
    x = _PAD + (float(lon) - _MIN_LON) * _K * _SCALE
    y = _PAD + (_MAX_LAT - float(lat)) * _SCALE
    return round(x, 1), round(y, 1)
''')
print('viewBox', int(W), H, 'bytes', len('\n'.join(lines)))

# Статичная иллюстрация карты (без ссылок) — для карточки раздела на главной
if len(sys.argv) > 4:
    fills = ['#b9e1dc', '#cde9c9', '#a9d6e5', '#d6e6c3', '#f3dcb3', '#f0cfb8', '#e9c7c2']
    art = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {int(W)} {H}">']
    for fill, slug in zip(fills, ADM1.values()):
        art.append(f'<path d="{path(shapes[slug], 2.5)}" fill="{fill}" stroke="#fff" stroke-width="3" stroke-linejoin="round"/>')
    for slug in ('bishkek', 'osh-city'):
        cx, cy = centroid(shapes[slug])
        art.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="12" fill="#d6282b" stroke="#fff" stroke-width="4"/>')
    art.append('</svg>')
    open(sys.argv[4], 'w').write(''.join(art))
