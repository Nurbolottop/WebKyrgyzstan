from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.articles.models import Category
from apps.base.models import Section


class CategoryTests(TestCase):
    def test_reserved_slug_rejected(self):
        category = Category(section=Section.objects.get(key='discover'), slug='regions', title_ru='Области')
        with self.assertRaises(ValidationError):
            category.full_clean()
