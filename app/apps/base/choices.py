from django.db import models
from django.utils.translation import gettext_lazy as _


class SectionKey(models.TextChoices):
    DISCOVER = 'discover', _('Discover Kyrgyzstan')
    CULTURE = 'culture', _('Culture and Traditions')
    LEARN = 'learn', _('Learn and Play')
    PRACTICE = 'practice', _('Try It Yourself')
    MODERN = 'modern', _('Modern Kyrgyzstan')


class Difficulty(models.TextChoices):
    EASY = 'easy', _('Easy')
    MEDIUM = 'medium', _('Medium')
    HARD = 'hard', _('Hard')
