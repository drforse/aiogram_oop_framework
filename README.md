# aiogram_oop_framework
An extender for aiogram to make it more OOP


# QUICK START

## 1) Create project
`python -m aiogram_oop_framework startproject mybot`
aiogram_oop_framework will create directory with your project
create projects in root directory, otherwise you may get in some bugs (but if you are ready to fix it, than it is even better for this framework's future xD)

## 2) Create your views in mybot.views directory
You can create views anywhere inside mybot (but not outside), but preferably in mybot.views or it's subdirectories

## 3) If you had created views not in mybot.views (if you created views in it's subdirectories, this is also for you):
In settings.py change project structure by writing struc.include(<path to directory containing your views> with dots as separators) before `pr.structure = struc`

## 4) Write your settings in settings.py, TELEGRAM_BOT_TOKEN is of course required

## 5) You can now run start polling with `python -m mybot.manage start_polling` or you can see how it is done in code in examples/<example_name>/__init__.py


# VIEWS

All your views must be inherited from BaseView, preferably using a more high-level class as MessageView, which are already inherited from BaseView
All settings which are present in aiogram in @dp.message_handler() as args now should be the Views' fields, ex.:
```
from aiogram_oop_framework.views import MessageView


class MyView(MessageView):
    regexp = r'^hello$'
    index = 0

    @classmethod
    async def execute(m, state, **kwargs):
        await m.answer('Hello there')
```

Every view has "index" field, which present the order in which the views will be registered, it is not a required field however
The code which will be run after handling update must be written in classmethod "execute"

