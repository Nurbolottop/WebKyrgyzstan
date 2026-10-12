from django.contrib import admin
from modeltranslation.admin import TranslationStackedInline, TranslationTabularInline

from apps.base.admin.mixins import ContentAdmin

from .models import Activity, ActivityStep, CreativeTask, MasterClass, Recipe, Supply


class SupplyInline(TranslationTabularInline):
    model = Supply
    fields = ('order', 'name', 'amount')
    extra = 0


class StepInline(TranslationStackedInline):
    model = ActivityStep
    fields = (('order', 'title'), 'text', ('image', 'image_alt'), 'video_url')
    extra = 0


class ActivityAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'difficulty', 'duration_min', 'is_published', 'order')
    list_filter = ('difficulty', 'is_published')
    inlines = (SupplyInline, StepInline)
    extra_fieldsets = (
        ('Параметры', {'fields': ('difficulty', 'duration_min')}),
        ('Образец и видео', {'fields': ('sample_image', 'sample_image_alt', 'video_url')}),
        ('Безопасность', {'fields': ('safety_notes',)}),
    )


@admin.register(Activity)
class AllActivityAdmin(ActivityAdmin):
    """Все виды сразу. В меню скрыта, нужна для выбора материала в «Избранном на главной»."""

    list_display = ('cover_preview', 'title', 'kind', 'is_published', 'order')
    list_filter = ('kind', 'is_published')

    def get_model_perms(self, request):
        return {}

    def has_add_permission(self, request):
        return False


@admin.register(Recipe)
class RecipeAdmin(ActivityAdmin):
    extra_fieldsets = (
        ('Параметры', {'fields': ('difficulty', 'duration_min', 'servings')}),
        ('Безопасность', {'fields': ('safety_notes',)}),
        ('Видео', {'fields': ('video_url',)}),
    )


@admin.register(MasterClass)
class MasterClassAdmin(ActivityAdmin):
    pass


@admin.register(CreativeTask)
class CreativeTaskAdmin(ActivityAdmin):
    pass
