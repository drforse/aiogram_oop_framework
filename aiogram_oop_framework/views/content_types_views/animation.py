from aiogram.types import ContentType

from .base import BaseContentTypesView


class AnimationView(BaseContentTypesView):
    """May be same as :class:`aiogram_oop_framework.views.message.MessageView`, or
    :class:`aiogram_oop_framework.views.edited_message_view.EditedMessageView`, or
    :class:`aiogram_oop_framework.views.channel_post_view.ChannelPostView`, or
    :class:`aiogram_oop_framework.views.edited_channel_post_view.EditedChannelPostView`,
    dependently on update_type field, with difference that content_types field defaults to [ContentType.ANIMATION], and it has one more field:

    Attributes:
        update_type (str): Update type, must be one of: 'message', 'edited_message', 'channel_post', 'edited_channel_post', defaults to 'message's

    """
    content_types = [ContentType.ANIMATION]
