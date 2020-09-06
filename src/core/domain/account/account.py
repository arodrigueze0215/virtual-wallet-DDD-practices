from src.core.domain.account.open_date import OpenDate
from src.core.domain.account.credit import Credit
from src.core.domain.account.debit import Debit
from src.core.domain.account.status import Status
from src.core.domain.exceptions import DontAllowWithdawMoreThanExistingFunds
class Account(object):
    def __init__(self, idAccount, idCustomer):
        self.id = idAccount
        self.status = Status.OPEN
        self.idCustomer = idCustomer
        self.balance = 0
        self.OpeningDate = OpenDate.create()
        self.creditList = list()
        self.debitList = list()

    @staticmethod
    def create(idAccount, idCustomer):
        account = Account(idAccount, idCustomer)
        return account

    def makeCredit(self, amountValue, descriptionText):
        credit = Credit(amountValue, descriptionText)
        self.creditList.append(credit)
        self.balance = self._calculateTotalCredit()
    
    def withDraw(self, amountValue, descriptionText):
        debit = Debit(amountValue, descriptionText)
        if debit.getAmount() <= self.balance:
            self.debitList.append(debit)
            self.balance = self._calculateTotalDebit()
        else:
            raise DontAllowWithdawMoreThanExistingFunds()



    def _calculateTotalCredit(self):
        count = 0
        for item in self.creditList:
            count += item.getAmount()
        return count

    def _calculateTotalDebit(self):
        count = 0
        for item in self.debitList:
            count += item.getAmount()
        count = self.balance - count
        return count

    def setStatus(self, status: Status):
        self.status = status

    def isClosed(self):
        return self.status == Status.CLOSED

    def setClose(self):
        if self.balance <= 0:
            self.setStatus(Status.CLOSED)


        