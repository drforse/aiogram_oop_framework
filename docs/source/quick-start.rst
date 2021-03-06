Quick-Start
===========


1) Create project

.. code-block:: python

    python -m aiogram_oop_framework startproject mybot


aiogram_oop_framework will create directory with your project.

Create projects in root directory, otherwise you may get in some bugs (but if you are ready to fix it, than it is even better for this framework's future xD)

2) Create your views in mybot.views directory
You can create views anywhere inside mybot (but not outside), but preferably in mybot.views or it's subdirectories
Your view must be inherited from any View class, for example: :class:`MessageView<aiogram_oop_framework.views.message.MessageView>`
and have classmethod .execute() which is used to run code. And it also may have additional classmethods with any name,
with filters (see :ref:`additional-filters<filter_execute decorator for methods>` for more info about filters)
Code example:

.. code-block:: python


    class Example(MessageView):

    @classmethod
    async def execute(cls, m: types.Message, state: FSMContext = None, **kwargs):
        await m.answer('Hello, World!')


3) If you had created views not in mybot.views (if you created views in it's subdirectories, this is also for you):
In settings.py change project structure by writing
:code:`struc.include(<path to directory containing your views> with dots as separators)` before :code:`pr.structure = struc`
For example:

.. code-block:: python

    pr: Project = Project(PROJECT_NAME, PATH)
    struc: ProjectStructure = ProjectStructure(pr)
    struc.include('views')
    struc.include('views.messages.user_commands')
    struc.include('views.callbacks')
    pr.structure = struc

    PROJECT: Project = pr


4) Write your settings in settings.py (see detailed explanation of all settings in :ref:`Settings`)

5) You can now start polling with :code:`python -m mybot.manage start-polling` or in code:

.. code-block:: python

    from aiogram import executor

    from mybot.manage import initialize_project


    if __name__ == '__main__':
        dp, bot = initialize_project()
        executor.start_polling(dp)


OR

.. code-block:: python

    from aiogram import executor, Dispatcher, Bot

    from mybot.manage import initialize_project
    from mybot.settings import TELEGRAM_BOT_TOKEN


    if __name__ == '__main__':
        bot: Bot = Bot(TELEGRAM_BOT_TOKEN)
        dp: Dispatcher = Dispatcher(bot)
        initialize_project(dp, bot)
        executor.start_polling(dp)


