from aiogram import executor

from examples.echo_bot.manage import initialize_project


if __name__ == '__main__':
    dp, bot = initialize_project()
    executor.start_polling(dp)
