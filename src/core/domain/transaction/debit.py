from . import Transaction
from .events.fund_was_withdrew import FundWasWithDrew
class Debit(Transaction):
    def __init__(self, id_account, amountValue, descriptionText):
        super().__init__(id_account, amountValue, descriptionText)
        fund_was_withdrew = FundWasWithDrew(self.id)
        self.register(fund_was_withdrew)

    @staticmethod
    def withDraw(id_account, amountValue, descriptionText):
        debit = Debit(id_account, amountValue, descriptionText)
        return debit