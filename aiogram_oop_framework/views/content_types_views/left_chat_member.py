from aiogram.types import ContentType

from .base import BaseContentTypesView


class LeftChatMemberView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.LEFT_CHAT_MEMBER]"""
    content_types = [ContentType.LEFT_CHAT_MEMBER]
