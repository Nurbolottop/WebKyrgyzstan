from django.db import models

from apps.base.choices import SectionKey
from apps.base.validators import IMAGE_VALIDATORS

from .abstract import CoverMixin, upload_to


class SiteSettings(models.Model):
    """Единственная запись с общими текстами сайта и главной страницы."""

    site_name = models.CharField('название сайта', max_length=100, default='Web Kyrgyzstan')
    tagline = models.CharField('слоган', max_length=200, blank=True)
    about = models.TextField('о проекте (подвал)', blank=True)
    copyright = models.CharField('копирайт', max_length=200, blank=True)

    hero_title = models.CharField('заголовок главной', max_length=200, blank=True)
    hero_subtitle = models.TextField('подзаголовок главной', blank=True)
    hero_cta_label = models.CharField('текст кнопки главной', max_length=60, blank=True)
    hero_image = models.ImageField(
        'изображение главной', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS
    )
    hero_image_alt = models.CharField('описание изображения главной', max_length=200, blank=True)
    hero_image_credit = models.CharField('автор и лицензия', max_length=255, blank=True)

    default_og_image = models.ImageField(
        'картинка для соцсетей по умолчанию', upload_to=upload_to, blank=True,
        validators=IMAGE_VALIDATORS, help_text='1200×630.',
    )

    class Meta:
        verbose_name = 'настройки сайта'
        verbose_name_plural = 'настройки сайта'

    def __str__(self):
        return 'Настройки сайта'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj


class Section(CoverMixin, models.Model):
    """Один из пяти основных разделов. Набор фиксирован, редактируются только тексты и обложки."""

    key = models.CharField('ключ', max_length=20, choices=SectionKey.choices, unique=True, editable=False)
    title = models.CharField('название', max_length=100)
    short_title = models.CharField(
        'короткое название', max_length=40, blank=True, help_text='Для меню, если полное не помещается.'
    )
    description = models.TextField('описание', blank=True, help_text='Для карточки на главной и шапки раздела.')
    order = models.PositiveSmallIntegerField('порядок', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return self.title
