from django.http import Http404
from django.shortcuts import get_object_or_404, render

from apps.base.models import Section
from apps.learn.models import Game, Quiz

from .models import Article, Category


def section_index(request, section_key):
    section = get_object_or_404(Section, key=section_key)
    categories = section.categories.published()
    return render(request, 'articles/section_index.html', {
        'section': section,
        'categories': categories,
        'articles': Article.objects.published()
            .filter(category__section=section).select_related('category__section')[:9],
        'games': Game.objects.published().filter(section=section),
        'quizzes': Quiz.objects.published().filter(section=section)[:3],
    })


def category_detail(request, section_key, category):
    category = get_object_or_404(
        Category.objects.published().select_related('section'), section__key=section_key, slug=category
    )
    return render(request, 'articles/category.html', {
        'section': category.section,
        'category': category,
        'categories': category.section.categories.published(),
        'articles': category.articles.published().select_related('category__section'),
    })


def article_detail(request, section_key, category, slug):
    article = get_object_or_404(
        Article.objects.published().select_related('category__section'), slug=slug
    )
    if article.category.section.key != section_key or article.category.slug != category:
        raise Http404
    related = article.related.published().select_related('category__section')
    if not related:
        related = article.category.articles.published().exclude(pk=article.pk).select_related('category__section')
    return render(request, 'articles/article_detail.html', {
        'section': article.category.section,
        'article': article,
        'gallery': article.gallery.all(),
        'facts': article.facts.all(),
        'related': related[:3],
    })
