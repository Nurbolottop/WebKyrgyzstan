#!/bin/bash
# Обновление production: ./deploy/deploy.sh  (запускать из /root/WebKyrgyzstan)
set -euo pipefail
cd "$(dirname "$0")/.."

git pull --ff-only
mkdir -p volumes/static volumes/media
chown -R 1000:1000 volumes
docker compose -f docker-compose.prod.yml up -d --build
docker image prune -f >/dev/null
echo "Готово: https://webkg.zeastudio.su"
