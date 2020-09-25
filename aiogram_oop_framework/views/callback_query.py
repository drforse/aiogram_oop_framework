from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext, Dispatcher

from .base import BaseView


class CallbackQueryView(BaseView):
    @classmethod
    async def execute(cls, q: CallbackQuery, state: FSMContext = None, **kwargs):
        raise NotImplementedError

    @classmethod
    async def _execute(cls, q: CallbackQuery, state: FSMContext = None, **kwargs):
        chat_type = q.message.chat.type
        if hasattr(cls, f'execute_in_{chat_type}'):
            await cls.__dict__[f'execute_in_{chat_type}'].__func__(cls, q, state, **kwargs)
            return
        await cls.execute(q, state, **kwargs)

    @classmethod
    def register(cls, dp: Dispatcher):
        callback = cls._execute
        kwargs = cls.register_kwargs if cls.register_kwargs else {}
        custom_filters = cls.custom_filters if cls.custom_filters else []
        dp.register_callback_query_handler(callback, *custom_filters, state=cls.state(),
                                           run_task=cls.run_task, **kwargs)
