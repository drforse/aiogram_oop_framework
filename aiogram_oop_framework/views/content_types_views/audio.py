from aiogram.types import ContentType

from .base import BaseContentTypesView


class AudioView(BaseContentTypesView):
    content_types = [ContentType.AUDIO]
