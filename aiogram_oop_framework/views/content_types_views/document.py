from aiogram.types import ContentType

from .base import BaseContentTypesView


class DocumentView(BaseContentTypesView):
    content_types = [ContentType.DOCUMENT]
