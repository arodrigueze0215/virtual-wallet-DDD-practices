import uuid
from src.core.domain.account.amount import Amount
from src.core.domain.account.description import Description
from src.core.domain.account.transaction_date import TransactionDate

class Transaction():
    def __init__(self, amountValue, descriptionText):
        self.id = uuid.uuid4()
        self.amount = Amount(amountValue)
        self.description = Description(descriptionText)
        self.transactionDate = TransactionDate.create()

    def getAmount(self):
        return self.amount.value
