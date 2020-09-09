#core
from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository as RepositoryBase

class AccountRepository(RepositoryBase):
    
    def __init__(self):
        self.store = {}

    def findById(self, idAccount):
        return self.store.get(idAccount)
    
    def isClosed(self, accountId):
        account = self.store.get(accountId)
        return account.isClosed()
    
    def save(self, account: Account):
        self.store[account.id] = account

