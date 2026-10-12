import os

bind = '0.0.0.0:8000'
workers = int(os.getenv('GUNICORN_WORKERS', '3'))
timeout = 60
graceful_timeout = 30

# Перезапуск воркеров снижает риск утечек памяти при долгой работе
max_requests = 1000
max_requests_jitter = 100

accesslog = '-'
errorlog = '-'

# Запросы приходят только от nginx на хосте через 127.0.0.1-порт
forwarded_allow_ips = '*'
