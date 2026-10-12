FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# gettext — для compilemessages, netcat — ожидание базы в entrypoint
RUN apt-get update && apt-get install -y --no-install-recommends \
        gettext \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Приложение работает не от root. UID совпадает с владельцем каталогов
# static/media на хосте (по умолчанию 1000), чтобы контейнер мог в них писать.
ARG APP_UID=1000
RUN useradd --uid "${APP_UID}" --create-home --shell /usr/sbin/nologin app

COPY docker/entrypoint.sh /entrypoint.sh
COPY docker/gunicorn.conf.py /gunicorn.conf.py
RUN chmod +x /entrypoint.sh

COPY --chown=app:app app /app
RUN mkdir -p /app/staticfiles /app/media && chown app:app /app/staticfiles /app/media

USER app

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "--config", "/gunicorn.conf.py", "core.wsgi:application"]
