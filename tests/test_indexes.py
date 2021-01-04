import pytest

from aiogram_oop_framework.views import TextView, CommandView, CallbackQueryView
from aiogram_oop_framework.utils import order_views


class Abc(CommandView):
    pass


class Bear(TextView):
    index = 0


class Text(TextView):
    index = -1


class Text1(TextView):
    index = -2


class Call(CallbackQueryView):
    index = 1


class ThrowsException(TextView):
    index = 1


def test_indexes():
    views = order_views([Abc, Bear, Text, Text1, Call])
    assert views == [Bear, Call, Abc, Text1, Text]


def test_same_indexes_error():
    with pytest.raises(ValueError):
        order_views([Abc, Bear, Text, Text1, Call, ThrowsException])
