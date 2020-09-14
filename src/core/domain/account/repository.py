from .account import Account

class AccountRepository():
    """ Account Repository, this is a Account port to comunicate with the repostories"""
    def findById(self, idAccount):
        pass

    def isClosed(self, accountId):
        pass

    def save(self, account:Account):
        pass

    def storeTransaction(self, account:Account):
        pass