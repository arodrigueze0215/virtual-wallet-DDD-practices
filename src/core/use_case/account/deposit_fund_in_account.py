from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository
class DepositFundInAccount(object):

    def __init__(self, accountRepository:AccountRepository):
        self.accountRepository = accountRepository

    def execute(self, idAccount, amount, description):
        account = self.accountRepository.findById(idAccount)
        account.makeCredit(amount, description)
        self.accountRepository.save(account)