from aiogram.types import ContentType

from .base import BaseContentTypesView


class NewChatTitleView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.NEW_CHAT_TITLE]"""
    content_types = [ContentType.NEW_CHAT_TITLE]
