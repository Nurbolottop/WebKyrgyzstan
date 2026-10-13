from django import template
from django.utils.html import strip_tags
from django.utils.text import Truncator

from apps.base.images import renditions

register = template.Library()


@register.inclusion_tag('partials/seo_meta.html', takes_context=True)
def seo_meta(context, obj=None, title='', description=''):
    """Title, description, Open Graph, canonical и hreflang для страницы."""
    request = context['request']
    site = context.get('site')
    site_name = site.site_name if site else 'Web Kyrgyzstan'

    if obj is not None:
        title = title or getattr(obj, 'meta_title', '') or str(obj)
        description = (
            description
            or getattr(obj, 'meta_description', '')
            or getattr(obj, 'summary', '')
            or strip_tags(getattr(obj, 'body', '') or '')
        )
    description = Truncator(description or (site.tagline if site else '')).chars(160)

    image = None
    for candidate in (getattr(obj, 'og_image', None), getattr(obj, 'cover', None), getattr(site, 'default_og_image', None)):
        if candidate:
            image = candidate
            break
    image_url = ''
    if image:
        variants = renditions(image)
        if variants:
            image_url = request.build_absolute_uri(variants[-1][0])

    full_title = f'{title} — {site_name}' if title and title != site_name else site_name
    return {
        'title': full_title,
        'description': description,
        'image_url': image_url,
        'canonical': request.build_absolute_uri(request.path),
        'language_links': [
            {**link, 'absolute': request.build_absolute_uri(link['url'])}
            for link in context.get('language_links', [])
        ],
        'site_name': site_name,
    }


@register.simple_tag(takes_context=True)
def jsonld(context, obj, kind='Article'):
    """Структурированные данные schema.org + хлебные крошки."""
    import json

    from django.utils.html import format_html
    from django.utils.safestring import mark_safe

    request = context['request']
    url = request.build_absolute_uri(obj.get_absolute_url())
    image = ''
    if getattr(obj, 'cover', None):
        variants = renditions(obj.cover)
        image = request.build_absolute_uri(variants[-1][0]) if variants else ''

    data = {
        '@context': 'https://schema.org',
        '@type': kind,
        'name': obj.title,
        'url': url,
        'inLanguage': context.get('LANGUAGE_CODE', ''),
    }
    summary = getattr(obj, 'summary', '')
    if summary:
        data['description'] = summary
    if image:
        data['image'] = image
    if kind == 'Article':
        data['headline'] = obj.title
        data['datePublished'] = obj.published_at.date().isoformat()
        data['dateModified'] = obj.updated_at.date().isoformat()
        data['publisher'] = {'@type': 'Organization', 'name': 'Web Kyrgyzstan'}
        data['audience'] = {'@type': 'EducationalAudience', 'educationalRole': 'student'}
    elif kind == 'Recipe':
        data['recipeIngredient'] = [f'{s.amount} {s.name}'.strip() for s in obj.supplies.all()]
        data['recipeInstructions'] = [{'@type': 'HowToStep', 'text': s.text} for s in obj.steps.all()]
        if obj.servings:
            data['recipeYield'] = str(obj.servings)
        if obj.duration_min:
            data['totalTime'] = f'PT{obj.duration_min}M'
    elif kind == 'TouristAttraction' and getattr(obj, 'latitude', None):
        data['geo'] = {'@type': 'GeoCoordinates', 'latitude': float(obj.latitude), 'longitude': float(obj.longitude)}

    crumbs = [('Web Kyrgyzstan', request.build_absolute_uri('/'))]
    parents = _parents(obj)
    crumbs += [(str(p), request.build_absolute_uri(p.get_absolute_url())) for p in parents]
    crumbs.append((obj.title, url))
    breadcrumbs = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'name': name, 'item': item}
            for i, (name, item) in enumerate(crumbs, start=1)
        ],
    }
    payload = json.dumps([data, breadcrumbs], ensure_ascii=False).replace('<', '\\u003c')
    return format_html('<script type="application/ld+json">{}</script>', mark_safe(payload))


def _parents(obj):
    """Родительские страницы материала для хлебных крошек."""
    from apps.base.models import Section

    if hasattr(obj, 'category'):
        return [obj.category.section, obj.category]
    if hasattr(obj, 'region'):
        return [Section.objects.get(key='discover'), obj.region]
    if obj._meta.model_name == 'region':
        return [Section.objects.get(key='discover')]
    if obj._meta.app_label == 'practice':
        return [Section.objects.get(key='practice')]
    return []
