from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.choices import Difficulty
from apps.base.models import ContentModel, PublishableModel, TimeStampedModel, upload_to
from apps.base.validators import AUDIO_VALIDATORS, IMAGE_VALIDATORS


class Topic(models.TextChoices):
    GEOGRAPHY = 'geography', _('Geography')
    HISTORY = 'history', _('History')
    CULTURE = 'culture', _('Culture')
    NATURE = 'nature', _('Nature and animals')
    LANGUAGE = 'language', _('Kyrgyz language')


# ---------------------------------------------------------------------------
# Викторины
# ---------------------------------------------------------------------------
class Quiz(ContentModel):
    topic = models.CharField('тема', max_length=20, choices=Topic.choices)
    difficulty = models.CharField(
        'сложность', max_length=10, choices=Difficulty.choices, default=Difficulty.EASY
    )
    section = models.ForeignKey(
        'base.Section', verbose_name='показывать также в разделе', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='quizzes',
        help_text='Все викторины есть в «Учись и играй»; здесь можно добавить ещё один раздел.',
    )
    shuffle_answers = models.BooleanField('перемешивать варианты ответов', default=True)

    class Meta(ContentModel.Meta):
        verbose_name = 'викторина'
        verbose_name_plural = 'викторины'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name='викторина', on_delete=models.CASCADE, related_name='questions')
    order = models.PositiveIntegerField('порядок', default=0)
    text = models.TextField('вопрос')
    image = models.ImageField('картинка', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS)
    image_alt = models.CharField('описание картинки', max_length=200, blank=True)
    explanation = models.TextField('пояснение после ответа', blank=True)
    show_on_home = models.BooleanField(
        'показывать на главной', default=False,
        help_text='Вопрос может попасть в блок мини-викторины на главной странице.',
    )

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.text[:80]


class Answer(models.Model):
    question = models.ForeignKey(
        Question, verbose_name='вопрос', on_delete=models.CASCADE, related_name='answers'
    )
    order = models.PositiveIntegerField('порядок', default=0)
    text = models.CharField('вариант ответа', max_length=300)
    is_correct = models.BooleanField('правильный', default=False)

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответа'

    def __str__(self):
        return self.text


# ---------------------------------------------------------------------------
# Загадки и ребусы
# ---------------------------------------------------------------------------
class Puzzle(TimeStampedModel, PublishableModel):
    class Kind(models.TextChoices):
        RIDDLE = 'riddle', _('Riddle')
        REBUS = 'rebus', _('Rebus')

    kind = models.CharField('тип', max_length=10, choices=Kind.choices)
    topic = models.CharField('тема', max_length=20, choices=Topic.choices, blank=True)
    prompt = models.TextField('задание', help_text='Текст загадки или подсказка к ребусу.')
    image = models.ImageField(
        'картинка', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS,
        help_text='Для ребуса обязательна.',
    )
    image_alt = models.CharField('описание картинки', max_length=200, blank=True)
    answer = models.CharField('ответ', max_length=100)
    alt_answers = models.TextField(
        'другие правильные варианты', blank=True, help_text='Каждый вариант с новой строки.'
    )
    options = models.TextField(
        'варианты для выбора', blank=True,
        help_text='Каждый с новой строки. Если пусто — ответ вводится с клавиатуры.',
    )
    hint = models.CharField('подсказка', max_length=300, blank=True)
    explanation = models.TextField('пояснение', blank=True)

    class Meta(PublishableModel.Meta):
        verbose_name = 'загадка или ребус'
        verbose_name_plural = 'загадки и ребусы'

    def __str__(self):
        return self.prompt[:80]

    def clean(self):
        if self.kind == self.Kind.REBUS and not self.image:
            raise ValidationError({'image': 'У ребуса должна быть картинка.'})


# ---------------------------------------------------------------------------
# Кыргызский язык
# ---------------------------------------------------------------------------
class WordTopic(ContentModel):
    class Meta(ContentModel.Meta):
        verbose_name = 'тема слов'
        verbose_name_plural = 'кыргызский язык: темы'


class Word(models.Model):
    topic = models.ForeignKey(WordTopic, verbose_name='тема', on_delete=models.CASCADE, related_name='words')
    order = models.PositiveIntegerField('порядок', default=0)
    kyrgyz = models.CharField('слово на кыргызском', max_length=100)
    transliteration = models.CharField(
        'произношение латиницей', max_length=100, blank=True, help_text='Например «salam».'
    )
    translation = models.CharField('перевод', max_length=100)
    image = models.ImageField('картинка', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS)
    image_alt = models.CharField('описание картинки', max_length=200, blank=True)
    audio = models.FileField('произношение (аудио)', upload_to=upload_to, blank=True, validators=AUDIO_VALIDATORS)

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'слово'
        verbose_name_plural = 'слова'

    def __str__(self):
        return self.kyrgyz


# ---------------------------------------------------------------------------
# Мини-игры
# ---------------------------------------------------------------------------
class Game(ContentModel):
    class Engine(models.TextChoices):
        CHOICE = 'choice', 'Выбери правильный ответ'
        MATCH = 'match', 'Соедини пары'
        MEMORY = 'memory', 'Найди пару (память)'
        MAP_GUESS = 'map_guess', 'Угадай область на карте'
        ASSEMBLY = 'assembly', 'Пошаговая сборка (юрта)'

    class Source(models.TextChoices):
        ITEMS = 'items', 'Элементы игры (ниже)'
        WORDS = 'words', 'Слова выбранной темы'
        REGIONS = 'regions', 'Области и города'
        PLACES = 'places', 'Достопримечательности'

    # Какие источники данных умеет использовать каждая механика
    ENGINE_SOURCES = {
        Engine.CHOICE: {Source.ITEMS, Source.PLACES, Source.WORDS},
        Engine.MATCH: {Source.ITEMS, Source.WORDS},
        Engine.MEMORY: {Source.ITEMS, Source.WORDS},
        Engine.MAP_GUESS: {Source.REGIONS},
        Engine.ASSEMBLY: {Source.ITEMS},
    }

    engine = models.CharField('механика', max_length=20, choices=Engine.choices)
    source = models.CharField('откуда брать данные', max_length=20, choices=Source.choices, default=Source.ITEMS)
    word_topic = models.ForeignKey(
        WordTopic, verbose_name='тема слов', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='games',
    )
    section = models.ForeignKey(
        'base.Section', verbose_name='раздел', on_delete=models.PROTECT, related_name='games',
        help_text='Где находится игра. Сборка юрты — «Культура и традиции».',
    )
    difficulty = models.CharField(
        'сложность', max_length=10, choices=Difficulty.choices, default=Difficulty.EASY
    )
    instructions = models.TextField('правила', blank=True)
    success_text = models.CharField('текст при победе', max_length=200, blank=True)

    class Meta(ContentModel.Meta):
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def clean(self):
        allowed = self.ENGINE_SOURCES.get(self.engine, set())
        if self.engine and self.source not in allowed:
            names = ', '.join(f'«{self.Source(s).label}»' for s in sorted(allowed))
            raise ValidationError({'source': f'Эта механика работает только с: {names}.'})
        if self.source == self.Source.WORDS and not self.word_topic_id:
            raise ValidationError({'word_topic': 'Выберите тему слов.'})


class GameItem(models.Model):
    game = models.ForeignKey(Game, verbose_name='игра', on_delete=models.CASCADE, related_name='items')
    order = models.PositiveIntegerField('порядок / шаг', default=0)
    title = models.CharField('название', max_length=200)
    text = models.TextField('описание', blank=True)
    image = models.ImageField('картинка', upload_to=upload_to, blank=True, validators=IMAGE_VALIDATORS)
    image_alt = models.CharField('описание картинки', max_length=200, blank=True)
    pair_text = models.CharField(
        'пара', max_length=200, blank=True, help_text='Для «Соедини пары»: что соединяется с этим элементом.'
    )
    svg_layer = models.SlugField(
        'слой SVG', max_length=50, blank=True,
        help_text='Для сборки юрты: id слоя в сцене (kerege, uuk, tunduk…).',
    )
    is_distractor = models.BooleanField(
        'лишний элемент', default=False, help_text='Неправильный вариант, который нужно не выбрать.'
    )
    explanation = models.TextField('пояснение', blank=True)

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'элемент игры'
        verbose_name_plural = 'элементы игры'

    def __str__(self):
        return self.title
