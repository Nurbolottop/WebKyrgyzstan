import re

from django.utils.text import Truncator

from apps.base.images import renditions

from .map_projection import project
from .models import Place, Region


def _key(slug):
    # В шаблоне ключи словаря с дефисом недоступны: chuy, issyk_kul, osh_city…
    return slug.replace('-', '_')


def _thumb(image):
    variants = renditions(image)
    for url, width in variants:
        if width >= 480:
            return url
    return variants[-1][0] if variants else ''


# Короткая подпись на карте: «Чуйская область» → «Чуйская», «Бишкек шаары» → «Бишкек»
_LABEL_WORDS = re.compile(r'\s*(область|облусу|region|город|шаары|city)\s*', re.IGNORECASE)


def _label(title):
    return _LABEL_WORDS.sub(' ', title).strip()


def _short(text):
    return Truncator(text or '').chars(150)


def map_context(pins=True):
    """Данные для templates/svg/map_kyrgyzstan.html и карточки рядом с картой."""
    regions = list(Region.objects.published().prefetch_related('places'))
    links, names, labels, tips = {}, {}, {}, {}
    for region in regions:
        links[_key(region.map_id)] = region.get_absolute_url()
        names[_key(region.map_id)] = region.title
        labels[_key(region.map_id)] = _label(region.title)
        tips[region.map_id] = {
            'type': 'region',
            'title': region.title,
            'kind': region.get_kind_display(),
            'summary': _short(region.summary),
            'capital': region.capital,
            'area': f'{region.area_km2:,}'.replace(',', ' ') if region.area_km2 else '',
            'places': sum(1 for p in region.places.all() if p.is_published),
            'image': _thumb(region.cover),
            'url': region.get_absolute_url(),
        }

    pin_list, pin_tips = [], {}
    if pins:
        places = Place.objects.published().select_related('region').exclude(latitude=None).exclude(longitude=None)
        for place in places:
            x, y = project(place.latitude, place.longitude)
            # Строки, а не float: иначе локализация выведет «720,1», и SVG не поймёт координату
            pin_list.append({'x': f'{x:.1f}', 'y': f'{y:.1f}', 'title': place.title,
                             'slug': place.slug, 'url': place.get_absolute_url(), 'kind': place.kind})
            pin_tips[place.slug] = {
                'type': 'place',
                'title': place.title,
                'kind': place.get_kind_display(),
                'summary': _short(place.summary),
                'region': place.region.title,
                'value': place.key_value,
                'valueLabel': place.key_label,
                'image': _thumb(place.cover),
                'url': place.get_absolute_url(),
            }
    kinds = [(value, label) for value, label in Place.Kind.choices if any(p['kind'] == value for p in pin_list)]
    return {'links': links, 'names': names, 'labels': labels, 'tips': tips, 'pins': pin_list,
            'pin_tips': pin_tips, 'pin_kinds': kinds, 'regions': regions}
