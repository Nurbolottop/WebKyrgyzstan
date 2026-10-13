from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from apps.articles.models import Article, Category
from apps.base.models import Section
from apps.discover.models import Place, Region
from apps.learn.models import Game, Puzzle, WordTopic, Word
from apps.practice.models import Recipe

LANGS = ('ky', 'ru', 'en')


class PublicPagesTests(TestCase):
    """Все публичные страницы открываются на трёх языках."""

    @classmethod
    def setUpTestData(cls):
        call_command('seed_content', stdout=StringIO())
        category = Category.objects.get(slug='yurt')
        cls.article = Article.objects.create(category=category, slug='yurt-structure', title_ru='Как устроена юрта')
        cls.recipe = Recipe.objects.create(slug='boorsok', title_ru='Боорсоки', safety_notes_ru='Со взрослыми')
        topic = WordTopic.objects.create(slug='family', title_ru='Семья')
        Word.objects.create(topic=topic, kyrgyz='апа', translation_ru='мама')
        Puzzle.objects.create(kind='riddle', prompt_ru='Загадка', answer_ru='юрта')
        Game.objects.create(slug='guess-region', title_ru='Угадай область', engine='map_guess', source='regions',
                            section=Section.objects.get(key='learn'))

    def urls(self):
        return [
            '', 'discover/', 'discover/regions/issyk-kul/', 'discover/regions/bishkek/', 'discover/places/',
            'discover/places/?kind=lake', 'discover/places/issyk-kul-lake/', 'culture/', 'culture/yurt/',
            'culture/yurt/yurt-structure/', 'modern/', 'modern/sport/', 'learn/', 'learn/quizzes/',
            'learn/quizzes/?topic=geography', 'learn/quizzes/kyrgyzstan-geography/', 'learn/riddles/',
            'learn/rebuses/', 'learn/kyrgyz/', 'learn/kyrgyz/family/', 'learn/play/', 'learn/play/guess-region/',
            'try/', 'try/recipes/', 'try/recipes/boorsok/', 'try/master-classes/', 'try/tasks/',
        ]

    def test_pages_render_in_all_languages(self):
        for lang in LANGS:
            for url in self.urls():
                with self.subTest(url=f'/{lang}/{url}'):
                    response = self.client.get(f'/{lang}/{url}')
                    self.assertEqual(response.status_code, 200)

    def test_unknown_filter_value_is_ignored(self):
        response = self.client.get('/ru/discover/places/?kind=<script>alert(1)</script>')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'alert(1)')
        self.assertEqual(response.context['current_kind'], '')

    def test_unpublished_material_returns_404(self):
        Place.objects.filter(slug='tash-rabat').update(is_published=False)
        self.assertEqual(self.client.get('/ru/discover/places/tash-rabat/').status_code, 404)

    def test_article_in_wrong_section_returns_404(self):
        self.assertEqual(self.client.get('/ru/modern/yurt/yurt-structure/').status_code, 404)

    def test_language_switcher_keeps_current_page(self):
        response = self.client.get('/ru/discover/places/issyk-kul-lake/')
        self.assertContains(response, 'href="/ky/discover/places/issyk-kul-lake/"')
        self.assertContains(response, 'href="/en/discover/places/issyk-kul-lake/"')

    def test_hreflang_alternates(self):
        response = self.client.get('/ky/discover/')
        for lang in LANGS:
            self.assertContains(response, f'hreflang="{lang}" href="http://testserver/{lang}/discover/"')

    def test_kyrgyz_interface_translated(self):
        response = self.client.get('/ky/')
        self.assertContains(response, 'Кыргызстанды ачып көр')
        self.assertContains(response, 'Эмнеден баштайбыз?')

    def test_map_has_all_regions_and_cities(self):
        response = self.client.get('/ru/discover/')
        for region in Region.objects.all():
            self.assertContains(response, f'data-region="{region.map_id}"')
        # Координаты без локализованной запятой
        self.assertNotRegex(response.content.decode(), r'cx="\d+,\d"')

    def test_sitemap_and_robots(self):
        sitemap = self.client.get('/sitemap.xml')
        self.assertEqual(sitemap.status_code, 200)
        self.assertContains(sitemap, '/ky/discover/places/issyk-kul-lake/')
        self.assertContains(sitemap, 'hreflang="en"')
        robots = self.client.get('/robots.txt')
        self.assertContains(robots, 'Sitemap: http://testserver/sitemap.xml')

    def test_404_page(self):
        response = self.client.get('/ru/no-such-page/')
        self.assertEqual(response.status_code, 404)
