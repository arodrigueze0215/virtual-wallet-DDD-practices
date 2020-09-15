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

    
    def get_amount(self):
        return self.amount.value

    def get_date(self):
        return self.transactionDate.date

    def __str__(self):
        return f'Amount: {self.get_amount()}, Description: {self.description.text}'
