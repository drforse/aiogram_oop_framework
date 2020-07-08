from aiogram.types import ContentType

from .base import BaseContentTypesView


class GameView(BaseContentTypesView):
    content_types = [ContentType.GAME]
