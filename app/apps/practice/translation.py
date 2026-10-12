from modeltranslation.translator import TranslationOptions, register

from apps.base.translation import CONTENT_FIELDS, STEP_FIELDS

from .models import Activity, ActivityStep, CreativeTask, KindProxy, MasterClass, Recipe, Supply


@register(Activity)
class ActivityTranslation(TranslationOptions):
    fields = CONTENT_FIELDS + ('safety_notes', 'sample_image_alt')


@register(Supply)
class SupplyTranslation(TranslationOptions):
    fields = ('name', 'amount')


@register(ActivityStep)
class ActivityStepTranslation(TranslationOptions):
    fields = STEP_FIELDS


@register([KindProxy, Recipe, MasterClass, CreativeTask])
class ActivityProxyTranslation(TranslationOptions):
    # Proxy-модели наследуют переводимые поля Activity
    fields = ()
