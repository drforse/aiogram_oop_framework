from aiogram.types import ContentType

from .base import BaseContentTypesView


class ConnectedWebsiteView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.CONNECTED_WEBSITE]"""
    content_types = [ContentType.CONNECTED_WEBSITE]
