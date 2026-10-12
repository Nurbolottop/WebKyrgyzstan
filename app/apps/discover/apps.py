from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DiscoverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.discover'
    verbose_name = _('Discover Kyrgyzstan')
