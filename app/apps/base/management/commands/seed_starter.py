"""
Стартовые материалы для всех пяти разделов: статьи, рецепт, мастер-класс,
творческое задание, загадки, слова, игры, вторая викторина и избранное на главной.

Полный текст статей — на русском; названия и краткие описания — на трёх языках
(для ky/en текст показывается по-русски, пока редакция не добавит перевод).
Повторный запуск ничего не дублирует и не перезаписывает правки из админки.

    python manage.py seed_starter
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import translation

from apps.articles.models import Article, Category
from apps.base.models import Fact, HomeFeatured, Section
from apps.discover.models import Region
from apps.learn.models import Answer, Game, GameItem, Puzzle, Question, Quiz, Topic, Word, WordTopic
from apps.practice.models import Activity, ActivityStep, Supply

from apps.base.content.starter import ACTIVITIES, ARTICLES, GAMES, PUZZLES, QUIZ, WORD_TOPICS


def tr(field, values):
    ky, ru, en = values
    return {f'{field}_ky': ky, f'{field}_ru': ru, f'{field}_en': en}


class Command(BaseCommand):
    help = 'Стартовые материалы для всех разделов сайта.'

    @transaction.atomic
    def handle(self, *args, **options):
        with translation.override('ru'):
            articles = self.seed_articles()
            activities = self.seed_activities()
            self.seed_puzzles()
            topics = self.seed_words()
            games = self.seed_games(topics)
            self.seed_quiz()
            self.seed_featured(articles, activities, games)
        self.stdout.write(self.style.SUCCESS('Готово.'))

    def log(self, label, obj, created):
        self.stdout.write(f'  {label}: {obj} — {"создано" if created else "уже есть"}')

    def seed_articles(self):
        result = {}
        for order, data in enumerate(ARTICLES, start=1):
            section_key, category_slug = data['category']
            category = Category.objects.get(section__key=section_key, slug=category_slug)
            article, created = Article.objects.get_or_create(
                slug=data['slug'],
                defaults={
                    'category': category, 'order': order, 'layout': data.get('layout', 'standard'),
                    **tr('title', data['title']), **tr('summary', data['summary']), 'body_ru': data['body'],
                    'body': data['body'],
                },
            )
            if created:
                article.regions.set(Region.objects.filter(slug__in=data.get('regions', [])))
                for i, text in enumerate(data.get('facts', []), start=1):
                    Fact.objects.create(content_object=article, order=i, text_ru=text, text=text)
            result[data['slug']] = article
            self.log('Статья', article, created)
        return result

    def seed_activities(self):
        result = {}
        for order, data in enumerate(ACTIVITIES, start=1):
            activity, created = Activity.objects.get_or_create(
                slug=data['slug'],
                defaults={
                    'kind': data['kind'], 'order': order, 'difficulty': data['difficulty'],
                    'duration_min': data.get('duration'), 'servings': data.get('servings'),
                    **tr('title', data['title']), **tr('summary', data['summary']),
                    'body_ru': data.get('body', ''), 'body': data.get('body', ''),
                    'safety_notes_ru': data.get('safety', ''), 'safety_notes': data.get('safety', ''),
                },
            )
            if created:
                for i, (name, amount) in enumerate(data.get('supplies', []), start=1):
                    Supply.objects.create(activity=activity, order=i, name_ru=name, name=name, amount_ru=amount, amount=amount)
                for i, (title, text) in enumerate(data['steps'], start=1):
                    ActivityStep.objects.create(activity=activity, order=i, title_ru=title, title=title, text_ru=text, text=text)
            result[data['slug']] = activity
            self.log('Практика', activity, created)
        return result

    def seed_puzzles(self):
        for order, data in enumerate(PUZZLES, start=1):
            puzzle, created = Puzzle.objects.get_or_create(
                kind='riddle', prompt_ru=data['prompt'],
                defaults={
                    'order': order, 'topic': data['topic'], 'prompt': data['prompt'],
                    'answer_ru': data['answer'], 'answer': data['answer'],
                    'alt_answers_ru': data.get('alt', ''), 'hint_ru': data.get('hint', ''),
                    'explanation_ru': data.get('explanation', ''),
                },
            )
            self.log('Загадка', puzzle, created)

    def seed_words(self):
        result = {}
        for order, data in enumerate(WORD_TOPICS, start=1):
            topic, created = WordTopic.objects.get_or_create(
                slug=data['slug'],
                defaults={'order': order, **tr('title', data['title']), **tr('summary', data['summary'])},
            )
            if created:
                for i, (kyrgyz, latin, ru, en) in enumerate(data['words'], start=1):
                    Word.objects.create(
                        topic=topic, order=i, kyrgyz=kyrgyz, transliteration=latin,
                        translation=ru, translation_ru=ru, translation_en=en,
                    )
            result[data['slug']] = topic
            self.log('Тема слов', topic, created)
        return result

    def seed_games(self, topics):
        result = {}
        for order, data in enumerate(GAMES, start=1):
            game, created = Game.objects.get_or_create(
                slug=data['slug'],
                defaults={
                    'order': order, 'engine': data['engine'], 'source': data['source'],
                    'section': Section.objects.get(key=data['section']),
                    'word_topic': topics.get(data.get('word_topic')),
                    **tr('title', data['title']), **tr('summary', data['summary']),
                    **tr('instructions', data['instructions']),
                },
            )
            if created:
                for i, item in enumerate(data.get('items', []), start=1):
                    GameItem.objects.create(
                        game=game, order=i, title_ru=item['title'], title=item['title'],
                        text_ru=item.get('text', ''), svg_layer=item.get('layer', ''),
                        is_distractor=item.get('distractor', False), explanation_ru=item.get('explanation', ''),
                    )
            result[data['slug']] = game
            self.log('Игра', game, created)
        return result

    def seed_quiz(self):
        quiz, created = Quiz.objects.get_or_create(
            slug=QUIZ['slug'],
            defaults={
                'topic': Topic.CULTURE, 'section': Section.objects.get(key='culture'), 'order': 2,
                **tr('title', QUIZ['title']), **tr('summary', QUIZ['summary']),
            },
        )
        self.log('Викторина', quiz, created)
        if not created:
            return
        for q_order, data in enumerate(QUIZ['questions'], start=1):
            question = Question.objects.create(
                quiz=quiz, order=q_order, show_on_home=data.get('home', False),
                **tr('text', data['text']), **tr('explanation', data['explanation']),
            )
            for a_order, (texts, correct) in enumerate(data['answers'], start=1):
                Answer.objects.create(question=question, order=a_order, is_correct=correct, **tr('text', texts))

    def seed_featured(self, articles, activities, games):
        if HomeFeatured.objects.exists():
            self.stdout.write('  Избранное на главной уже заполнено')
            return
        items = [
            {'article': articles['why-issyk-kul-does-not-freeze']},
            {'article': articles['how-a-yurt-is-built']},
            {'article': articles['what-is-a-komuz']},
            {'activity': activities['boorsok']},
            {'article': articles['it-in-kyrgyzstan']},
            {'game': games['build-a-yurt']},
        ]
        for order, item in enumerate(items, start=1):
            HomeFeatured.objects.create(order=order, **item)
        self.stdout.write(f'  Избранное на главной: {len(items)}')
