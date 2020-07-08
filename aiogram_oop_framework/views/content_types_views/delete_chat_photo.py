from aiogram.types import ContentType

from .base import BaseContentTypesView


class DeleteChatPhotoView(BaseContentTypesView):
    content_types = [ContentType.DELETE_CHAT_PHOTO]
