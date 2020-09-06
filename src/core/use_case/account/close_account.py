from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.status import Status
class CloseAccount(object):

    def __init__(self, accountRepository):
        self.accountRepository = accountRepository

    def execute(self, account: Account):
        account.setClose()
        self.accountRepository.save(account)
            