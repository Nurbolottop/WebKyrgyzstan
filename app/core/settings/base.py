"""
Общие настройки Web Kyrgyzstan.

Все секреты и всё, что отличается между окружениями, читается из переменных
окружения (.env в корне репозитория, шаблон — .env.example).
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# =============================================================================
# PATHS (ПУТИ)
# =============================================================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # app/

# В Docker переменные приходят из env_file; локально — из .env в корне репозитория.
load_dotenv(BASE_DIR.parent / '.env')


def env_list(name, default=''):
    return [item.strip() for item in os.getenv(name, default).split(',') if item.strip()]


# =============================================================================
# SECURITY (БЕЗОПАСНОСТЬ)
# =============================================================================
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise Exception("SECRET_KEY не задан в переменных окружения")

DEBUG = False

ALLOWED_HOSTS = env_list('ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = env_list('CSRF_TRUSTED_ORIGINS')

# Адрес админки задаётся через окружение, чтобы не держать его стандартным /admin/
ADMIN_URL = os.getenv('ADMIN_URL', 'admin').strip('/') + '/'

# =============================================================================
# APPLICATIONS (ПРИЛОЖЕНИЯ)
# =============================================================================
INSTALLED_APPS = [
    # modeltranslation должен стоять до django.contrib.admin
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'django_ckeditor_5',

    # Local apps
    'apps.base',
    'apps.articles',
    'apps.discover',
    'apps.learn',
    'apps.practice',
]

# =============================================================================
# MIDDLEWARE (ПРОМЕЖУТОЧНЫЕ ОБРАБОТЧИКИ)
# =============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =============================================================================
# URLS & WSGI (МАРШРУТЫ И WSGI)
# =============================================================================
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

# =============================================================================
# TEMPLATES (ШАБЛОНЫ)
# =============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# =============================================================================
# DATABASE (БАЗА ДАННЫХ)
# =============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': int(os.getenv('POSTGRES_PORT', 5432)),
        'CONN_MAX_AGE': 60,
        'CONN_HEALTH_CHECKS': True,
    }
}

# =============================================================================
# CACHE (КЕШ)
# =============================================================================
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'KEY_PREFIX': 'webkg',
    }
}

# =============================================================================
# PASSWORD VALIDATION (ВАЛИДАЦИЯ ПАРОЛЕЙ)
# =============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =============================================================================
# INTERNATIONALIZATION (ИНТЕРНАЦИОНАЛИЗАЦИЯ)
# =============================================================================
# Корень сайта перенаправляет на язык браузера; если он не из списка — на кыргызский.
LANGUAGE_CODE = 'ky'
LANGUAGES = [
    ('ky', 'Кыргызча'),
    ('ru', 'Русский'),
    ('en', 'English'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

TIME_ZONE = os.getenv('TIME_ZONE', 'Asia/Bishkek')
USE_I18N = True
USE_TZ = True

# Переводы контента в БД: обязательна русская версия, ky/en — по мере готовности.
# Если перевода нет, показывается русский, затем кыргызский, затем английский.
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ky', 'ru', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('ru', 'ky', 'en')}
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'ru'

# =============================================================================
# STATIC & MEDIA FILES (СТАТИЧЕСКИЕ И МЕДИА ФАЙЛЫ)
# =============================================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'core.storage.StaticStorage',
    },
}

FILE_UPLOAD_PERMISSIONS = 0o644

# =============================================================================
# DEFAULTS (ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ)
# =============================================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# CKEDITOR 5 (РЕДАКТОР ТЕКСТА В АДМИНКЕ)
# =============================================================================
# Набор кнопок намеренно короткий: оформление задаёт дизайн-система сайта,
# а не редактор. H1 недоступен — это заголовок страницы.
CKEDITOR_5_FILE_UPLOAD_PERMISSION = 'staff'
CKEDITOR_5_CONFIGS = {
    'default': {
        'language': 'ru',
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'link', '|',
                'bulletedList', 'numberedList', 'blockQuote', '|',
                'imageUpload', '|',
                'undo', 'redo',
            ],
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
            ],
        },
        'image': {
            'toolbar': ['imageTextAlternative'],
        },
    },
}
