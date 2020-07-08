from aiogram.types import ContentType

from .base import BaseContentTypesView


class PollMessageView(BaseContentTypesView):
    content_types = [ContentType.POLL]
