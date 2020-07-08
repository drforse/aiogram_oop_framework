class WrongUpdateType(Exception):
    def __init__(self, txt=None):
        self.txt = txt
