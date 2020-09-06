from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
class DepositFundInAccount(object):

    def __init__(self, accountRepository):
        self.accountRepository = accountRepository

    def execute(self, account: Account, amount, description):
        account.makeCredit(amount, description)
        self.accountRepository.save(account)