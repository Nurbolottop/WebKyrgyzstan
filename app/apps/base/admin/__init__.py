from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from apps.base.models import HomeFeatured, Section, SiteSettings

admin.site.site_header = 'Web Kyrgyzstan'
admin.site.site_title = 'Web Kyrgyzstan'
admin.site.index_title = 'Управление контентом'


@admin.register(SiteSettings)
class SiteSettingsAdmin(TabbedTranslationAdmin):
    fieldsets = (
        (None, {'fields': ('site_name', 'tagline', 'about', 'copyright', 'default_og_image')}),
        ('Главная страница', {'fields': (
            'hero_title', 'hero_subtitle', 'hero_cta_label',
            'hero_image', 'hero_image_alt', 'hero_image_credit',
        )}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Section)
class SectionAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'key', 'order')
    list_editable = ('order',)
    readonly_fields = ('key',)
    fields = ('key', 'title', 'short_title', 'description', 'cover', 'cover_alt', 'cover_credit', 'order')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomeFeatured)
class HomeFeaturedAdmin(TabbedTranslationAdmin):
    list_display = ('__str__', 'label', 'order')
    list_editable = ('order',)
    autocomplete_fields = ('article', 'region', 'place', 'activity', 'quiz', 'game')
    fieldsets = (
        (None, {'fields': ('label', 'order')}),
        ('Материал (выберите один)', {
            'fields': ('article', 'region', 'place', 'activity', 'quiz', 'game'),
        }),
    )
