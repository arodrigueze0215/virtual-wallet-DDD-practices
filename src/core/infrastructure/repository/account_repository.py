#core
from src.core.domain.account.account import Account, Status
from src.core.domain.account.repository import AccountRepository as RepositoryBase

#models
from account.models import (
    Credit,
    Debit,
    Account as AccountDb
)

from .customer_repository import CustomerRepository
class AccountRepository(RepositoryBase):
    
    def __init__(self):
        self.store = {}
        self.customerRepository = CustomerRepository()

    def findById(self, idAccount):
        """This return an Account object that was found by ID from de DB"""

        account_db = AccountDb.objects.get(account_id = idAccount)
        if account_db is None:
            return None
        account = Account.create(account_db.account_id, account_db.customer.customer_id)
        account.setStatus(account_db.status)
        account.balance = account_db.balance
        account.setOpeningDate(account_db.opening_date)
        return account

    def _getAllMovements(self, account: Account):
        """ Get All Moventments Deposits and Debits"""        
        account_db = self.findAccountDBObjectById(account.id)
        deposit_list = Credit.objects.filter(account=account_db)
        for deposit in deposit_list:
            account.makeCredit(deposit.ammount, deposit.description)

        debit_list = Debit.objects.filter(account=account_db)
        for debit in debit_list:
            account.withDraw(debit.ammount, debit.description)



    def getAccountDetail(self, idAccount):
        account_db = AccountDb.objects.get(account_id = idAccount)
        if account_db is None:
            return None
        account = Account.create(account_db.account_id, account_db.customer.customer_id)
        account.setStatus(account_db.status)
        account.setOpeningDate(account_db.opening_date)
        self._getAllMovements(account)
        return account

    def isClosed(self, accountId):
        account_db = self.findAccountDBObjectById(accountId)
        return account_db.status == Status.CLOSED

    def findCustomerDBObjectById(self, customer_id):
        return self.customerRepository.getCustomerDBObject(customer_id)

    def findAccountDBObjectById(self, account_id):
        account_db = AccountDb.objects.get(account_id=account_id)
        if account_db is None:
            return None
        return account_db

    def addDeposit(self, account: Account):
        account_db = self.findAccountDBObjectById(account.id)
        credit = account.creditList[0]
        Credit.objects.create(
            account = account_db,
            ammount = credit.get_amount(),
            description = credit.description.text,
            transaction_date = credit.get_date()
        )

        all_deposit = Credit.objects.filter(account=account_db)
        balance = 0
        for deposit in all_deposit:
            balance = balance + deposit.ammount
        
        account_db.balance = balance
        account_db.save()

    def addWithdraw(self, account:Account):
        account_db = self.findAccountDBObjectById(account.id)
        debit = account.debitList[0]
        Debit.objects.create(
            account = account_db,
            ammount = debit.get_amount(),
            description = debit.description.text,
            transaction_date = debit.get_date()
        )

        all_debit = Debit.objects.filter(account=account_db)
        balance = account_db.balance
        for debit in all_debit:
            balance = balance - debit.ammount
        
        account_db.balance = balance
        account_db.save()
            

    def update(self, account: Account):
        account_db = self.findAccountDBObjectById(account.id)
        account_db.status = int(account.status)
        account_db.balance = account.balance
        account_db.opening_date = account.get_opening_date()
        account_db.save()
        

    def save(self, account: Account):
        customer = self.findCustomerDBObjectById(account.idCustomer)
        account_db = AccountDb()
        account_db.account_id = account.id
        account_db.customer = customer
        account_db.opening_date = account.OpeningDate.date
        account_db.status = int(account.status)
        account_db.balance = account.balance
        account_db.save()