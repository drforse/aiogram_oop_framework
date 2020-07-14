from aiogram.types import ContentType

from .base import BaseContentTypesView


class VideoNoteView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.VIDEO_NOTE]"""
    content_types = [ContentType.VIDEO_NOTE]
