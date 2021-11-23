from .code_generator import add_count
from os.path import splitext


class AutoCodedFileName:
    def __init__(self, code_generator=None):
        self.code_generator = code_generator if code_generator is not None else add_count()

    def coded(self, dst):
        return f'{splitext(dst)[0]}_{str(next(self.code_generator))}{splitext(dst)[1]}'
