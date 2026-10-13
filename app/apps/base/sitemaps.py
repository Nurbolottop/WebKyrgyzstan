from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.articles.models import Article, Category
from apps.discover.models import Place, Region
from apps.learn.models import Game, Quiz, WordTopic
from apps.practice.models import Activity

from .models import Section


class I18nSitemap(Sitemap):
    i18n = True
    alternates = True
    x_default = True


class StaticSitemap(I18nSitemap):
    priority = 1.0

    def items(self):
        return ['base:home', 'discover:places', 'learn:quizzes', 'learn:riddles', 'learn:rebuses',
                'learn:word_topics', 'learn:games', 'practice:recipes', 'practice:masterclasses', 'practice:tasks']

    def location(self, item):
        return reverse(item)


class SectionSitemap(I18nSitemap):
    priority = 0.9

    def items(self):
        return Section.objects.all()


def model_sitemap(queryset_func, priority=0.7):
    class _Sitemap(I18nSitemap):
        def items(self):
            return queryset_func()

        def lastmod(self, obj):
            return getattr(obj, 'updated_at', None)

    _Sitemap.priority = priority
    return _Sitemap


sitemaps = {
    'static': StaticSitemap,
    'sections': SectionSitemap,
    'categories': model_sitemap(lambda: Category.objects.published().select_related('section'), 0.6),
    'articles': model_sitemap(lambda: Article.objects.published().select_related('category__section')),
    'regions': model_sitemap(lambda: Region.objects.published(), 0.8),
    'places': model_sitemap(lambda: Place.objects.published(), 0.8),
    'quizzes': model_sitemap(lambda: Quiz.objects.published()),
    'words': model_sitemap(lambda: WordTopic.objects.published()),
    'games': model_sitemap(lambda: Game.objects.published().select_related('section')),
    'activities': model_sitemap(lambda: Activity.objects.published()),
}
