from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.status import Status
from src.core.domain.account.repository import AccountRepository
from src.core.infrastructure.repository_in_memory.credit_repository import CreditRepository
class IncreaseBalanceAccount():

    def __init__(self, accountRepository: AccountRepository, creditRepository: CreditRepository):
        self.accountRepository = accountRepository
        self.creditRepository = creditRepository

    def execute(self, account_id):
        account = self.accountRepository.findById(account_id)
        credit_list = self.creditRepository.all()
        balance = self._increase_balance(credit_list)
        account.increase_balance(balance)
        self.accountRepository.update(account)
            

    def _increase_balance(self, credit_list):
        count = 0
        for item in credit_list.values():
            count += item.get_amount()
        return count