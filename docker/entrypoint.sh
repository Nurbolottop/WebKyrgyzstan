#!/bin/sh
set -e

echo "Ожидание базы данных ${POSTGRES_HOST}:${POSTGRES_PORT}..."
until nc -z -w 2 "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

# makemigrations здесь намеренно нет: миграции создаются разработчиком
# и хранятся в репозитории.
python manage.py migrate --noinput

if [ "${DJANGO_COMPILEMESSAGES:-0}" = "1" ]; then
  python manage.py compilemessages --ignore=staticfiles --ignore=media
fi

if [ "${DJANGO_COLLECTSTATIC:-0}" = "1" ]; then
  python manage.py collectstatic --noinput
fi

exec "$@"
