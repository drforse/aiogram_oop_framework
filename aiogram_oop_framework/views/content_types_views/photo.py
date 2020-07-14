from aiogram.types import ContentType

from .base import BaseContentTypesView


class PhotoView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.PHOTO]"""
    content_types = [ContentType.PHOTO]
