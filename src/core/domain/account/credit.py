from .transaction import Transaction
class Credit(Transaction):
    def __init__(self, amountValue, descriptionText):
        super().__init__(amountValue, descriptionText)