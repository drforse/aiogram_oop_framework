from aiogram.types import ContentType

from .base import BaseContentTypesView


class MigrateToChatIdView(BaseContentTypesView):
    content_types = [ContentType.MIGRATE_TO_CHAT_ID]
