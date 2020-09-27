from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram_oop_framework.views import AnyContentTypeMessageView


class Echo(AnyContentTypeMessageView):
    index = 0

    @classmethod
    async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
        print(m)
        await m.send_copy(m.chat.id, reply_to_message_id=m.message_id)
