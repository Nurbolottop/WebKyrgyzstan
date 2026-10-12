from django.conf import settings
from django.test import TestCase


class LanguageRoutingTests(TestCase):
    def test_root_redirects_to_kyrgyz_by_default(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/ky/', fetch_redirect_response=False)

    def test_root_redirects_to_browser_language(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='ru-RU,ru;q=0.9')
        self.assertRedirects(response, '/ru/', fetch_redirect_response=False)

    def test_unsupported_browser_language_falls_back_to_kyrgyz(self):
        response = self.client.get('/', HTTP_ACCEPT_LANGUAGE='de-DE,de;q=0.9')
        self.assertRedirects(response, '/ky/', fetch_redirect_response=False)

    def test_home_renders_in_every_language(self):
        for code, _name in settings.LANGUAGES:
            with self.subTest(language=code):
                response = self.client.get(f'/{code}/')
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f'<html lang="{code}"')


class AdminTests(TestCase):
    def test_admin_login_available_at_configured_url(self):
        response = self.client.get(f'/{settings.ADMIN_URL}login/')
        self.assertEqual(response.status_code, 200)
