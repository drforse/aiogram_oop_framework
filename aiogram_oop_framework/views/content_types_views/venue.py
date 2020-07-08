from aiogram.types import ContentType

from .base import BaseContentTypesView


class VenueView(BaseContentTypesView):
    content_types = [ContentType.VENUE]
