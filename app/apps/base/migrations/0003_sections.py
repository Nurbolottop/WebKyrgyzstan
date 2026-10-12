from django.db import migrations

# Пять разделов сайта. Набор фиксирован: в админке их нельзя добавить или удалить,
# можно только редактировать тексты и обложки.
SECTIONS = [
    {
        'key': 'discover',
        'title': ('Кыргызстанды ачып көр', 'Открой Кыргызстан', 'Discover Kyrgyzstan'),
        'description': (
            'Кыргызстандын облустары, тоолору, көлдөрү жана кооз жерлери интерактивдүү картада.',
            'Области, горы, озёра и достопримечательности Кыргызстана на интерактивной карте.',
            "Regions, mountains, lakes and landmarks of Kyrgyzstan on an interactive map.",
        ),
    },
    {
        'key': 'culture',
        'title': ('Маданият жана салттар', 'Культура и традиции', 'Culture and Traditions'),
        'description': (
            'Боз үй, шырдак, комуз, улуттук кийим, Нооруз жана «Манас» эпосу.',
            'Юрта, шырдак, комуз, национальная одежда, Нооруз и эпос «Манас».',
            'The yurt, shyrdak, komuz, national dress, Nooruz and the Manas epic.',
        ),
    },
    {
        'key': 'learn',
        'title': ('Үйрөн жана ойно', 'Учись и играй', 'Learn and Play'),
        'description': (
            'Викториналар, табышмактар, ребустар, кыргыз тили жана оюндар.',
            'Викторины, загадки, ребусы, кыргызский язык и мини-игры.',
            'Quizzes, riddles, rebuses, the Kyrgyz language and mini-games.',
        ),
    },
    {
        'key': 'practice',
        'title': ('Өзүң жасап көр', 'Попробуй сам', 'Try It Yourself'),
        'description': (
            'Улуттук тамактардын рецепттери, мастер-класстар жана чыгармачыл тапшырмалар.',
            'Рецепты национальных блюд, мастер-классы и творческие задания.',
            'National recipes, master classes and creative tasks.',
        ),
    },
    {
        'key': 'modern',
        'title': ('Азыркы Кыргызстан', 'Современный Кыргызстан', 'Modern Kyrgyzstan'),
        'description': (
            'Спорт, технологиялар, жаштардын жетишкендиктери жана кызыктуу кесиптер.',
            'Спорт, технологии, достижения молодёжи и интересные профессии.',
            'Sport, technology, youth achievements and interesting professions.',
        ),
    },
]


def create_sections(apps, schema_editor):
    Section = apps.get_model('base', 'Section')
    for order, data in enumerate(SECTIONS, start=1):
        title_ky, title_ru, title_en = data['title']
        desc_ky, desc_ru, desc_en = data['description']
        Section.objects.update_or_create(
            key=data['key'],
            defaults={
                'order': order,
                'title': title_ru,
                'title_ky': title_ky,
                'title_ru': title_ru,
                'title_en': title_en,
                'description': desc_ru,
                'description_ky': desc_ky,
                'description_ru': desc_ru,
                'description_en': desc_en,
            },
        )


def create_site_settings(apps, schema_editor):
    SiteSettings = apps.get_model('base', 'SiteSettings')
    SiteSettings.objects.get_or_create(pk=1)


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(create_sections, migrations.RunPython.noop),
        migrations.RunPython(create_site_settings, migrations.RunPython.noop),
    ]
