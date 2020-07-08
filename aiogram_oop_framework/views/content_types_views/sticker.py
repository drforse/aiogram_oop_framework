from aiogram.types import ContentType

from .base import BaseContentTypesView


class StickerView(BaseContentTypesView):
    content_types = [ContentType.STICKER]
