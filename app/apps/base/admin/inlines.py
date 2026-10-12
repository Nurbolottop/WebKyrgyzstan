from modeltranslation.admin import TranslationGenericStackedInline, TranslationGenericTabularInline

from apps.base.models import Fact, GalleryImage


class GalleryImageInline(TranslationGenericStackedInline):
    model = GalleryImage
    extra = 0
    fields = ('image', 'alt', 'caption', 'credit', 'order')


class FactInline(TranslationGenericTabularInline):
    model = Fact
    extra = 0
    fields = ('text', 'order')
