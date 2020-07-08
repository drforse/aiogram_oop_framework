from aiogram.types import ContentType

from .base import BaseContentTypesView


class AnyContentTypeMessageView(BaseContentTypesView):
    content_types = ContentType.all()
