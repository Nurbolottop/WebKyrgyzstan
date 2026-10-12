from modeltranslation.translator import TranslationOptions, register

from apps.base.translation import CONTENT_FIELDS

from .models import Place, Region


@register(Region)
class RegionTranslation(TranslationOptions):
    fields = CONTENT_FIELDS + ('capital', 'geography', 'nature', 'culture')


@register(Place)
class PlaceTranslation(TranslationOptions):
    fields = CONTENT_FIELDS + ('key_value', 'key_label')
