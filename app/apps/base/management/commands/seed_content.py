"""
Начальное наполнение: области и города, достопримечательности, категории,
демо-викторина. Команду можно запускать повторно — записи обновляются по slug,
а тексты, уже отредактированные в админке, не затираются.

    python manage.py seed_content
"""
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import translation

from apps.articles.models import Category
from apps.base.models import Section
from apps.discover.models import Place, Region
from apps.learn.models import Answer, Question, Quiz, Topic


def tr(field, ky, ru, en):
    """Значения поля на трёх языках для modeltranslation."""
    return {f'{field}_ky': ky, f'{field}_ru': ru, f'{field}_en': en}


REGIONS = [
    # slug, kind, (ky, ru, en), (центр ky, ru, en)
    ('chuy', 'oblast', ('Чүй облусу', 'Чуйская область', 'Chuy Region'), ('Бишкек', 'Бишкек', 'Bishkek')),
    ('talas', 'oblast', ('Талас облусу', 'Таласская область', 'Talas Region'), ('Талас', 'Талас', 'Talas')),
    ('issyk-kul', 'oblast', ('Ысык-Көл облусу', 'Иссык-Кульская область', 'Issyk-Kul Region'),
     ('Каракол', 'Каракол', 'Karakol')),
    ('naryn', 'oblast', ('Нарын облусу', 'Нарынская область', 'Naryn Region'), ('Нарын', 'Нарын', 'Naryn')),
    ('jalal-abad', 'oblast', ('Жалал-Абад облусу', 'Джалал-Абадская область', 'Jalal-Abad Region'),
     ('Жалал-Абад', 'Джалал-Абад', 'Jalal-Abad')),
    ('osh-region', 'oblast', ('Ош облусу', 'Ошская область', 'Osh Region'), ('Ош', 'Ош', 'Osh')),
    ('batken', 'oblast', ('Баткен облусу', 'Баткенская область', 'Batken Region'), ('Баткен', 'Баткен', 'Batken')),
    ('bishkek', 'city', ('Бишкек шаары', 'Город Бишкек', 'Bishkek City'), ('', '', '')),
    ('osh-city', 'city', ('Ош шаары', 'Город Ош', 'Osh City'), ('', '', '')),
]

PLACES = [
    # slug, регион, тип, (ky, ru, en), широта, долгота, главная цифра (ky, ru, en), подпись (ky, ru, en)
    ('issyk-kul-lake', 'issyk-kul', 'lake', ('Ысык-Көл', 'Озеро Иссык-Куль', 'Lake Issyk-Kul'),
     '42.43000', '77.20000', ('1607 м', '1607 м', '1,607 m'),
     ('деңиз деңгээлинен бийиктиги', 'высота над уровнем моря', 'above sea level')),
    ('son-kul-lake', 'naryn', 'lake', ('Соң-Көл', 'Озеро Сон-Куль', 'Lake Son-Kul'),
     '41.83000', '75.13000', ('3016 м', '3016 м', '3,016 m'),
     ('деңиз деңгээлинен бийиктиги', 'высота над уровнем моря', 'above sea level')),
    ('sulaiman-too', 'osh-city', 'historic', ('Сулайман-Тоо', 'Сулайман-Тоо', 'Sulaiman-Too'),
     '40.53000', '72.79000', ('2009', '2009', '2009'),
     ('ЮНЕСКОнун тизмесине кирген жылы', 'год включения в список ЮНЕСКО', 'UNESCO World Heritage since')),
    ('tash-rabat', 'naryn', 'historic', ('Таш-Рабат', 'Таш-Рабат', 'Tash Rabat'),
     '40.82000', '75.29000', ('', '', ''), ('', '', '')),
    ('burana-tower', 'chuy', 'historic', ('Бурана мунарасы', 'Башня Бурана', 'Burana Tower'),
     '42.74600', '75.25000', ('', '', ''), ('', '', '')),
    ('arslanbob', 'jalal-abad', 'nature', ('Арстанбап', 'Арсланбоб', 'Arslanbob'),
     '41.33000', '72.94000', ('', '', ''), ('', '', '')),
    ('ala-archa', 'chuy', 'nature', ('Ала-Арча', 'Ала-Арча', 'Ala-Archa'),
     '42.56000', '74.48000', ('', '', ''), ('', '', '')),
    ('sary-chelek', 'jalal-abad', 'lake', ('Сары-Челек', 'Сары-Челек', 'Sary-Chelek'),
     '41.87000', '71.96000', ('', '', ''), ('', '', '')),
]

CATEGORIES = {
    'culture': [
        ('yurt', ('Боз үй', 'Юрта', 'The Yurt')),
        ('crafts', ('Кол өнөрчүлүк', 'Ремёсла', 'Crafts')),
        ('music', ('Музыка', 'Музыка', 'Music')),
        ('clothing', ('Улуттук кийим', 'Национальная одежда', 'National Dress')),
        ('holidays', ('Майрамдар жана үрп-адаттар', 'Праздники и обычаи', 'Holidays and Customs')),
        ('manas', ('«Манас» эпосу', 'Эпос «Манас»', 'The Manas Epic')),
    ],
    'modern': [
        ('sport', ('Спорт', 'Спорт', 'Sport')),
        ('technology', ('Технологиялар', 'Технологии', 'Technology')),
        ('youth', ('Жаштардын жетишкендиктери', 'Достижения молодёжи', 'Youth Achievements')),
        ('professions', ('Кызыктуу кесиптер', 'Интересные профессии', 'Interesting Professions')),
        ('modern-life', ('Азыркы турмуш', 'Современная жизнь', 'Modern Life')),
    ],
    'discover': [
        ('nature', ('Жаратылыш', 'Природа', 'Nature')),
    ],
}

QUIZ = {
    'slug': 'kyrgyzstan-geography',
    'title': ('Кыргызстандын географиясы', 'География Кыргызстана', 'Geography of Kyrgyzstan'),
    'summary': (
        'Тоолор, көлдөр жана шаарлар боюнча суроолор.',
        'Вопросы о горах, озёрах и городах.',
        'Questions about mountains, lakes and cities.',
    ),
    'questions': [
        {
            'text': (
                'Кыргызстандагы эң бийик чоку кайсы?',
                'Какая вершина самая высокая в Кыргызстане?',
                'What is the highest peak in Kyrgyzstan?',
            ),
            'explanation': (
                'Жеңиш чокусунун бийиктиги — 7439 метр.',
                'Пик Победы (Жеңиш чокусу) поднимается на 7439 метров.',
                'Jengish Chokusu (Victory Peak) rises to 7,439 metres.',
            ),
            'show_on_home': True,
            'answers': [
                (('Жеңиш чокусу', 'Пик Победы', 'Jengish Chokusu (Victory Peak)'), True),
                (('Ленин чокусу', 'Пик Ленина', 'Lenin Peak'), False),
                (('Хан-Теңири', 'Хан-Тенгри', 'Khan Tengri'), False),
                (('Корженевская чокусу', 'Пик Корженевской', 'Korzhenevskaya Peak'), False),
            ],
        },
        {
            'text': (
                'Кыргызстандагы эң чоң көл кайсы?',
                'Какое озеро самое большое в Кыргызстане?',
                'What is the largest lake in Kyrgyzstan?',
            ),
            'explanation': (
                'Ысык-Көл — дүйнөдөгү эң чоң бийик тоолуу көлдөрдүн бири.',
                'Иссык-Куль — одно из крупнейших высокогорных озёр мира.',
                'Issyk-Kul is one of the largest mountain lakes in the world.',
            ),
            'show_on_home': False,
            'answers': [
                (('Ысык-Көл', 'Иссык-Куль', 'Issyk-Kul'), True),
                (('Соң-Көл', 'Сон-Куль', 'Son-Kul'), False),
                (('Сары-Челек', 'Сары-Челек', 'Sary-Chelek'), False),
                (('Чатыр-Көл', 'Чатыр-Куль', 'Chatyr-Kul'), False),
            ],
        },
        {
            'text': (
                'Кыргызстанда канча облус бар?',
                'Сколько областей в Кыргызстане?',
                'How many regions (oblasts) does Kyrgyzstan have?',
            ),
            'explanation': (
                'Жети облус, ошондой эле өзгөчө статусу бар эки шаар — Бишкек жана Ош.',
                'Семь областей, а ещё два города с особым статусом — Бишкек и Ош.',
                'Seven regions, plus two cities with special status: Bishkek and Osh.',
            ),
            'show_on_home': False,
            'answers': [
                (('7', '7', '7'), True),
                (('5', '5', '5'), False),
                (('9', '9', '9'), False),
                (('12', '12', '12'), False),
            ],
        },
        {
            'text': (
                'Кыргызстандын борбор шаары кайсы?',
                'Какой город — столица Кыргызстана?',
                'What is the capital of Kyrgyzstan?',
            ),
            'explanation': (
                'Бишкек — өлкөнүн борбору жана эң чоң шаары.',
                'Бишкек — столица и самый большой город страны.',
                'Bishkek is the capital and the largest city of the country.',
            ),
            'show_on_home': False,
            'answers': [
                (('Бишкек', 'Бишкек', 'Bishkek'), True),
                (('Ош', 'Ош', 'Osh'), False),
                (('Каракол', 'Каракол', 'Karakol'), False),
                (('Нарын', 'Нарын', 'Naryn'), False),
            ],
        },
    ],
}


class Command(BaseCommand):
    help = 'Начальное наполнение: области, достопримечательности, категории, демо-викторина.'

    @transaction.atomic
    def handle(self, *args, **options):
        with translation.override('ru'):
            regions = self.seed_regions()
            self.seed_places(regions)
            self.seed_categories()
            self.seed_quiz()
        self.stdout.write(self.style.SUCCESS('Готово.'))

    def seed_regions(self):
        regions = {}
        for order, (slug, kind, names, capital) in enumerate(REGIONS, start=1):
            region, created = Region.objects.get_or_create(
                slug=slug,
                defaults={'kind': kind, 'map_id': slug, 'order': order, **tr('title', *names), **tr('capital', *capital)},
            )
            regions[slug] = region
            self.report('Область/город', region, created)
        return regions

    def seed_places(self, regions):
        for order, (slug, region, kind, names, lat, lon, value, label) in enumerate(PLACES, start=1):
            place, created = Place.objects.get_or_create(
                slug=slug,
                defaults={
                    'region': regions[region], 'kind': kind, 'order': order,
                    'latitude': Decimal(lat), 'longitude': Decimal(lon),
                    **tr('title', *names), **tr('key_value', *value), **tr('key_label', *label),
                },
            )
            self.report('Достопримечательность', place, created)

    def seed_categories(self):
        for section_key, categories in CATEGORIES.items():
            section = Section.objects.get(key=section_key)
            for order, (slug, names) in enumerate(categories, start=1):
                category, created = Category.objects.get_or_create(
                    section=section, slug=slug, defaults={'order': order, **tr('title', *names)},
                )
                self.report('Категория', category, created)

    def seed_quiz(self):
        quiz, created = Quiz.objects.get_or_create(
            slug=QUIZ['slug'],
            defaults={'topic': Topic.GEOGRAPHY, **tr('title', *QUIZ['title']), **tr('summary', *QUIZ['summary'])},
        )
        self.report('Викторина', quiz, created)
        if not created:
            return
        for q_order, data in enumerate(QUIZ['questions'], start=1):
            question = Question.objects.create(
                quiz=quiz, order=q_order, show_on_home=data['show_on_home'],
                **tr('text', *data['text']), **tr('explanation', *data['explanation']),
            )
            for a_order, (texts, is_correct) in enumerate(data['answers'], start=1):
                Answer.objects.create(question=question, order=a_order, is_correct=is_correct, **tr('text', *texts))

    def report(self, label, obj, created):
        status = 'создано' if created else 'уже есть'
        self.stdout.write(f'  {label}: {obj} — {status}')
