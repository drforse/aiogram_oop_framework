class WrongUpdateType(Exception):
    def __init__(self, txt=None):
        self.txt = txt


class BotTokenNotDefined(Exception):
    def __init__(self, txt=None):
        self.txt = txt


class FilterNameImpossible(Exception):
    def __init__(self, txt=None):
        self.txt = txt


class WrappedFunctionWrongAnnotations(Exception):
    def __init__(self, txt=None):
        self.txt = txt
