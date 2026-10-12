from core.settings.base import *  # noqa: F401,F403

# Тесты не требуют collectstatic
STORAGES = {
    **STORAGES,  # noqa: F405
    'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
}

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
