Additional Filters
===================

filter_execute decorator for methods
------------------------------------
You can add to your views additional filters for calling different methods dependently on conditions.
filter_execute accepts all `aiogram filters <https://docs.aiogram.dev/en/latest/dispatcher/filters.html>`_ with content_types set to ContentType.all() by default

Example:

.. code-block:: python

    from aiogram import types
    from aiogram.dispatcher import FSMContext
    from aiogram.types.chat_member import ChatMemberStatus

    from aiogram_oop_framework.views import MessageView
    from aiogram_oop_framework.filters import filter_execute


    class Example(MessageView):

        @classmethod
        async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
            """this will be executed if chat type is not private"""
            await m.answer('undef')

        @classmethod
        @filter_execute(chat_member_status=ChatMemberStatus.ADMINISTRATOR)
        async def execute_for_admins(cls, m: types.Message, state: FSMContext = None, **kwargs):
            """execute if sender is administrator"""
            await m.answer('gg ADMIN brr')


aiogram_oop_framework builtin filters list:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

chat_member_status
    status of from_user member (it calls bot.get_chat_member to find out the status!)
chat_type
    type of chat where update occurred
entities
    if message.entities/message.caption_entities/poll.explanation_entities contains entities with specified types
poll_type
    type of the Poll
dice_emoji
    dice's emoji
func
    |a callable, which returns boolean value
    |DEPRECATED in 0.2.dev4, because of starting using aiogram filters, so you can simply put the func in args (ex.: filter_execute(foo))


While func may only be a function or lambda, other filter types accept much more values:

- str
- aiogram.util.helper.Item (for ex.: ChatType.PRIVATE)
- list of the above
- a function, which accepts a TelegramObject as parameter and returns any of the above



| Note!
| filter_execute works with execute_in_<chat_type> with no problem, if it's given chat_type in filter_execute, then chat_type from method's name is omitted
