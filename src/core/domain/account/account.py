from src.core.domain.account.open_date import OpenDate
from src.core.domain.transaction.credit import Credit
from src.core.domain.transaction.debit import Debit
from src.core.domain.account.status import Status
from src.core.domain.exceptions import DontAllowWithdawMoreThanExistingFunds
from src.core.domain.agregate_root import AgregateRoot
from .events.account_was_created import AccountWasCreated
class Account(AgregateRoot):
    def __init__(self, idAccount, idCustomer):
        super().__init__(idAccount)
        self.id = idAccount
        self.status = Status.OPEN
        self.idCustomer = idCustomer
        self.balance = 0
        self.OpeningDate = OpenDate.create()
        self.debitList = list()

    @staticmethod
    def create(idAccount, idCustomer):
        account = Account(idAccount, idCustomer)
        accountWasCreated = AccountWasCreated(idAccount)
        account.register(accountWasCreated)
        return account

    def increase_balance(self, balance):
        self.balance = balance

    def decrease_balance(self, count):
        if count <= self.balance:
            self.balance = self.balance - count
        else:
            raise DontAllowWithdawMoreThanExistingFunds()

    def _calculateTotalDebit(self):
        count = 0
        for item in self.debitList:
            count += item.get_amount()
        count = self.balance - count
        return count

    def setStatus(self, status: Status):
        self.status = status

    def isClosed(self):
        return self.status == Status.CLOSED

    def setClose(self):
        if self.balance <= 0:
            self.setStatus(Status.CLOSED)

    def setOpeningDate(self, date):
        self.OpeningDate = OpenDate.add(date)
    
    def get_opening_date(self):
        return self.OpeningDate.date

    def __str__(self):
        return f'id:{self.id}, status:{self.status}, balance:{self.balance}'