from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse


class AdminPagesTests(TestCase):
    """Каждая страница списка и формы добавления в админке открывается без ошибок."""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_superuser('admin', 'admin@example.com', 'pass')
        call_command('seed_content', stdout=open('/dev/null', 'w'))

    def setUp(self):
        self.client.force_login(self.user)

    def test_changelists_and_forms_render(self):
        for model, model_admin in admin.site._registry.items():
            info = (model._meta.app_label, model._meta.model_name)
            with self.subTest(model=model.__name__):
                response = self.client.get(reverse('admin:%s_%s_changelist' % info))
                self.assertEqual(response.status_code, 200)

                obj = model._default_manager.first()
                if obj is not None:
                    response = self.client.get(reverse('admin:%s_%s_change' % info, args=[obj.pk]))
                    self.assertEqual(response.status_code, 200)

                if model_admin.has_add_permission(self._request()):
                    response = self.client.get(reverse('admin:%s_%s_add' % info))
                    self.assertEqual(response.status_code, 200)

    def _request(self):
        request = self.client.request().wsgi_request
        request.user = self.user
        return request


class AdminLanguageTests(TestCase):
    def test_admin_is_russian_for_any_browser_language(self):
        for accept in ('ky', 'en-US', ''):
            with self.subTest(accept=accept):
                response = self.client.get(reverse('admin:login'), HTTP_ACCEPT_LANGUAGE=accept)
                self.assertContains(response, 'Имя пользователя')

    def test_site_language_not_affected(self):
        response = self.client.get('/en/')
        self.assertContains(response, '<html lang="en"')
