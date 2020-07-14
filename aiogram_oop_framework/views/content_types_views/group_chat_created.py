from aiogram.types import ContentType

from .base import BaseContentTypesView


class GroupChatCreatedView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.GROUP_CHAT_CREATED]"""
    content_types = [ContentType.GROUP_CHAT_CREATED]
