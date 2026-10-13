from django.shortcuts import get_object_or_404, render

from apps.articles.models import Article
from apps.base.models import Section

from .models import Place, Region
from .services import map_context


def index(request):
    section = Section.objects.get(key='discover')
    return render(request, 'discover/index.html', {
        'section': section,
        'map': map_context(),
        'places': Place.objects.published().select_related('region')[:8],
        'articles': Article.objects.published()
            .filter(category__section=section).select_related('category__section')[:6],
    })


def region_detail(request, slug):
    region = get_object_or_404(Region.objects.published(), slug=slug)
    return render(request, 'discover/region_detail.html', {
        'section': Section.objects.get(key='discover'),
        'region': region,
        'map': map_context(pins=False),
        'places': region.places.published(),
        'articles': region.articles.published().select_related('category__section'),
        'gallery': region.gallery.all(),
        'facts': region.facts.all(),
    })


def place_list(request):
    places = Place.objects.published().select_related('region')
    kind = request.GET.get('kind', '')
    if kind not in Place.Kind.values:
        kind = ''
    if kind:
        places = places.filter(kind=kind)
    return render(request, 'discover/place_list.html', {
        'section': Section.objects.get(key='discover'),
        'places': places,
        'kinds': Place.Kind.choices,
        'current_kind': kind,
    })


def place_detail(request, slug):
    place = get_object_or_404(Place.objects.published().select_related('region'), slug=slug)
    return render(request, 'discover/place_detail.html', {
        'section': Section.objects.get(key='discover'),
        'place': place,
        'gallery': place.gallery.all(),
        'facts': place.facts.all(),
        'nearby': place.region.places.published().exclude(pk=place.pk)[:3],
    })
