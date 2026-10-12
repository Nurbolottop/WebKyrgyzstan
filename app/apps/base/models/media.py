from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.base.validators import IMAGE_VALIDATORS

from .abstract import upload_to


class GenericAttachment(models.Model):
    """Запись, которую можно прикрепить к статье, области или достопримечательности."""

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    order = models.PositiveIntegerField('порядок', default=0)

    class Meta:
        abstract = True
        ordering = ['order', 'pk']
        indexes = [models.Index(fields=['content_type', 'object_id'])]


class GalleryImage(GenericAttachment):
    image = models.ImageField('фото', upload_to=upload_to, validators=IMAGE_VALIDATORS)
    alt = models.CharField('что изображено', max_length=200)
    caption = models.CharField('подпись', max_length=300, blank=True)
    credit = models.CharField(
        'автор и лицензия', max_length=255,
        help_text='Например: «Фото: Иван Иванов, CC BY-SA 4.0, Wikimedia Commons».',
    )

    class Meta(GenericAttachment.Meta):
        verbose_name = 'фото галереи'
        verbose_name_plural = 'фотогалерея'

    def __str__(self):
        return self.alt


class Fact(GenericAttachment):
    text = models.TextField('факт')

    class Meta(GenericAttachment.Meta):
        verbose_name = 'интересный факт'
        verbose_name_plural = 'интересные факты'

    def __str__(self):
        return self.text[:80]
