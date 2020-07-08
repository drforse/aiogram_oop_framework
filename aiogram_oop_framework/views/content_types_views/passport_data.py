from aiogram.types import ContentType

from .base import BaseContentTypesView


class PassportDataView(BaseContentTypesView):
    content_types = [ContentType.PASSPORT_DATA]
