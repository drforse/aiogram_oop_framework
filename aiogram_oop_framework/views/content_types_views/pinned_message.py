from aiogram.types import ContentType

from .base import BaseContentTypesView


class PinnedMessageView(BaseContentTypesView):
    content_types = [ContentType.PINNED_MESSAGE]
