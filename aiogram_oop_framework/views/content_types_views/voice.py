from aiogram.types import ContentType

from .base import BaseContentTypesView


class VoiceView(BaseContentTypesView):
    content_types = [ContentType.VOICE]
