from aiogram.types import ContentType

from .base import BaseContentTypesView


class MigrateToChatIdView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.MIGRATE_TO_CHAT_ID]"""
    content_types = [ContentType.MIGRATE_TO_CHAT_ID]
