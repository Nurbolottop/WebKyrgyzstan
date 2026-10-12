from modeltranslation.translator import TranslationOptions, register

from .models import Fact, GalleryImage, HomeFeatured, Section, SiteSettings

# Переводимые поля любой модели на основе ContentModel
CONTENT_FIELDS = ('title', 'summary', 'body', 'cover_alt', 'meta_title', 'meta_description')
STEP_FIELDS = ('title', 'text', 'image_alt')


@register(SiteSettings)
class SiteSettingsTranslation(TranslationOptions):
    fields = ('tagline', 'about', 'copyright', 'hero_title', 'hero_subtitle', 'hero_cta_label', 'hero_image_alt')


@register(Section)
class SectionTranslation(TranslationOptions):
    fields = ('title', 'short_title', 'description', 'cover_alt')


@register(HomeFeatured)
class HomeFeaturedTranslation(TranslationOptions):
    fields = ('label',)


@register(GalleryImage)
class GalleryImageTranslation(TranslationOptions):
    fields = ('alt', 'caption')


@register(Fact)
class FactTranslation(TranslationOptions):
    fields = ('text',)
