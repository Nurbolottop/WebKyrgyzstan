from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.utils import translation

from apps.articles.models import Category
from apps.base.models import HomeFeatured, Section, SiteSettings
from apps.discover.models import Region
from apps.learn.models import Quiz


class SectionTests(TestCase):
    def test_five_sections_created_by_migration(self):
        self.assertEqual(
            list(Section.objects.values_list('key', flat=True)),
            ['discover', 'culture', 'learn', 'practice', 'modern'],
        )

    def test_section_titles_translated(self):
        section = Section.objects.get(key='learn')
        with translation.override('ky'):
            self.assertEqual(section.title, 'Үйрөн жана ойно')
        with translation.override('en'):
            self.assertEqual(section.title, 'Learn and Play')


class SiteSettingsTests(TestCase):
    def test_singleton(self):
        SiteSettings(site_name='Другая запись').save()
        self.assertEqual(SiteSettings.objects.count(), 1)
        self.assertEqual(SiteSettings.load().site_name, 'Другая запись')


class TranslationFallbackTests(TestCase):
    def test_missing_translation_falls_back_to_russian(self):
        category = Category.objects.create(
            section=Section.objects.get(key='culture'), slug='test', title_ru='Юрта'
        )
        for lang in ('ky', 'en'):
            with translation.override(lang):
                self.assertEqual(category.title, 'Юрта')


class HomeFeaturedTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.region = Region.objects.create(slug='talas', map_id='talas', title_ru='Таласская область')
        cls.quiz = Quiz.objects.create(slug='q', title_ru='Викторина', topic='geography')

    def test_target_returns_selected_material(self):
        item = HomeFeatured.objects.create(region=self.region)
        self.assertEqual(item.target, self.region)

    def test_two_targets_rejected_by_database(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            HomeFeatured.objects.create(region=self.region, quiz=self.quiz)

    def test_no_target_rejected_by_database(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            HomeFeatured.objects.create()

    def test_clean_explains_problem(self):
        with self.assertRaisesMessage(ValidationError, 'ровно один'):
            HomeFeatured(region=self.region, quiz=self.quiz).clean()
