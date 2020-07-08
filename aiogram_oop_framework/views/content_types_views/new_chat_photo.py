from aiogram.types import ContentType

from .base import BaseContentTypesView


class NewChatPhotoView(BaseContentTypesView):
    content_types = [ContentType.NEW_CHAT_PHOTO]
