from aiogram.types import ContentType

from .base import BaseContentTypesView


class PassportDataView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.PASSPORT_DATA]"""
    content_types = [ContentType.PASSPORT_DATA]
