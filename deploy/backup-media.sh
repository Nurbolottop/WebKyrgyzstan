#!/bin/bash
# Ежедневный архив загруженных файлов (базу бэкапит общий /usr/local/bin/db-backup).
# Ставится в /etc/cron.d/webkg-media-backup:  30 4 * * * root /root/WebKyrgyzstan/deploy/backup-media.sh
set -euo pipefail
umask 077
SRC=/root/WebKyrgyzstan/volumes/media
DEST=/var/backups/media/webkg
mkdir -p "$DEST"
tar -czf "$DEST/media_$(date +%F).tar.gz" --exclude='renditions' -C "$SRC" .
find "$DEST" -name 'media_*.tar.gz' -mtime +14 -delete
