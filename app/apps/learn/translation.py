from modeltranslation.translator import TranslationOptions, register

from apps.base.translation import CONTENT_FIELDS

from .models import Answer, Game, GameItem, Puzzle, Question, Quiz, Word, WordTopic


@register(Quiz)
class QuizTranslation(TranslationOptions):
    fields = CONTENT_FIELDS


@register(Question)
class QuestionTranslation(TranslationOptions):
    fields = ('text', 'image_alt', 'explanation')


@register(Answer)
class AnswerTranslation(TranslationOptions):
    fields = ('text',)


@register(Puzzle)
class PuzzleTranslation(TranslationOptions):
    fields = ('prompt', 'image_alt', 'answer', 'alt_answers', 'options', 'hint', 'explanation')


@register(WordTopic)
class WordTopicTranslation(TranslationOptions):
    fields = CONTENT_FIELDS


@register(Word)
class WordTranslation(TranslationOptions):
    # Само слово (kyrgyz) не переводится — его и изучают
    fields = ('translation', 'image_alt')


@register(Game)
class GameTranslation(TranslationOptions):
    fields = CONTENT_FIELDS + ('instructions', 'success_text')


@register(GameItem)
class GameItemTranslation(TranslationOptions):
    fields = ('title', 'text', 'image_alt', 'pair_text', 'explanation')
