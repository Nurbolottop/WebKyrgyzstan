"""
Обложки из Wikimedia Commons — только свободные лицензии (CC0, PD, CC BY, CC BY-SA).
У каждой обложки сохраняется автор и лицензия. Уже загруженные в админке обложки
не трогаются (--force перезаписывает).

    python manage.py fetch_photos
"""
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from apps.articles.models import Article, Category
from apps.base.models import GalleryImage, Section
from apps.discover.models import Place, Region
from apps.practice.models import Activity

USER_AGENT = 'WebKyrgyzstan/1.0 (educational website for children; webkg.zeastudio.su)'
FREE_LICENSE = re.compile(r'^(CC BY(-SA)? [0-9.]+|CC0|Public domain|PD)', re.I)

PHOTOS = [
    # (модель, поле поиска, значение, файл на Commons)
    (Place, 'slug', 'issyk-kul-lake', 'File:Lake Issyk-Kul, Kyrgyzstan.jpg'),
    (Place, 'slug', 'son-kul-lake', 'File:View Son-Kul lake and Ak-Tash mountains, Kyrgyzstan - panoramio.jpg'),
    (Place, 'slug', 'sulaiman-too', 'File:Sulayman Mountain, Osh.jpg'),
    (Place, 'slug', 'tash-rabat', 'File:Caravanserai- Tash Rabat - panoramio.jpg'),
    (Place, 'slug', 'burana-tower', 'File:Burana Tower, Kyrgyzstan 01.jpg'),
    (Place, 'slug', 'arslanbob', 'File:Walnut forest Arslanbob.jpg'),
    (Place, 'slug', 'ala-archa', 'File:Pix113. Ala-Archa National Park.jpg'),
    (Place, 'slug', 'sary-chelek', 'File:Sary Chelek Lake.jpg'),

    (Region, 'slug', 'issyk-kul', 'File:Issyk kul Lake 2.jpg'),
    (Region, 'slug', 'naryn', 'File:Kyrgyzská jurta, Song-köl.jpg'),
    (Region, 'slug', 'chuy', 'File:Burana Tower site 13.jpg'),
    (Region, 'slug', 'jalal-abad', 'File:Sary-Chelek lake 2025.jpg'),
    (Region, 'slug', 'osh-city', 'File:Sulayman Mountain with flag.jpg'),
    (Region, 'slug', 'bishkek', 'File:Ala Too Square Bishkek 2021.jpg'),

    (Section, 'key', 'discover', 'File:Kyrgyzstan, Tian Shan Mountains (14244010047).jpg'),
    (Section, 'key', 'culture', 'File:Kyrgyz Yurt, Kyrgyzstan.jpg'),
    (Section, 'key', 'practice', 'File:Boortsog 2.JPG'),
    (Section, 'key', 'modern', 'File:Ala-Too Square in Bishkek.jpg'),

    (Category, 'slug', 'crafts', 'File:Kyrgyz design felt rugs.jpg'),
    (Category, 'slug', 'yurt', 'File:Dismantling a Yurt at Lake Tuz-Kol at Kyzyl-Tuu.jpg'),

    (Article, 'slug', 'why-issyk-kul-does-not-freeze', 'File:Issyk kul Lake 1.jpg'),
    (Article, 'slug', 'how-a-yurt-is-built',
     'File:The ethnic village, consisting of a traditional dwelling - a yurt, Kyrgyzstan, World Nomad Games 2018.jpg'),
    (Article, 'slug', 'what-is-a-komuz', 'File:Dusepo komuz front.jpg'),
    (Article, 'slug', 'shyrdak-felt-carpet', 'File:Shyrdak on floor.jpg'),
    (Article, 'slug', 'ak-kalpak', 'File:Kyrgyz man with ak-kalpak hat (ак-калпак шапкa).jpg'),
    (Article, 'slug', 'manas-epic', 'File:Philharmonic, Bishkek 01.jpg'),
    (Article, 'slug', 'kok-boru-and-nomad-games', 'File:Kok-boru, Kyrgyzstan 2018.jpg'),
    (Article, 'slug', 'it-in-kyrgyzstan', 'File:Bishkek City.jpg'),
    (Activity, 'slug', 'boorsok', 'File:Boortsog 2.JPG'),

    (Region, 'slug', 'talas', 'File:Manas Ordo near Talas.jpg'),
    (Region, 'slug', 'osh-region', 'File:Alai Valley 1.jpg'),
    (Article, 'slug', 'snow-leopard', 'File:Snow leopard portrait.jpg'),
    (Article, 'slug', 'why-so-many-mountains',
     'File:Pik Pobedy and Vazha-Pshavela Peak at sunset from South Engilchek Base Camp, Central Tian Shan, Kyrgyzstan.jpg'),
    (Article, 'slug', 'glaciers-water-tanks', 'File:Khan Tengri, Southern Inylchek Glacier, Tien Shan — Golden Hour.jpg'),
    (Article, 'slug', 'toguz-korgool', 'File:Toguz kumalak.jpg'),
    (Article, 'slug', 'bishkek-today', 'File:Oak Park in Bishkek.jpg'),
]


# Дополнительные фото для фотогалерей (добавляются, только если галерея пуста)
GALLERY = [
    (Place, 'issyk-kul-lake', ['File:Issyk kul Lake 3.jpg', 'File:Issyk kul Lake 1.jpg']),
    (Place, 'son-kul-lake', ['File:Song Köl lake, Kyrgyzstan (29441553104).jpg', 'File:View to lake Son-Kul, Kyrgyzstan - panoramio.jpg']),
    (Place, 'sulaiman-too', ['File:Cave on Sulayman Mountain 2.jpg', 'File:Building at Sulayman Mountain in Osh.jpg']),
    (Place, 'burana-tower', ['File:Burana Tower site 05.jpg', 'File:Burana Tower site 12.jpg']),
    (Place, 'ala-archa', ['File:Ала-Арча сверху (1).jpg', 'File:Ала-Арча сверху (3).jpg']),
    (Place, 'sary-chelek', ['File:Sary Chelek and bird.jpg', 'File:Sary Chelek Lake 2.1.jpg']),
    (Place, 'arslanbob', ['File:Walnut forest in Arslanbab.jpg']),
    (Article, 'glaciers-water-tanks', ['File:Glacier valley in Khan Tengri Nature Park, Tien Shan.jpg']),
    (Article, 'how-a-yurt-is-built', ['File:Dismantling a Yurt at Lake Tuz-Kol at Kyzyl-Tuu 2.jpg']),
    (Article, 'kok-boru-and-nomad-games', ['File:Kok-boru Cholpon-Ata, Kyrgyzstan 2018.jpg', 'File:The ethnic village, World Nomad Games.jpg']),
]


def fetch(url):
    """GET с паузой: Wikimedia отвечает 429 на частые запросы."""
    for attempt in range(4):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': USER_AGENT})).read()
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    return b''


def commons_info(title, width=1600):
    params = {
        'action': 'query', 'titles': title, 'prop': 'imageinfo', 'format': 'json',
        'iiprop': 'url|extmetadata', 'iiurlwidth': width,
    }
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    data = json.loads(fetch(url))
    page = next(iter(data['query']['pages'].values()))
    info = page['imageinfo'][0]
    meta = info.get('extmetadata', {})
    artist = re.sub(r'<[^>]+>', '', meta.get('Artist', {}).get('value', '')).strip() or 'неизвестный автор'
    license_name = meta.get('LicenseShortName', {}).get('value', '')
    return info['thumburl'], artist, license_name


class Command(BaseCommand):
    help = 'Загружает обложки со свободной лицензией из Wikimedia Commons.'

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', help='Перезаписать уже заданные обложки.')

    def handle(self, *args, force=False, **options):
        for model, field, value, title in PHOTOS:
            obj = model.objects.filter(**{field: value}).first()
            if obj is None:
                self.stdout.write(f'  нет записи {model.__name__} {value} — пропуск')
                continue
            if obj.cover and not force:
                self.stdout.write(f'  {obj}: обложка уже есть')
                continue
            try:
                url, artist, license_name = commons_info(title)
            except (OSError, KeyError, StopIteration) as error:
                self.stderr.write(f'  {title}: {error}')
                continue
            if not FREE_LICENSE.match(license_name):
                self.stderr.write(f'  {title}: лицензия «{license_name}» не подходит')
                continue

            content = fetch(url)
            time.sleep(3)
            obj.cover.save(f'{value}{Path(url).suffix.lower() or ".jpg"}', ContentFile(content), save=False)
            obj.cover_credit = f'{artist[:120]} · {license_name} · Wikimedia Commons'
            for lang in ('ky', 'ru', 'en'):
                setattr(obj, f'cover_alt_{lang}', getattr(obj, f'title_{lang}') or obj.title_ru)
            obj.save()
            self.stdout.write(self.style.SUCCESS(f'  {obj}: {license_name}, {artist[:40]}'))

        self.fill_galleries()

    def fill_galleries(self):
        for model, slug, titles in GALLERY:
            obj = model.objects.filter(slug=slug).first()
            if obj is None or obj.gallery.exists():
                continue
            for order, title in enumerate(titles, start=1):
                try:
                    url, artist, license_name = commons_info(title, width=1600)
                    if not FREE_LICENSE.match(license_name):
                        self.stderr.write(f'  {title}: лицензия «{license_name}» не подходит')
                        continue
                    content = fetch(url)
                    time.sleep(3)
                except (OSError, KeyError, StopIteration) as error:
                    self.stderr.write(f'  {title}: {error}')
                    continue
                photo = GalleryImage(content_object=obj, order=order,
                                     credit=f'{artist[:120]} · {license_name} · Wikimedia Commons')
                for lang in ('ky', 'ru', 'en'):
                    setattr(photo, f'alt_{lang}', getattr(obj, f'title_{lang}') or obj.title_ru)
                photo.image.save(f'{slug}-{order}{Path(url).suffix.lower() or ".jpg"}', ContentFile(content), save=False)
                photo.save()
                self.stdout.write(self.style.SUCCESS(f'  галерея {obj}: {license_name}, {artist[:40]}'))
