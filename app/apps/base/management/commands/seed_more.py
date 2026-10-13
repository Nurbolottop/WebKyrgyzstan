"""
Дополнительное наполнение: переводы стартовых материалов, описания областей
и достопримечательностей, новые статьи, викторины, слова и загадки.

Заполняет только пустые поля — то, что уже отредактировано в админке, не меняется.
Повторный запуск безопасен.

    python manage.py seed_more
"""
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import translation

from apps.articles.models import Article, Category
from decimal import Decimal

from apps.base.content import geography, modern, more, places_extra, starter, translations
from apps.base.models import Fact, Section, SiteSettings
from apps.discover.models import Place, Region
from apps.learn.models import Answer, Game, Puzzle, Question, Quiz, Word, WordTopic
from apps.practice.models import Activity

LANGS = ('ky', 'ru', 'en')


def fill(obj, field, values):
    """Заполняет пустые языковые версии поля. values — (ky, ru, en) или {'ky': …, 'en': …}."""
    if isinstance(values, (tuple, list)):
        values = dict(zip(LANGS, values))
    changed = False
    for lang, value in values.items():
        name = f'{field}_{lang}'
        if value and not getattr(obj, name):
            setattr(obj, name, value)
            changed = True
    if changed and values.get('ru') and not getattr(obj, field + '_ru'):
        setattr(obj, field, values['ru'])
    return changed


class Command(BaseCommand):
    help = 'Переводы и новые материалы для всех разделов.'

    @transaction.atomic
    def handle(self, *args, **options):
        with translation.override('ru'):
            self.translate_starter()
            self.describe_geography()
            self.add_places()
            self.add_articles(more.ARTICLES + modern.ARTICLES)
            self.add_quizzes()
            self.add_words()
            self.add_puzzles()
            self.site_defaults()
        self.stdout.write(self.style.SUCCESS('Готово.'))

    # ----------------------------------------------------------------- переводы
    def translate_starter(self):
        for slug, data in translations.ARTICLES.items():
            article = Article.objects.filter(slug=slug).first()
            if not article:
                continue
            changed = fill(article, 'body', data['body'])
            article.save()
            for fact, (ky, en) in zip(article.facts.order_by('order', 'pk'), data.get('facts', [])):
                if fill(fact, 'text', {'ky': ky, 'en': en}):
                    fact.save()
            self.stdout.write(f'  перевод статьи {slug}: {"обновлено" if changed else "без изменений"}')

        for slug, data in translations.ACTIVITIES.items():
            activity = Activity.objects.filter(slug=slug).first()
            if not activity:
                continue
            fill(activity, 'body', data.get('body', {}))
            fill(activity, 'safety_notes', data.get('safety', {}))
            activity.save()
            for supply, (ky, en) in zip(activity.supplies.all(), data.get('supplies', [])):
                fill(supply, 'name', {'ky': ky[0], 'en': en[0]})
                fill(supply, 'amount', {'ky': ky[1], 'en': en[1]})
                supply.save()
            for step, (ky, en) in zip(activity.steps.all(), data.get('steps', [])):
                fill(step, 'title', {'ky': ky[0], 'en': en[0]})
                fill(step, 'text', {'ky': ky[1], 'en': en[1]})
                step.save()
            self.stdout.write(f'  перевод практики {slug}')

        for slug, items in translations.GAME_ITEMS.items():
            game = Game.objects.filter(slug=slug).first()
            if not game:
                continue
            for item, data in zip(game.items.order_by('order', 'pk'), items):
                for i, field in enumerate(('title', 'text', 'explanation')):
                    fill(item, field, {lang: data[lang][i] for lang in ('ky', 'en')})
                item.save()

        for source, data in zip(starter.PUZZLES, translations.PUZZLES):
            puzzle = Puzzle.objects.filter(prompt_ru=source['prompt']).first()
            if not puzzle:
                continue
            for field, key in (('prompt', 'prompt'), ('answer', 'answer'), ('alt_answers', 'alt'),
                               ('hint', 'hint'), ('explanation', 'explanation')):
                fill(puzzle, field, {lang: data[lang].get(key, '') for lang in ('ky', 'en')})
            puzzle.save()

    # ------------------------------------------------------------ география
    def describe_geography(self):
        for slug, data in geography.REGIONS.items():
            region = Region.objects.filter(slug=slug).first()
            if not region:
                continue
            for field in ('summary', 'body', 'geography', 'nature', 'culture'):
                fill(region, field, data[field])
            if region.area_km2 is None and data.get('area_km2'):
                region.area_km2 = data['area_km2']
            region.save()
            self.add_facts(region, data.get('facts', []))
            self.stdout.write(f'  область {slug}')

        for slug, data in geography.PLACES.items():
            place = Place.objects.filter(slug=slug).first()
            if not place:
                continue
            fill(place, 'summary', data['summary'])
            fill(place, 'body', data['body'])
            place.save()
            self.add_facts(place, data.get('facts', []))
            self.stdout.write(f'  достопримечательность {slug}')

    def add_places(self):
        for data in places_extra.PLACES:
            if Place.objects.filter(slug=data['slug']).exists():
                continue
            place = Place(slug=data['slug'], region=Region.objects.get(slug=data['region']), kind=data['kind'],
                          latitude=Decimal(data['lat']), longitude=Decimal(data['lon']),
                          order=Place.objects.count() + 1)
            for field in ('title', 'summary', 'body', 'key_value', 'key_label'):
                fill(place, field, data[field])
            place.save()
            self.add_facts(place, data.get('facts', []))
            self.stdout.write(f'  новая достопримечательность {data["slug"]}')

    def add_facts(self, obj, facts):
        if obj.facts.exists():
            return
        for order, values in enumerate(facts, start=1):
            fact = Fact(content_object=obj, order=order)
            fill(fact, 'text', values)
            fact.save()

    # ------------------------------------------------------------ новые материалы
    def add_articles(self, articles):
        start = Article.objects.count()
        for i, data in enumerate(articles, start=1):
            section_key, category_slug = data['category']
            category = Category.objects.filter(section__key=section_key, slug=category_slug).first()
            if not category or Article.objects.filter(slug=data['slug']).exists():
                continue
            article = Article(slug=data['slug'], category=category, order=start + i,
                              layout=data.get('layout', 'standard'))
            for field in ('title', 'summary', 'body'):
                fill(article, field, data[field])
            article.save()
            self.add_facts(article, data.get('facts', []))
            self.stdout.write(f'  новая статья {data["slug"]}')

    def add_quizzes(self):
        for order, data in enumerate(more.QUIZZES, start=3):
            if Quiz.objects.filter(slug=data['slug']).exists():
                continue
            quiz = Quiz(slug=data['slug'], topic=data['topic'], difficulty=data.get('difficulty', 'easy'), order=order)
            fill(quiz, 'title', data['title'])
            fill(quiz, 'summary', data['summary'])
            quiz.save()
            for q_order, q in enumerate(data['questions'], start=1):
                question = Question(quiz=quiz, order=q_order, show_on_home=q.get('home', False))
                fill(question, 'text', q['text'])
                fill(question, 'explanation', q['explanation'])
                question.save()
                for a_order, (texts, correct) in enumerate(q['answers'], start=1):
                    answer = Answer(question=question, order=a_order, is_correct=correct)
                    fill(answer, 'text', texts)
                    answer.save()
            self.stdout.write(f'  новая викторина {data["slug"]}')

    def add_words(self):
        for order, data in enumerate(more.WORD_TOPICS, start=3):
            if WordTopic.objects.filter(slug=data['slug']).exists():
                continue
            topic = WordTopic(slug=data['slug'], order=order)
            fill(topic, 'title', data['title'])
            fill(topic, 'summary', data['summary'])
            topic.save()
            for i, (kyrgyz, latin, ru, en) in enumerate(data['words'], start=1):
                word = Word(topic=topic, order=i, kyrgyz=kyrgyz, transliteration=latin)
                fill(word, 'translation', {'ru': ru, 'en': en})
                word.save()
            self.stdout.write(f'  новая тема слов {data["slug"]}')

    def add_puzzles(self):
        start = Puzzle.objects.count()
        for i, data in enumerate(more.PUZZLES, start=1):
            if Puzzle.objects.filter(prompt_ru=data['ru']['prompt']).exists():
                continue
            puzzle = Puzzle(kind='riddle', topic=data.get('topic', ''), order=start + i)
            for field, key in (('prompt', 'prompt'), ('answer', 'answer'), ('alt_answers', 'alt'),
                               ('hint', 'hint'), ('explanation', 'explanation')):
                fill(puzzle, field, {lang: data[lang].get(key, '') for lang in LANGS})
            puzzle.save()
            self.stdout.write(f'  новая загадка: {puzzle.answer}')

    # ------------------------------------------------------------ сайт
    def site_defaults(self):
        site = SiteSettings.load()
        if not site.default_og_image:
            cover = Section.objects.get(key='discover').cover
            if cover:
                site.default_og_image.save('og-default.jpg', ContentFile(cover.read()), save=False)
        fill(site, 'tagline', (
            'Кыргызстан жөнүндө балдар үчүн интерактивдүү сайт',
            'Интерактивный сайт о Кыргызстане для детей',
            'An interactive website about Kyrgyzstan for children',
        ))
        site.save()
