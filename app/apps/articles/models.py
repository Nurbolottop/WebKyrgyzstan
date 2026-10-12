from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import ContentModel, CoverMixin, Fact, GalleryImage, PublishableModel, upload_to
from apps.base.validators import AUDIO_VALIDATORS

# Адреса, занятые собственными страницами разделов: категории с таким slug
# перекрыли бы их (/discover/regions/, /culture/play/ и т. д.).
RESERVED_CATEGORY_SLUGS = {
    'regions', 'places', 'play', 'quizzes', 'riddles', 'rebuses', 'kyrgyz',
    'recipes', 'master-classes', 'tasks',
}


class Category(PublishableModel, CoverMixin):
    section = models.ForeignKey(
        'base.Section', verbose_name='раздел', on_delete=models.PROTECT, related_name='categories'
    )
    title = models.CharField('название', max_length=100)
    slug = models.SlugField('адрес (slug)', max_length=100)
    description = models.TextField('описание', blank=True)

    class Meta(PublishableModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        constraints = [
            models.UniqueConstraint(fields=['section', 'slug'], name='category_unique_slug_in_section'),
        ]

    def __str__(self):
        return f'{self.section} → {self.title}'

    def clean(self):
        if self.slug in RESERVED_CATEGORY_SLUGS:
            raise ValidationError({'slug': 'Этот адрес занят служебной страницей раздела.'})


class Article(ContentModel):
    class Layout(models.TextChoices):
        STANDARD = 'standard', _('Article')
        PROFILE = 'profile', _('Profile')
        PROFESSION = 'profession', _('Profession')

    category = models.ForeignKey(
        Category, verbose_name='категория', on_delete=models.PROTECT, related_name='articles'
    )
    layout = models.CharField(
        'вид страницы', max_length=20, choices=Layout.choices, default=Layout.STANDARD,
        help_text='«Профиль» — история человека, «Профессия» — рассказ о профессии.',
    )
    subtitle = models.CharField(
        'подзаголовок', max_length=200, blank=True,
        help_text='Например, для профиля: «Чемпионка мира по борьбе».',
    )
    video_url = models.URLField('видео (YouTube)', blank=True)
    audio = models.FileField(
        'аудио', upload_to=upload_to, blank=True, validators=AUDIO_VALIDATORS,
        help_text='Например, звучание комуза. MP3, до 20 МБ.',
    )
    audio_title = models.CharField('название аудио', max_length=200, blank=True)
    audio_credit = models.CharField('автор и лицензия аудио', max_length=255, blank=True)

    regions = models.ManyToManyField(
        'discover.Region', verbose_name='связанные области', blank=True, related_name='articles'
    )
    related = models.ManyToManyField('self', verbose_name='похожие материалы', blank=True)

    gallery = GenericRelation(GalleryImage)
    facts = GenericRelation(Fact)

    class Meta(ContentModel.Meta):
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
