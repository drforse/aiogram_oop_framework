from aiogram.types import ContentType

from .base import BaseContentTypesView


class NewChatMembersView(BaseContentTypesView):
    content_types = [ContentType.NEW_CHAT_MEMBERS]
