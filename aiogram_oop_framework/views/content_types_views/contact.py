from aiogram.types import ContentType

from .base import BaseContentTypesView


class ContactView(BaseContentTypesView):
    content_types = [ContentType.CONTACT]
