from aiogram.types import ContentType

from .base import BaseContentTypesView


class TextView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.TEXT]"""
    content_types = [ContentType.TEXT]
