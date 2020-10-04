Utils
=====

aiogram_oop_framework.utils.get_help
-------------------------------------
Use get_help(command) to get help for command

It looks for all registered handlers with the specified command in handler's filters and returns .get_help() return (which is (View.help_text or View.__doc__) by default) of the first found View, if the handler is method of a BaseView subclass, else it returns __doc__ argument of the function

So, you can write help's text in View's docs, in View's help_text attribute, in View's get_text() method, or if not using views (what the point using the framework then however?) - in function docs.


Usage examples:
+++++++++++++++

.. code-block:: python

    class Start(CommandView):
    """start doc"""
    @classmethod
    async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
        await m.answer('hi')


    @dp.message_handler(commands=['cancel'])
    async def foo(m: Message, state: FSMContext = None, **kwargs):
        """cancel doc"""
        await m.answer('canceled')


    class Help(CommandView):
        """your description for you and other developers"""
        help_text = "help help for users"
        @classmethod
        async def execute(cls, m: Message, state: FSMContext = None, **kwargs):
            await m.answer('...\n\nWrite /help &lt;command&gt; for more info')

        @classmethod
        @filter_execute(lambda m: m.get_args(), update_type='message')
        async def execute_with_args(cls, m: Message, state: FSMContext = None, **kwargs):
            help_ = get_help(m.get_args())
            if help_:
                await m.answer(help_)
            else:
                await m.answer("Sry, help for command isn't found")


Commands
--------
Docs not ready yet...
