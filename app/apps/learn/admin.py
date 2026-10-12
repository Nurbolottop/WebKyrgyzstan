from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline, TranslationTabularInline

from apps.base.admin.mixins import ContentAdmin, publish, thumbnail, unpublish

from .forms import AnswerInlineFormSet
from .models import Answer, Game, GameItem, Puzzle, Question, Quiz, Word, WordTopic


# ---------------------------------------------------------------------------
# Викторины
# ---------------------------------------------------------------------------
class QuestionInline(TranslationTabularInline):
    model = Question
    fields = ('order', 'text', 'show_on_home')
    extra = 0
    show_change_link = True


@admin.register(Quiz)
class QuizAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'topic', 'difficulty', 'question_count', 'is_published', 'order')
    list_filter = ('topic', 'difficulty', 'is_published')
    inlines = (QuestionInline,)
    extra_fieldsets = (
        ('Параметры', {'fields': ('topic', 'difficulty', 'section', 'shuffle_answers')}),
    )

    @admin.display(description='Вопросов')
    def question_count(self, obj):
        return obj.questions.count()


class AnswerInline(TranslationTabularInline):
    model = Answer
    formset = AnswerInlineFormSet
    fields = ('order', 'text', 'is_correct')
    extra = 4


@admin.register(Question)
class QuestionAdmin(TabbedTranslationAdmin):
    list_display = ('text', 'quiz', 'order', 'show_on_home')
    list_filter = ('quiz', 'show_on_home')
    list_select_related = ('quiz',)
    search_fields = ('text_ru', 'text_ky', 'text_en')
    autocomplete_fields = ('quiz',)
    fields = ('quiz', 'order', 'text', 'image', 'image_alt', 'explanation', 'show_on_home')
    inlines = (AnswerInline,)


# ---------------------------------------------------------------------------
# Загадки и ребусы
# ---------------------------------------------------------------------------
@admin.register(Puzzle)
class PuzzleAdmin(TabbedTranslationAdmin):
    list_display = ('image_preview', '__str__', 'kind', 'topic', 'is_published', 'order')
    list_display_links = ('image_preview', '__str__')
    list_editable = ('is_published', 'order')
    list_filter = ('kind', 'topic', 'is_published')
    search_fields = ('prompt_ru', 'answer_ru')
    actions = (publish, unpublish)
    fieldsets = (
        (None, {'fields': ('kind', 'topic', 'prompt', 'image', 'image_alt')}),
        ('Ответ', {'fields': ('answer', 'alt_answers', 'options', 'hint', 'explanation')}),
        ('Публикация', {'fields': ('is_published', 'order')}),
    )

    @admin.display(description='Картинка')
    def image_preview(self, obj):
        return thumbnail(obj.image)


# ---------------------------------------------------------------------------
# Кыргызский язык
# ---------------------------------------------------------------------------
class WordInline(TranslationStackedInline):
    model = Word
    fields = (('kyrgyz', 'transliteration', 'order'), 'translation', ('image', 'image_alt'), 'audio')
    extra = 0


@admin.register(WordTopic)
class WordTopicAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'word_count', 'is_published', 'order')
    inlines = (WordInline,)

    @admin.display(description='Слов')
    def word_count(self, obj):
        return obj.words.count()


# ---------------------------------------------------------------------------
# Мини-игры
# ---------------------------------------------------------------------------
class GameItemInline(TranslationStackedInline):
    model = GameItem
    fields = (
        ('title', 'order'), 'text', ('image', 'image_alt'),
        'pair_text', ('svg_layer', 'is_distractor'), 'explanation',
    )
    extra = 0


@admin.register(Game)
class GameAdmin(ContentAdmin):
    list_display = ('cover_preview', 'title', 'engine', 'source', 'section', 'is_published', 'order')
    list_filter = ('engine', 'section', 'is_published')
    autocomplete_fields = ('word_topic',)
    inlines = (GameItemInline,)
    extra_fieldsets = (
        ('Механика', {
            'fields': ('engine', 'source', 'word_topic', 'section', 'difficulty'),
            'description': 'Элементы ниже нужны, если данные берутся из «Элементов игры».',
        }),
        ('Тексты игры', {'fields': ('instructions', 'success_text')}),
    )
