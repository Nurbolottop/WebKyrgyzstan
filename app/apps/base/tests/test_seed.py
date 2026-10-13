from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from apps.articles.models import Category
from apps.discover.models import Place, Region
from apps.learn.models import Question, Quiz


class SeedContentTests(TestCase):
    def test_seed_is_idempotent(self):
        call_command('seed_content', stdout=StringIO())
        call_command('seed_content', stdout=StringIO())

        self.assertEqual(Region.objects.filter(kind='oblast').count(), 7)
        self.assertEqual(Region.objects.filter(kind='city').count(), 2)
        self.assertEqual(Place.objects.count(), 8)
        self.assertEqual(Category.objects.count(), 12)
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(Question.objects.count(), 4)

    def test_every_question_has_exactly_one_correct_answer(self):
        call_command('seed_content', stdout=StringIO())
        for question in Question.objects.all():
            self.assertEqual(question.answers.filter(is_correct=True).count(), 1)


class SeedStarterTests(TestCase):
    def test_starter_is_idempotent_and_pages_render(self):
        from apps.articles.models import Article
        from apps.base.models import HomeFeatured
        from apps.learn.models import Game
        from apps.practice.models import Activity

        call_command('seed_content', stdout=StringIO())
        call_command('seed_starter', stdout=StringIO())
        call_command('seed_starter', stdout=StringIO())
        self.assertEqual(Article.objects.count(), 10)
        self.assertEqual(Activity.objects.count(), 3)
        self.assertEqual(Game.objects.count(), 4)
        self.assertEqual(HomeFeatured.objects.count(), 6)
        for question in Question.objects.all():
            self.assertEqual(question.answers.filter(is_correct=True).count(), 1)

        urls = [obj.get_absolute_url() for model in (Article, Activity, Game) for obj in model.objects.all()]
        urls += ['/ru/', '/ky/learn/riddles/', '/en/learn/kyrgyz/nature/']
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)
