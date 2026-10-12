from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

# Материалы, которые можно вывести в блоке «Интересные материалы» на главной
FEATURED_TARGETS = ('article', 'region', 'place', 'activity', 'quiz', 'game')


def _exactly_one_target():
    condition = Q()
    for field in FEATURED_TARGETS:
        term = Q(**{f'{field}__isnull': False})
        for other in FEATURED_TARGETS:
            if other != field:
                term &= Q(**{f'{other}__isnull': True})
        condition |= term
    return condition


class HomeFeatured(models.Model):
    order = models.PositiveIntegerField('порядок', default=0)
    label = models.CharField(
        'плашка', max_length=60, blank=True, help_text='Необязательно, например «Знаешь ли ты?».'
    )

    article = models.ForeignKey(
        'articles.Article', verbose_name='статья', on_delete=models.CASCADE, null=True, blank=True
    )
    region = models.ForeignKey(
        'discover.Region', verbose_name='область / город', on_delete=models.CASCADE, null=True, blank=True
    )
    place = models.ForeignKey(
        'discover.Place', verbose_name='достопримечательность', on_delete=models.CASCADE, null=True, blank=True
    )
    activity = models.ForeignKey(
        'practice.Activity', verbose_name='рецепт / мастер-класс / задание',
        on_delete=models.CASCADE, null=True, blank=True,
    )
    quiz = models.ForeignKey(
        'learn.Quiz', verbose_name='викторина', on_delete=models.CASCADE, null=True, blank=True
    )
    game = models.ForeignKey(
        'learn.Game', verbose_name='игра', on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'избранное на главной'
        verbose_name_plural = 'избранное на главной'
        constraints = [
            models.CheckConstraint(condition=_exactly_one_target(), name='home_featured_exactly_one_target'),
        ]

    def __str__(self):
        return str(self.target) if self.target else 'Пустая запись'

    @property
    def target(self):
        for field in FEATURED_TARGETS:
            obj = getattr(self, field)
            if obj is not None:
                return obj
        return None

    def clean(self):
        filled = [f for f in FEATURED_TARGETS if getattr(self, f'{f}_id')]
        if len(filled) != 1:
            raise ValidationError('Выберите ровно один материал.')
