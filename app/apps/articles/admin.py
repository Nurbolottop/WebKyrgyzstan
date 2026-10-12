from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from apps.base.admin.inlines import FactInline, GalleryImageInline
from apps.base.admin.mixins import ContentAdmin

from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'section', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    list_filter = ('section',)
    search_fields = ('title_ru', 'title_ky', 'title_en')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('section', 'title', 'slug', 'description', 'cover', 'cover_alt', 'cover_credit', 'is_published', 'order')


@admin.register(Article)
class ArticleAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'category', 'layout', 'is_published', 'order', 'updated_at')
    list_filter = ('category__section', 'category', 'layout', 'is_published')
    list_select_related = ('category__section',)
    autocomplete_fields = ('category', 'regions', 'related')
    inlines = (GalleryImageInline, FactInline)
    extra_fieldsets = (
        ('Рубрика и вид', {'fields': ('category', 'layout', 'subtitle')}),
        ('Видео и аудио', {
            'classes': ('collapse',),
            'fields': ('video_url', 'audio', 'audio_title', 'audio_credit'),
        }),
        ('Связи', {'fields': ('regions', 'related')}),
    )
