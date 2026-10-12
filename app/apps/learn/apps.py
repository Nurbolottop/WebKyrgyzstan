from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.learn'
    verbose_name = _('Learn and play')
