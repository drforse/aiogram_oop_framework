from aiogram.types import ContentType

from .base import BaseContentTypesView


class DiceView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.DICE]"""
    content_types = [ContentType.DICE]
