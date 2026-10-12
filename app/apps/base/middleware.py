from django.conf import settings
from django.utils import translation


class AdminLocaleMiddleware:
    """Админка всегда на русском, независимо от языка браузера контент-менеджера."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.prefixes = (f'/{settings.ADMIN_URL}', '/ckeditor5/')

    def __call__(self, request):
        if request.path.startswith(self.prefixes):
            translation.activate('ru')
            request.LANGUAGE_CODE = 'ru'
        return self.get_response(request)
