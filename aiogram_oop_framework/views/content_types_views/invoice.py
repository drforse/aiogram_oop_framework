from aiogram.types import ContentType

from .base import BaseContentTypesView


class InvoiceView(BaseContentTypesView):
    content_types = [ContentType.INVOICE]
