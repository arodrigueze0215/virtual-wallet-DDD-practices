from abc import ABCMeta

#Domain
from .debit import Debit
class DebitRepository(metaclass=ABCMeta):
    """
    docstring
    """
    def save(self, debit: Debit) -> None : pass 
    def all(self) -> dict() : pass