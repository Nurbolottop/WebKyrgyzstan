import os

from core.settings.base import *  # noqa: F401,F403

DEBUG = False

# Файловый кеш общий для всех воркеров Gunicorn и не требует отдельного сервиса
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.getenv('CACHE_DIR', '/tmp/webkg-cache'),
        'KEY_PREFIX': 'webkg',
        'TIMEOUT': 600,
    }
}

# Cookies только по HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Приложение работает за nginx, который терминирует HTTPS.
# Без этого Django считает запрос http-запросом и ломает CSRF/редиректы.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

# Редирект http → https делает nginx, поэтому SECURE_SSL_REDIRECT не нужен
SILENCED_SYSTEM_CHECKS = ['security.W008']

# Прочие security-заголовки
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
X_FRAME_OPTIONS = 'DENY'

# HSTS включай только когда HTTPS точно настроен и работает,
# иначе браузеры запомнят домен и http перестанет открываться.
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# =============================================================================
# LOGGING — при DEBUG=False ошибки иначе уходят в никуда
# =============================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name}: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
