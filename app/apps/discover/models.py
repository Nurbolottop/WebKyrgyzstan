from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field

from apps.base.models import ContentModel, Fact, GalleryImage


class Region(ContentModel):
    class Kind(models.TextChoices):
        OBLAST = 'oblast', _('Region')
        CITY = 'city', _('City of republican significance')

    kind = models.CharField('тип', max_length=10, choices=Kind.choices, default=Kind.OBLAST)
    map_id = models.SlugField(
        'id на карте', max_length=50, unique=True,
        help_text='Совпадает с id контура в SVG-карте. Меняет только разработчик.',
    )
    capital = models.CharField('административный центр', max_length=100, blank=True)
    area_km2 = models.PositiveIntegerField('площадь, км²', null=True, blank=True)
    population = models.PositiveIntegerField('население', null=True, blank=True)
    population_year = models.PositiveSmallIntegerField('год данных о населении', null=True, blank=True)

    geography = CKEditor5Field('географические особенности', blank=True)
    nature = CKEditor5Field('горы, озёра и природа', blank=True)
    culture = CKEditor5Field('культура и местные особенности', blank=True)

    gallery = GenericRelation(GalleryImage)
    facts = GenericRelation(Fact)

    class Meta(ContentModel.Meta):
        verbose_name = 'область / город'
        verbose_name_plural = 'области и города'


class Place(ContentModel):
    class Kind(models.TextChoices):
        LAKE = 'lake', _('Lake')
        MOUNTAIN = 'mountain', _('Mountain')
        NATURE = 'nature', _('Nature')
        HISTORIC = 'historic', _('Historic site')
        CITY = 'city', _('City')

    region = models.ForeignKey(
        Region, verbose_name='область / город', on_delete=models.PROTECT, related_name='places'
    )
    kind = models.CharField('тип', max_length=10, choices=Kind.choices)
    latitude = models.DecimalField(
        'широта', max_digits=8, decimal_places=5, null=True, blank=True,
        validators=[MinValueValidator(39), MaxValueValidator(44)],
        help_text='Для точки на карте, например 42.45000.',
    )
    longitude = models.DecimalField(
        'долгота', max_digits=8, decimal_places=5, null=True, blank=True,
        validators=[MinValueValidator(69), MaxValueValidator(81)],
        help_text='Например 77.25000.',
    )
    key_value = models.CharField(
        'главная цифра', max_length=40, blank=True, help_text='Например «1 607 м».'
    )
    key_label = models.CharField(
        'подпись к цифре', max_length=100, blank=True, help_text='Например «высота над уровнем моря».'
    )

    gallery = GenericRelation(GalleryImage)
    facts = GenericRelation(Fact)

    class Meta(ContentModel.Meta):
        verbose_name = 'достопримечательность'
        verbose_name_plural = 'достопримечательности'
