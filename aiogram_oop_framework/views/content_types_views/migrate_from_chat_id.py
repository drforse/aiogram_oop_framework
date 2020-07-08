from aiogram.types import ContentType

from .base import BaseContentTypesView


class MigrateFromChatIdView(BaseContentTypesView):
    content_types = [ContentType.MIGRATE_FROM_CHAT_ID]
