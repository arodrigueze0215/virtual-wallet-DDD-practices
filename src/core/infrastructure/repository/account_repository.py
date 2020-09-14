#core
from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository as RepositoryBase

#models
from account.models import (
    Credit,
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
        if account_db == None:
            return None
        account = Account.create(account_db.account_id, account_db.customer.customer_id)
        account.setStatus(account_db.status)
        account.balance = account_db.balance
        account.setOpeningDate(account_db.opening_date)
        return account

    def isClosed(self, accountId):
        account = self.store.get(accountId)
        return account.isClosed()

    def findCustomerDBObjectById(self, customer_id):
        return self.customerRepository.getCustomerDBObject(customer_id)
    
    def save(self, account: Account):
        customer = self.findCustomerDBObjectById(account.idCustomer)
        account_db = AccountDb()
        account_db.account_id = account.id
        account_db.customer = customer
        account_db.opening_date = account.OpeningDate.date
        account_db.status = int(account.status)
        account_db.balance = account.balance
        account_db.save()