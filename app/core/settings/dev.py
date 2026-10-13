from core.settings.base import *  # noqa: F401,F403

DEBUG = True

ALLOWED_HOSTS = ALLOWED_HOSTS or ['localhost', '127.0.0.1']  # noqa: F405

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Позволяет смотреть страницы во фрейме того же сайта (проверка мобильной вёрстки)
X_FRAME_OPTIONS = 'SAMEORIGIN'
