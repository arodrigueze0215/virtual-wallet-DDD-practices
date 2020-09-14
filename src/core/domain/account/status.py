from enum import IntEnum

class Status(IntEnum):
    CLOSED = 0
    OPEN = 1

    def __str__(self):
        return f'{self.name} = {self.value}'