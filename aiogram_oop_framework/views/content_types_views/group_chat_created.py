from aiogram.types import ContentType

from .base import BaseContentTypesView


class GroupChatCreatedView(BaseContentTypesView):
    content_types = [ContentType.GROUP_CHAT_CREATED]
