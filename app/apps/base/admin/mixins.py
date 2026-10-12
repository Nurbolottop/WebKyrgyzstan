from django.contrib import admin, messages
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin

SEO_FIELDSET = ('SEO', {
    'classes': ('collapse',),
    'fields': ('meta_title', 'meta_description', 'og_image'),
})
COVER_FIELDSET = ('Обложка', {
    'fields': ('cover', 'cover_alt', 'cover_credit'),
})
PUBLICATION_FIELDSET = ('Публикация', {
    'fields': ('is_published', 'order', 'published_at'),
})


def thumbnail(image, size=60):
    if not image:
        return '—'
    return format_html(
        '<img src="{}" alt="" style="width:{}px;height:{}px;object-fit:cover;border-radius:6px">',
        image.url, size, size,
    )


@admin.action(description='Опубликовать выбранные')
def publish(modeladmin, request, queryset):
    count = queryset.update(is_published=True)
    modeladmin.message_user(request, f'Опубликовано: {count}', messages.SUCCESS)


@admin.action(description='Снять с публикации')
def unpublish(modeladmin, request, queryset):
    count = queryset.update(is_published=False)
    modeladmin.message_user(request, f'Снято с публикации: {count}', messages.SUCCESS)


class ContentAdmin(TabbedTranslationAdmin):
    """Базовая админка для моделей на основе ContentModel."""

    list_display = ('cover_preview', 'title', 'is_published', 'order', 'updated_at')
    list_display_links = ('cover_preview', 'title')
    list_editable = ('is_published', 'order')
    list_filter = ('is_published',)
    search_fields = ('title_ru', 'title_ky', 'title_en', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = (publish, unpublish)
    list_per_page = 50

    # Поля, специфичные для модели, — между основным текстом и обложкой
    extra_fieldsets = ()

    def __init__(self, *args, **kwargs):
        # Собираем именно атрибут fieldsets: modeltranslation разворачивает в нём
        # переводимые поля (title → title_ky/title_ru/title_en)
        main = (None, {'fields': ('title', 'slug', 'summary', 'body')})
        self.fieldsets = (main, *self.extra_fieldsets, COVER_FIELDSET, PUBLICATION_FIELDSET, SEO_FIELDSET)
        super().__init__(*args, **kwargs)

    @admin.display(description='Обложка')
    def cover_preview(self, obj):
        return thumbnail(obj.cover)
