from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet


class AnswerInlineFormSet(BaseInlineFormSet):
    """У вопроса минимум два варианта и ровно один правильный."""

    def clean(self):
        super().clean()
        answers = [
            form.cleaned_data for form in self.forms
            if form.cleaned_data and not form.cleaned_data.get('DELETE')
        ]
        if len(answers) < 2:
            raise ValidationError('Добавьте хотя бы два варианта ответа.')
        correct = sum(1 for answer in answers if answer.get('is_correct'))
        if correct != 1:
            raise ValidationError('Отметьте ровно один правильный ответ.')
