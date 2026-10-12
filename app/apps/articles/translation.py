from modeltranslation.translator import TranslationOptions, register

from apps.base.translation import CONTENT_FIELDS

from .models import Article, Category


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('title', 'description', 'cover_alt')


@register(Article)
class ArticleTranslation(TranslationOptions):
    fields = CONTENT_FIELDS + ('subtitle', 'audio_title')
