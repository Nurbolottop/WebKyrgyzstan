"""
Абстрактные модели, на которых строится весь контент сайта.

Подписи полей — на русском без gettext: они видны только в админке.
Тексты, которые попадают на сайт (варианты choices), переводятся через gettext.
"""
import uuid
from pathlib import Path

from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

from apps.base.validators import IMAGE_VALIDATORS


def upload_to(instance, filename):
    """articles/article/2026/10/<uuid>.jpg — без кириллицы и коллизий в именах."""
    meta = instance._meta
    ext = Path(filename).suffix.lower()
    return f'{meta.app_label}/{meta.model_name}/{timezone.now():%Y/%m}/{uuid.uuid4().hex}{ext}'


class PublishedQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('создано', auto_now_add=True)
    updated_at = models.DateTimeField('изменено', auto_now=True)

    class Meta:
        abstract = True


class PublishableModel(models.Model):
    is_published = models.BooleanField('опубликовано', default=True, db_index=True)
    order = models.PositiveIntegerField(
        'порядок', default=0, db_index=True, help_text='Меньше — выше в списке.'
    )

    objects = PublishedQuerySet.as_manager()

    class Meta:
        abstract = True
        ordering = ['order', 'pk']


class SeoModel(models.Model):
    meta_title = models.CharField(
        'SEO-заголовок', max_length=70, blank=True,
        help_text='Если пусто, используется название.',
    )
    meta_description = models.CharField(
        'SEO-описание', max_length=160, blank=True,
        help_text='Если пусто, используется краткое описание.',
    )
    og_image = models.ImageField(
        'картинка для соцсетей', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS,
        help_text='1200×630. Если пусто, используется обложка.',
    )

    class Meta:
        abstract = True


class CoverMixin(models.Model):
    cover = models.ImageField(
        'обложка', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS,
        help_text='Горизонтальное фото не меньше 1600 px по ширине.',
    )
    cover_alt = models.CharField(
        'описание обложки', max_length=200, blank=True,
        help_text='Что изображено — для незрячих пользователей и поисковиков.',
    )
    cover_credit = models.CharField(
        'автор и лицензия обложки', max_length=255, blank=True,
        help_text='Например: «Фото: Иван Иванов, CC BY-SA 4.0, Wikimedia Commons».',
    )

    class Meta:
        abstract = True


class ContentModel(TimeStampedModel, PublishableModel, SeoModel, CoverMixin):
    """Любой самостоятельный материал с собственной страницей."""

    title = models.CharField('название', max_length=200)
    slug = models.SlugField(
        'адрес (slug)', max_length=200, unique=True,
        help_text='Латиницей, используется в URL. Заполняется автоматически из названия.',
    )
    summary = models.TextField(
        'краткое описание', blank=True, help_text='1–2 предложения для карточек и поисковиков.'
    )
    body = CKEditor5Field('текст', blank=True)
    published_at = models.DateTimeField('дата публикации', default=timezone.now)

    class Meta(PublishableModel.Meta):
        abstract = True

    def __str__(self):
        return self.title


class BaseStep(models.Model):
    """Шаг пошаговой инструкции (рецепт, мастер-класс, задание)."""

    order = models.PositiveIntegerField('порядок', default=0)
    title = models.CharField('заголовок шага', max_length=200, blank=True)
    text = models.TextField('что делать')
    image = models.ImageField(
        'иллюстрация', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS
    )
    image_alt = models.CharField('описание иллюстрации', max_length=200, blank=True)
    video_url = models.URLField('видео (YouTube)', blank=True)

    class Meta:
        abstract = True
        ordering = ['order', 'pk']

    def __str__(self):
        return self.title or f'Шаг {self.order}'
