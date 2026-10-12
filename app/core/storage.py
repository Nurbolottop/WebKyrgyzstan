from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class StaticStorage(ManifestStaticFilesStorage):
    """
    Хеширует имена статических файлов (их можно кешировать «навсегда»)
    и переписывает import/export внутри ES-модулей на хешированные пути.

    Переписываются только наши модули из static/js/: в чужих сборках
    (например, CKEditor) строки вида import ... встречаются внутри кода
    и ломают collectstatic.

    Пути для динамического import() не переписываются — их передаём
    из шаблона через {% static %} в data-атрибуте.
    """

    support_js_module_import_aggregation = True
    _js_module_import_aggregation_patterns = (
        'js/*.js',
        ManifestStaticFilesStorage._js_module_import_aggregation_patterns[1],
    )
