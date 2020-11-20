
#Domain
from src.core.domain.transaction.credit import Credit
from src.core.domain.transaction.credit_repository import CreditRepository as BaseRepository

class CreditRepository(BaseRepository):
    """
    Repository in memory to save all Credits
    """

    def __init__(self):
        """ Credit Repository Constructor """
        self.creditList = dict()
    
    def save(self, credit:Credit):
        """ Save the Credit inside repository """
        self.creditList[credit.id] = credit

    def all(self) -> dict():
        return self.creditList