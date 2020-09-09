from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.status import Status
from src.core.domain.account.repository import AccountRepository
class CloseAccount(object):

    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository

    def execute(self, account: Account):
        account.setClose()
        self.accountRepository.save(account)
            