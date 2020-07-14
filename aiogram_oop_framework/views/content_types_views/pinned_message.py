from aiogram.types import ContentType

from .base import BaseContentTypesView


class PinnedMessageView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.PINNED_MESSAGE]"""
    content_types = [ContentType.PINNED_MESSAGE]
