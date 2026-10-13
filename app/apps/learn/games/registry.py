"""
Реестр игровых механик.

Каждая механика — это JS-модуль (static/js/modules/engines/<module>.js) и функция,
которая готовит для него данные из БД. Новая игра на существующей механике
создаётся в админке; новая механика — новый модуль + запись в ENGINES.
"""
import random

from apps.discover.models import Place, Region
from apps.learn.models import Game
from apps.learn.services import image_src

OPTIONS_PER_ROUND = 4


def _items(game):
    return list(game.items.all())


def _rounds(entries, prompt_key, answer_key):
    """Раунды «выбери правильный ответ»: правильный вариант + случайные чужие."""
    pool = [e[answer_key] for e in entries]
    rounds = []
    for entry in entries:
        wrong = [a for a in pool if a != entry[answer_key]]
        options = random.sample(wrong, min(len(wrong), OPTIONS_PER_ROUND - 1)) + [entry[answer_key]]
        random.shuffle(options)
        rounds.append({
            'text': entry.get(prompt_key, ''),
            'image': entry.get('image', ''),
            'imageAlt': entry.get('imageAlt', ''),
            'explanation': entry.get('explanation', ''),
            'answers': [{'text': o, 'correct': o == entry[answer_key]} for o in options],
        })
    random.shuffle(rounds)
    return rounds


def choice_payload(game):
    if game.source == Game.Source.PLACES:
        entries = [
            {'prompt': '', 'answer': p.title, 'image': image_src(p.cover), 'imageAlt': p.cover_alt,
             'explanation': p.summary}
            for p in Place.objects.published() if p.cover
        ]
    elif game.source == Game.Source.WORDS and game.word_topic:
        entries = [
            {'prompt': w.kyrgyz, 'answer': w.translation, 'image': image_src(w.image), 'imageAlt': w.image_alt}
            for w in game.word_topic.words.all()
        ]
    else:
        entries = [
            {'prompt': i.text, 'answer': i.title, 'image': image_src(i.image), 'imageAlt': i.image_alt,
             'explanation': i.explanation}
            for i in _items(game) if not i.is_distractor
        ]
    return {'questions': _rounds(entries, 'prompt', 'answer')}


def pairs_payload(game):
    if game.source == Game.Source.WORDS and game.word_topic:
        pairs = [
            {'a': w.kyrgyz, 'b': w.translation, 'image': image_src(w.image, 480)}
            for w in game.word_topic.words.all()
        ]
    else:
        pairs = [
            {'a': i.title, 'b': i.pair_text, 'image': image_src(i.image, 480)}
            for i in _items(game) if i.pair_text and not i.is_distractor
        ]
    return {'pairs': pairs}


def map_guess_payload(game):
    targets = [{'id': r.map_id, 'title': r.title} for r in Region.objects.published()]
    random.shuffle(targets)
    return {'targets': targets}


def assembly_payload(game):
    steps = [
        {'title': i.title, 'text': i.text, 'layer': i.svg_layer, 'image': image_src(i.image, 480),
         'explanation': i.explanation, 'distractor': i.is_distractor}
        for i in _items(game)
    ]
    return {'steps': [s for s in steps if not s['distractor']], 'distractors': [s for s in steps if s['distractor']]}


ENGINES = {
    Game.Engine.CHOICE: {'module': 'quiz', 'payload': choice_payload},
    Game.Engine.MATCH: {'module': 'pairs', 'payload': pairs_payload},
    Game.Engine.MEMORY: {'module': 'pairs', 'payload': pairs_payload},
    Game.Engine.MAP_GUESS: {'module': 'map-guess', 'payload': map_guess_payload},
    Game.Engine.ASSEMBLY: {'module': 'assembly', 'payload': assembly_payload},
}


def build(game):
    engine = ENGINES[game.engine]
    payload = engine['payload'](game)
    payload['engine'] = game.engine
    return engine['module'], payload
