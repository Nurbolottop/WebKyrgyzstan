from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.practice.models import Activity, MasterClass, Recipe


class ActivityProxyTests(TestCase):
    def test_proxy_sets_kind_and_filters(self):
        Recipe.objects.create(slug='boorsok', title_ru='Боорсоки', safety_notes_ru='Со взрослыми')
        MasterClass.objects.create(slug='kalpak', title_ru='Калпак')

        self.assertEqual(Activity.objects.get(slug='boorsok').kind, 'recipe')
        self.assertEqual(list(Recipe.objects.values_list('slug', flat=True)), ['boorsok'])
        self.assertEqual(list(MasterClass.objects.values_list('slug', flat=True)), ['kalpak'])

    def test_recipe_requires_safety_notes(self):
        recipe = Recipe(slug='kurut', title_ru='Курут')
        with self.assertRaises(ValidationError) as ctx:
            recipe.full_clean()
        self.assertIn('safety_notes', ctx.exception.message_dict)
