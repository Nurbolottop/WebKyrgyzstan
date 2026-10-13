from django.shortcuts import get_object_or_404, render

from apps.base.models import Section

from .games import registry
from .models import Game, Puzzle, Quiz, Topic, WordTopic
from .services import quiz_payload


def _section():
    return Section.objects.get(key='learn')


def index(request):
    return render(request, 'learn/index.html', {
        'section': _section(),
        'quizzes': Quiz.objects.published()[:6],
        'riddle_count': Puzzle.objects.published().filter(kind=Puzzle.Kind.RIDDLE).count(),
        'rebus_count': Puzzle.objects.published().filter(kind=Puzzle.Kind.REBUS).count(),
        'word_topics': WordTopic.objects.published()[:4],
        'games': Game.objects.published().filter(section__key='learn')[:6],
    })


def quiz_list(request):
    quizzes = Quiz.objects.published()
    topic = request.GET.get('topic', '')
    if topic not in Topic.values:
        topic = ''
    if topic:
        quizzes = quizzes.filter(topic=topic)
    return render(request, 'learn/quiz_list.html', {
        'section': _section(), 'quizzes': quizzes, 'topics': Topic.choices, 'current_topic': topic,
    })


def quiz_detail(request, slug):
    quiz = get_object_or_404(Quiz.objects.published(), slug=slug)
    return render(request, 'learn/quiz_detail.html', {
        'section': _section(),
        'quiz': quiz,
        'payload': quiz_payload(quiz),
        'more': Quiz.objects.published().exclude(pk=quiz.pk)[:3],
    })


def puzzle_list(request, kind):
    return render(request, 'learn/puzzle_list.html', {
        'section': _section(),
        'kind': kind,
        'kind_label': Puzzle.Kind(kind).label,
        'puzzles': Puzzle.objects.published().filter(kind=kind),
    })


def word_topic_list(request):
    return render(request, 'learn/wordtopic_list.html', {
        'section': _section(), 'topics': WordTopic.objects.published(),
    })


def word_topic_detail(request, slug):
    topic = get_object_or_404(WordTopic.objects.published(), slug=slug)
    return render(request, 'learn/wordtopic_detail.html', {
        'section': _section(),
        'topic': topic,
        'words': topic.words.all(),
        'games': topic.games.published(),
    })


def game_list(request):
    return render(request, 'learn/game_list.html', {
        'section': _section(), 'games': Game.objects.published().select_related('section'),
    })


def game_detail(request, slug, section_key='learn'):
    game = get_object_or_404(Game.objects.published().select_related('section'), slug=slug, section__key=section_key)
    module, payload = registry.build(game)
    return render(request, 'learn/game_detail.html', {
        'section': game.section, 'game': game, 'module': module, 'payload': payload,
    })
