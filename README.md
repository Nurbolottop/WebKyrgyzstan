# Web Kyrgyzstan

Интерактивный образовательный сайт о Кыргызстане для детей и подростков: интерактивная карта, культура и традиции, викторины и игры, рецепты и мастер-классы, современный Кыргызстан. Три языка — кыргызский, русский, английский.

Production: https://webkg.zeastudio.su

**Стек:** Python 3.12 · Django 5.2 LTS · PostgreSQL 17 · Django Templates · HTML/CSS/Vanilla JS · Gunicorn · Docker Compose · Nginx (на хосте)

---

## Разделы сайта

| Раздел | URL | Приложение |
|---|---|---|
| Главная | `/<lang>/` | `base` |
| Открой Кыргызстан | `/<lang>/discover/` | `discover` + `articles` |
| Культура и традиции | `/<lang>/culture/` | `articles` + `learn` (сборка юрты) |
| Учись и играй | `/<lang>/learn/` | `learn` |
| Попробуй сам | `/<lang>/try/` | `practice` |
| Современный Кыргызстан | `/<lang>/modern/` | `articles` |

`<lang>` — `ky`, `ru` или `en`. Корень `/` перенаправляет на язык браузера, по умолчанию — на кыргызский.

## Структура

```
.
├── app/                    # Django-проект
│   ├── core/               # настройки (base/dev/prod/test), urls, wsgi, storage
│   ├── apps/
│   │   ├── base/           # ядро: главная, настройки сайта, разделы, SEO, общие модели
│   │   ├── articles/       # категории и статьи всех разделов
│   │   ├── discover/       # области, города, достопримечательности, карта
│   │   ├── learn/          # викторины, загадки и ребусы, кыргызский язык, игры
│   │   └── practice/       # рецепты, мастер-классы, творческие задания
│   ├── templates/          # base.html, layouts, partials, components, страницы
│   ├── static/             # css, js (ES-модули), img, icons, fonts
│   └── locale/             # переводы интерфейса (ky, ru, en)
├── docker/                 # Dockerfile, entrypoint.sh, gunicorn.conf.py
├── docker-compose.yml      # локальная разработка
├── docker-compose.prod.yml # production
├── requirements.txt
└── .env.example            # шаблон переменных окружения
```

## Локальный запуск

```bash
cp .env.example .env          # заполнить SECRET_KEY и POSTGRES_PASSWORD
docker compose up --build
docker compose exec web python manage.py createsuperuser
```

Сайт: http://127.0.0.1:8098 · админка: http://127.0.0.1:8098/admin/ (адрес задаётся `ADMIN_URL`).

Код смонтирован в контейнер, `runserver` перезапускается при изменениях.

### Наполнение

```bash
docker compose exec web python manage.py seed_content     # области, города, достопримечательности, категории, викторина
docker compose exec web python manage.py fetch_photos     # обложки со свободной лицензией из Wikimedia Commons
docker compose exec web python manage.py compilemessages  # переводы интерфейса
```

Обе команды наполнения можно запускать повторно: они не дублируют записи и не перезаписывают то, что уже изменено в админке.

### Частые команды

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec -e DJANGO_SETTINGS_MODULE=core.settings.test web python manage.py test
docker compose exec web python manage.py makemessages -l ky -l ru -l en
docker compose exec web python manage.py compilemessages
```

## Переменные окружения

Все настройки, которые отличаются между окружениями, и все секреты — в `.env` (в Git не попадает). Описание каждой переменной — в [.env.example](.env.example).

| Переменная | Назначение |
|---|---|
| `COMPOSE_PROJECT_NAME` | Префикс контейнеров и volume; уникален на машине |
| `WEB_PORT`, `DB_PORT` | Порты на `127.0.0.1` хоста |
| `SECRET_KEY` | Ключ Django |
| `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` | Домены сайта |
| `ADMIN_URL` | Адрес админки (в production — нестандартный) |
| `POSTGRES_*` | Доступ к базе |
| `GUNICORN_WORKERS` | Число воркеров в production |

## Карта

SVG-карта генерируется скриптом из открытых границ (geoBoundaries / OpenStreetMap, ODbL):

```bash
python3 tools/build_map.py tools/geo app/templates/svg/map_kyrgyzstan.html app/apps/discover/map_projection.py app/static/img/sections/discover.svg
```

## Многоязычность

- Интерфейс — Django i18n, файлы `app/locale/<lang>/LC_MESSAGES/django.po`.
- Контент — `django-modeltranslation`: у переводимых полей есть колонки `_ky`, `_ru`, `_en`, в админке они разложены по вкладкам. Русская версия обязательна, при отсутствии перевода показывается русский текст.

## Production

Контейнеры `db` и `web` (Gunicorn) поднимаются через `docker-compose.prod.yml`; Nginx на хосте проксирует запросы на `127.0.0.1:${WEB_PORT}`, сам отдаёт `volumes/static` и `volumes/media` и терминирует HTTPS.

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

При старте контейнер применяет миграции, компилирует переводы и собирает статику (имена файлов с хешем — кешируются Nginx надолго).

Конфигурация Nginx, бэкапы и порядок деплоя будут добавлены на этапе публикации.


