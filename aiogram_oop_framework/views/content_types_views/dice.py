from aiogram.types import ContentType

from .base import BaseContentTypesView


class DiceView(BaseContentTypesView):
    content_types = [ContentType.DICE]
