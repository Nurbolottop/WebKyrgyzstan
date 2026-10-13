import random

from django.shortcuts import render

from apps.discover.models import Place
from apps.discover.services import map_context
from apps.learn.models import Question
from apps.learn.services import question_payload

from .models import HomeFeatured


def _featured():
    items = HomeFeatured.objects.select_related(
        'article__category__section', 'region', 'place__region', 'activity', 'quiz', 'game__section'
    )
    result = [item for item in items if item.target is not None and item.target.is_published]
    if result:
        return result
    # Пока избранное не выбрано в админке — показываем достопримечательности
    return [HomeFeatured(place=place) for place in Place.objects.published().select_related('region')[:6]]


def home(request):
    questions = list(
        Question.objects.filter(show_on_home=True, quiz__is_published=True)
        .select_related('quiz').prefetch_related('answers')
    )
    question = random.choice(questions) if questions else None
    return render(request, 'home/index.html', {
        'featured': _featured(),
        'map': map_context(),
        'mini_quiz': question,
        'mini_quiz_payload': {'questions': [question_payload(question)]} if question else None,
    })


def robots_txt(request):
    return render(request, 'robots.txt', content_type='text/plain')
