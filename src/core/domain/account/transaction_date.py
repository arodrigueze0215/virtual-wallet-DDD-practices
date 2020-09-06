from datetime import date
class TransactionDate(object):
    def __init__(self):
        self.date = date.today()

    @staticmethod
    def create():
        transactionDate = TransactionDate()
        return TransactionDate
        