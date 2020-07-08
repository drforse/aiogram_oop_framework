from aiogram.types import ContentType

from .base import BaseContentTypesView


class AnimationView(BaseContentTypesView):
    content_types = [ContentType.ANIMATION]
