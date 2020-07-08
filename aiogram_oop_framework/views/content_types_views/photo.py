from aiogram.types import ContentType

from .base import BaseContentTypesView


class PhotoView(BaseContentTypesView):
    content_types = [ContentType.PHOTO]
