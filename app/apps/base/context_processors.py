from django.conf import settings
from django.urls import translate_url
from django.utils import translation

from .models import Section, SiteSettings

def site(request):
    if request.path.startswith(f'/{settings.ADMIN_URL}'):
        return {}

    current = translation.get_language()
    language_links = [
        {
            'code': code,
            'name': name,
            'url': translate_url(request.path, code),
            'current': code == current,
        }
        for code, name in settings.LANGUAGES
    ]
    return {
        'site': SiteSettings.load(),
        'nav_sections': Section.objects.all(),
        'language_links': language_links,
    }
