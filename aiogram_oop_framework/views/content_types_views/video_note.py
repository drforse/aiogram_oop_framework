from aiogram.types import ContentType

from .base import BaseContentTypesView


class VideoNoteView(BaseContentTypesView):
    content_types = [ContentType.VIDEO_NOTE]
