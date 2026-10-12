from django.contrib import admin

from apps.base.admin.inlines import FactInline, GalleryImageInline
from apps.base.admin.mixins import ContentAdmin

from .models import Place, Region


class PlaceInline(admin.TabularInline):
    model = Place
    fields = ('title', 'kind', 'is_published', 'order')
    readonly_fields = ('title', 'kind')
    extra = 0
    show_change_link = True
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Region)
class RegionAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'kind', 'capital', 'is_published', 'order')
    list_filter = ('kind', 'is_published')
    inlines = (PlaceInline, GalleryImageInline, FactInline)
    extra_fieldsets = (
        ('Основные данные', {'fields': ('kind', 'map_id', 'capital', 'area_km2', 'population', 'population_year')}),
        ('Разделы страницы', {'fields': ('geography', 'nature', 'culture')}),
    )


@admin.register(Place)
class PlaceAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'region', 'kind', 'is_published', 'order')
    list_filter = ('region', 'kind', 'is_published')
    list_select_related = ('region',)
    autocomplete_fields = ('region',)
    inlines = (GalleryImageInline, FactInline)
    extra_fieldsets = (
        ('Где и что', {'fields': ('region', 'kind', ('latitude', 'longitude'), ('key_value', 'key_label'))}),
    )
