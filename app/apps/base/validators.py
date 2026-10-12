from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_mb):
        self.max_mb = max_mb

    def __call__(self, file):
        if file.size > self.max_mb * 1024 * 1024:
            raise ValidationError(f'Файл больше {self.max_mb} МБ. Уменьшите его перед загрузкой.')

    def __eq__(self, other):
        return isinstance(other, MaxFileSizeValidator) and self.max_mb == other.max_mb


IMAGE_VALIDATORS = [
    FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp']),
    MaxFileSizeValidator(10),
]
AUDIO_VALIDATORS = [
    FileExtensionValidator(['mp3', 'ogg', 'm4a']),
    MaxFileSizeValidator(20),
]
SVG_VALIDATORS = [
    FileExtensionValidator(['svg']),
    MaxFileSizeValidator(2),
]
