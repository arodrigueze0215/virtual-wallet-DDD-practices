from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.status import Status
from src.core.domain.account.repository import AccountRepository
class CloseAccount():

    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository

    def execute(self, account_id):
        account = self.accountRepository.findById(account_id)
        account.setClose()
        self.accountRepository.update(account)
            