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
