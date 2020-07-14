from aiogram.types import ContentType

from .base import BaseContentTypesView


class DeleteChatPhotoView(BaseContentTypesView):
    """Same as :class:`aiogram_oop_framework.views.content_types_views.animation.AnimationView`, but content_types defaults to [ContentType.DELETE_CHAT_PHOTO]"""
    content_types = [ContentType.DELETE_CHAT_PHOTO]
