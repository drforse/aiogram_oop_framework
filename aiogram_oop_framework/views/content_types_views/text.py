from aiogram.types import ContentType

from .base import BaseContentTypesView


class TextView(BaseContentTypesView):
    content_types = [ContentType.TEXT]
