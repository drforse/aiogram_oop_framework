from .message import MessageView


class ChannelPostView(MessageView):
    @classmethod
    def register(cls):
        """

        Make sure you don't want to use a more high-level like Command or Photo view instead
        """
        callback = cls.execute
        cls.dp.register_channel_post_handler(callback=callback, *cls.custom_filters, commands=cls.commands,
                                             regexp=cls.regexp, content_types=cls.content_types, state=cls.state,
                                             run_task=cls.run_task, **cls.register_kwargs)
