from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.status import Status
from src.core.domain.account.repository import AccountRepository
from src.core.infrastructure.repository_in_memory.debit_repository import DebitRepository
class DecreaseBalanceAccount():

    def __init__(self, account_repository: AccountRepository, debit_repository: DebitRepository):
        self.account_repository = account_repository
        self.debit_repository = debit_repository

    def execute(self, account_id):
        account = self.account_repository.findById(account_id)
        debit_list = self.debit_repository.all()
        count_decreased = self._decrease_balance(debit_list)
        account.decrease_balance(count_decreased)
        self.account_repository.update(account)
            

    def _decrease_balance(self, debit_list):
        count_decreased = 0
        for item in debit_list.values():
            count_decreased += item.get_amount()
        return count_decreased