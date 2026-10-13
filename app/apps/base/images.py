"""
WebP-варианты загруженных изображений нужной ширины.

Генерируются при первом обращении и складываются рядом с медиа в renditions/;
повторно не пересчитываются, пока не изменится исходный файл.
"""
import hashlib
import logging
from pathlib import Path

from django.conf import settings
from django.core.files.storage import default_storage
from PIL import Image, ImageOps

logger = logging.getLogger(__name__)

WIDTHS = (480, 960, 1600)
QUALITY = 80


def _rendition_name(name, width):
    stem = Path(name).stem
    digest = hashlib.md5(name.encode()).hexdigest()[:10]
    return f'renditions/{digest}/{stem}-{width}.webp'


def renditions(image_field):
    """[(url, width)] для srcset; пустой список, если файла нет или он не читается."""
    if not image_field:
        return []
    try:
        original_width = image_field.width
    except (FileNotFoundError, OSError, ValueError):
        logger.warning('Не удалось прочитать изображение %s', image_field.name)
        return []

    widths = [w for w in WIDTHS if w < original_width] + [min(original_width, WIDTHS[-1])]
    result = []
    for width in sorted(set(widths)):
        name = _rendition_name(image_field.name, width)
        path = Path(settings.MEDIA_ROOT) / name
        if not path.exists() or path.stat().st_mtime < Path(image_field.path).stat().st_mtime:
            try:
                _build(image_field.path, path, width)
            except OSError:
                logger.exception('Не удалось создать вариант %s', name)
                continue
        result.append((default_storage.url(name), width))
    return result


def _build(source, target, width):
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as img:
        img = ImageOps.exif_transpose(img)
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGBA' if 'transparency' in img.info else 'RGB')
        if img.width > width:
            height = round(img.height * width / img.width)
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        img.save(target, 'WEBP', quality=QUALITY, method=5)
