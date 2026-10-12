from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.test import TestCase

from apps.base.models import Section
from apps.learn.forms import AnswerInlineFormSet
from apps.learn.models import Answer, Game, Puzzle, Question, Quiz


class GameTests(TestCase):
    def setUp(self):
        self.section = Section.objects.get(key='learn')

    def test_map_guess_requires_regions_source(self):
        game = Game(engine='map_guess', source='items', section=self.section, slug='g', title_ru='Игра')
        with self.assertRaises(ValidationError):
            game.clean()

    def test_words_source_requires_topic(self):
        game = Game(engine='match', source='words', section=self.section, slug='g', title_ru='Игра')
        with self.assertRaises(ValidationError):
            game.clean()

    def test_compatible_engine_and_source(self):
        Game(engine='map_guess', source='regions', section=self.section, slug='g', title_ru='Игра').clean()


class PuzzleTests(TestCase):
    def test_rebus_requires_image(self):
        with self.assertRaises(ValidationError):
            Puzzle(kind='rebus', prompt_ru='?', answer_ru='юрта').clean()


class AnswerFormSetTests(TestCase):
    FormSet = inlineformset_factory(Question, Answer, formset=AnswerInlineFormSet, fields=('text', 'is_correct'), extra=0)

    def setUp(self):
        quiz = Quiz.objects.create(slug='q', title_ru='Викторина', topic='geography')
        self.question = Question.objects.create(quiz=quiz, text_ru='Вопрос?')

    def formset(self, answers):
        data = {
            'answers-TOTAL_FORMS': str(len(answers)),
            'answers-INITIAL_FORMS': '0',
        }
        for i, (text, correct) in enumerate(answers):
            data[f'answers-{i}-text'] = text
            if correct:
                data[f'answers-{i}-is_correct'] = 'on'
        return self.FormSet(data, instance=self.question, prefix='answers')

    def test_valid(self):
        self.assertTrue(self.formset([('Бишкек', True), ('Ош', False)]).is_valid())

    def test_requires_two_answers(self):
        self.assertFalse(self.formset([('Бишкек', True)]).is_valid())

    def test_requires_exactly_one_correct(self):
        self.assertFalse(self.formset([('Бишкек', True), ('Ош', True)]).is_valid())
        self.assertFalse(self.formset([('Бишкек', False), ('Ош', False)]).is_valid())
