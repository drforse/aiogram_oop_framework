from aiogram.types import ContentType

from .base import BaseContentTypesView


class AudioView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.AUDIO]"""
    content_types = [ContentType.AUDIO]
