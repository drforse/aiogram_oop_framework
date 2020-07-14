from aiogram.types import ContentType

from .base import BaseContentTypesView


class GameView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.GAME]"""
    content_types = [ContentType.GAME]
