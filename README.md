# aiogram_oop_framework
An extender for aiogram to make it more OOP

## INSTALLATION
install with: 
```
pip install -e git://github.com/drforse/aiogram_oop_framework#egg=aiogram_oop_framework
```
uninstall with: 
```
pip uninstall aiogram_oop_framework
```


## QUICK START

### 1) Create project
```
python -m aiogram_oop_framework startproject mybot
```
aiogram_oop_framework will create directory with your project.

Create projects in root directory, otherwise you may get in some bugs (but if you are ready to fix it, than it is even better for this framework's future xD)

### 2) Create your views in mybot.views directory
You can create views anywhere inside mybot (but not outside), but preferably in mybot.views or it's subdirectories

### 3) If you had created views not in mybot.views (if you created views in it's subdirectories, this is also for you):
In settings.py change project structure by writing struc.include(<path to directory containing your views> with dots as separators) before `pr.structure = struc`

### 4) Write your settings in settings.py

### 5) You can now start polling with `python -m mybot.manage start-polling` or in code:
```
from aiogram import executor

from mybot.manage import initialize_project


if __name__ == '__main__':
    dp, bot = initialize_project()
    executor.start_polling(dp)
```
OR
```
from aiogram import executor, Dispatcher, Bot

from mybot.manage import initialize_project
from mybot.settings import TELEGRAM_BOT_TOKEN


if __name__ == '__main__':
    bot: Bot = Bot(TELEGRAM_BOT_TOKEN)
    dp: Dispatcher = Dispatcher(bot)
    initialize_project(dp, bot)
    executor.start_polling(dp)
```

## VIEWS

All your views must be inherited from BaseView, preferably using a more high-level class as MessageView, which are already inherited from BaseView (if not, you will need to define register method by yourself)
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

state must be a callable (most obvious a lambda), which returns the State object, because of some aiogram's State' specific shit
Every view has "index" field, which presents the order in which the views will be registered, it is not a required field however.
The code, which will be ran after handling update, must be written in classmethod "execute".
If you don't want the framework to automatically register your views, set AUTO_REGISTER_VIEWS in settings.py to False.
If you don't want some of views to be automatically register, set View.auto_register to False.
To register your view manually, call register method of your View, dp (aiogram's Dispatcher's instance) is a required parameter for this method.
