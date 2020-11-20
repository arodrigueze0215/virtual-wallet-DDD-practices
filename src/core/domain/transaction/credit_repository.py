from abc import ABCMeta

#Domain
from .credit import Credit
class CreditRepository(metaclass=ABCMeta):
    """
    docstring
    """
    def save(self, credit: Credit) -> None : pass 
    def all(self) -> dict() : pass