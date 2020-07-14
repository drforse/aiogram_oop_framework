from aiogram.types import ContentType

from .base import BaseContentTypesView


class DocumentView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.DOCUMENT]"""
    content_types = [ContentType.DOCUMENT]
