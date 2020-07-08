from aiogram.types import ContentType

from .base import BaseContentTypesView


class LeftChatMemberView(BaseContentTypesView):
    content_types = [ContentType.LEFT_CHAT_MEMBER]
