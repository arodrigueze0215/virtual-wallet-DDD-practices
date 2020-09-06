#core
from src.core.domain.account.account import Account

#models
from model.models import Account as AccountDb

from .customer_repository import CustomerRepository
class AccountRepository(object):
    
    def __init__(self):
        self.store = {}
        self.customerRepository = CustomerRepository()

    def findById(self, idAccount):
        return self.store.get(idAccount)
    
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
        account_db.status = str(int(account.status.OPEN))
        account_db.balance = account.balance
        account_db.save()

