
#Domain
from src.core.domain.transaction.debit import Debit
from src.core.domain.transaction.credit_repository import CreditRepository as BaseRepository

class DebitRepository(BaseRepository):
    """
    Repository in memory to save all Credits
    """

    def __init__(self):
        """ Credit Repository Constructor """
        self.debitList = dict()
    
    def save(self, debit:Debit):
        """ Save the debit inside repository """
        self.debitList[debit.id] = debit

    def all(self) -> dict():
        return self.debitList