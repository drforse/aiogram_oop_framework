from aiogram.types import ContentType

from .base import BaseContentTypesView


class NewChatTitleView(BaseContentTypesView):
    content_types = [ContentType.NEW_CHAT_TITLE]
