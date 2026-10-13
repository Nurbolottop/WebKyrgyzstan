from .map_projection import project
from .models import Place, Region


def _key(slug):
    # В шаблоне ключи словаря с дефисом недоступны: chuy, issyk_kul, osh_city…
    return slug.replace('-', '_')


def map_context(pins=True):
    """Данные для templates/svg/map_kyrgyzstan.html и всплывающих подсказок карты."""
    regions = list(Region.objects.published().prefetch_related('places'))
    links, names, tips = {}, {}, {}
    for region in regions:
        links[_key(region.map_id)] = region.get_absolute_url()
        names[_key(region.map_id)] = region.title
        tips[region.map_id] = {
            'title': region.title,
            'capital': region.capital,
            'places': sum(1 for p in region.places.all() if p.is_published),
            'url': region.get_absolute_url(),
        }
    pin_list = []
    if pins:
        for place in Place.objects.published().exclude(latitude=None).exclude(longitude=None):
            x, y = project(place.latitude, place.longitude)
            # Строки, а не float: иначе локализация выведет «720,1», и SVG не поймёт координату
            pin_list.append({'x': f'{x:.1f}', 'y': f'{y:.1f}', 'title': place.title})
    return {'links': links, 'names': names, 'tips': tips, 'pins': pin_list, 'regions': regions}
