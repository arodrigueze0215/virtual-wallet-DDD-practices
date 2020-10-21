from .account import Account
from abc import ABCMeta

class AccountRepository(metaclass=ABCMeta):
    """ Account Repository, this is a Account port to comunicate with the repostories"""
    def findById(self, idAccount):
        pass

    def getAccountDetail(self, idAccount):
        pass

    def isClosed(self, accountId):
        pass

    def save(self, account:Account):
        pass

    def addDeposit(self, account:Account):
        pass

    def addWithdraw(self, account:Account):
        pass
    
    def update(self, account: Account):
        pass