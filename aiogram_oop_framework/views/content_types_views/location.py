from aiogram.types import ContentType

from .base import BaseContentTypesView


class LocationView(BaseContentTypesView):
    content_types = [ContentType.LOCATION]
