from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from apps.base.images import renditions

register = template.Library()


@register.simple_tag
def picture(image, alt='', sizes='100vw', css_class='', eager=False):
    """Адаптивное изображение: WebP нужной ширины + srcset."""
    variants = renditions(image)
    if not variants:
        return ''
    src, width = variants[-1]
    height = round(image.height * width / image.width)
    srcset = ', '.join(f'{url} {w}w' for url, w in variants)
    loading = 'eager' if eager else 'lazy'
    priority = mark_safe(' fetchpriority="high"') if eager else ''
    return format_html(
        '<img src="{}" srcset="{}" sizes="{}" width="{}" height="{}" alt="{}" class="{}" loading="{}" decoding="async"{}>',
        src, srcset, sizes, width, height, alt, css_class, loading, priority,
    )


@register.simple_tag
def image_url(image, width=1600):
    """URL одного варианта изображения (для og:image, фона и т. п.)."""
    variants = renditions(image)
    if not variants:
        return ''
    suitable = [url for url, w in variants if w >= width]
    return suitable[0] if suitable else variants[-1][0]


@register.filter
def lines(value):
    """Текст «по строке на вариант» → список непустых строк."""
    return [line.strip() for line in (value or '').splitlines() if line.strip()]
