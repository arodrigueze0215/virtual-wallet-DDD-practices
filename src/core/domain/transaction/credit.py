from . import Transaction
from src.core.domain.transaction.events.fund_was_deposited import FundWasDeposited
class Credit(Transaction):
    def __init__(self, id_account:int, amountValue:int, descriptionText:str):
        super().__init__(id_account, amountValue, descriptionText)
        fundWasDeposited = FundWasDeposited(self.id)
        self.register(fundWasDeposited)

    def __str__(self):
        return super().__str__()

    @staticmethod
    def makeCredit(id_account:int, amountValue:int, descriptionText:str):
        deposit = Credit(id_account, amountValue, descriptionText)
        return deposit