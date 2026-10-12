from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.choices import Difficulty
from apps.base.models import BaseStep, ContentModel, PublishedQuerySet, upload_to
from apps.base.validators import IMAGE_VALIDATORS


class Activity(ContentModel):
    """Рецепт, мастер-класс или творческое задание: список нужного + шаги."""

    class Kind(models.TextChoices):
        RECIPE = 'recipe', _('Recipe')
        MASTERCLASS = 'masterclass', _('Master class')
        TASK = 'task', _('Creative task')

    kind = models.CharField('вид', max_length=20, choices=Kind.choices)
    difficulty = models.CharField(
        'сложность', max_length=10, choices=Difficulty.choices, default=Difficulty.EASY
    )
    duration_min = models.PositiveSmallIntegerField('время, минут', null=True, blank=True)
    servings = models.PositiveSmallIntegerField('порций', null=True, blank=True, help_text='Только для рецептов.')
    safety_notes = models.TextField(
        'безопасность', blank=True,
        help_text='Обязательно для рецептов: что делать только вместе со взрослыми.',
    )
    sample_image = models.ImageField(
        'образец результата', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS
    )
    sample_image_alt = models.CharField('описание образца', max_length=200, blank=True)
    video_url = models.URLField('видео (YouTube)', blank=True)

    class Meta(ContentModel.Meta):
        verbose_name = 'практика'
        verbose_name_plural = 'практика'

    def clean(self):
        if self.kind == self.Kind.RECIPE and not self.safety_notes:
            raise ValidationError({'safety_notes': 'Для рецепта нужны рекомендации по безопасности.'})


class Supply(models.Model):
    """Ингредиент рецепта или материал для мастер-класса."""

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='supplies')
    order = models.PositiveIntegerField('порядок', default=0)
    name = models.CharField('что нужно', max_length=200)
    amount = models.CharField('сколько', max_length=100, blank=True)

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'ингредиент / материал'
        verbose_name_plural = 'ингредиенты / материалы'

    def __str__(self):
        return self.name


class ActivityStep(BaseStep):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='steps')

    class Meta(BaseStep.Meta):
        verbose_name = 'шаг'
        verbose_name_plural = 'шаги'


# ---------------------------------------------------------------------------
# Proxy-модели: отдельные пункты меню админки для каждого вида
# ---------------------------------------------------------------------------
class KindManager(models.Manager.from_queryset(PublishedQuerySet)):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind

    def get_queryset(self):
        return super().get_queryset().filter(kind=self.kind)


class KindProxy(Activity):
    KIND = None

    class Meta:
        proxy = True

    def clean(self):
        # Вид задаётся пунктом меню, а не полем формы; ставим его до проверок модели
        self.kind = self.KIND
        super().clean()

    def save(self, *args, **kwargs):
        self.kind = self.KIND
        super().save(*args, **kwargs)


class Recipe(KindProxy):
    KIND = Activity.Kind.RECIPE
    objects = KindManager(KIND)

    class Meta:
        proxy = True
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'


class MasterClass(KindProxy):
    KIND = Activity.Kind.MASTERCLASS
    objects = KindManager(KIND)

    class Meta:
        proxy = True
        verbose_name = 'мастер-класс'
        verbose_name_plural = 'мастер-классы'


class CreativeTask(KindProxy):
    KIND = Activity.Kind.TASK
    objects = KindManager(KIND)

    class Meta:
        proxy = True
        verbose_name = 'творческое задание'
        verbose_name_plural = 'творческие задания'
