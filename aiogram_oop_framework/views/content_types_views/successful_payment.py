from aiogram.types import ContentType

from .base import BaseContentTypesView


class SuccessfulPaymentView(BaseContentTypesView):
    content_types = [ContentType.SUCCESSFUL_PAYMENT]
