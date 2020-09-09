from src.core.domain.account.repository import AccountRepository
class GetAccountDetails():
    def __init__(self, accountRepository:AccountRepository):
        self.accountRepository = accountRepository

    def execute(self, idAccount):
        return self.accountRepository.findById(idAccount)