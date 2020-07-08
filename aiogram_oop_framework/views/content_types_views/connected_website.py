from aiogram.types import ContentType

from .base import BaseContentTypesView


class ConnectedWebsiteView(BaseContentTypesView):
    content_types = [ContentType.CONNECTED_WEBSITE]
