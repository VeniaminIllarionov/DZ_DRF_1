from rest_framework.serializers import ValidationError


class YoutubeValidation:
    """Валидатор на ссылку к видео"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if "youtube.com" not in val:
            raise ValidationError(f'{self.field} must be a YouTube link')

