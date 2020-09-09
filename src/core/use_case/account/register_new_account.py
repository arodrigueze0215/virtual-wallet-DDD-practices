
from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository
class RegisterNewAccount():
    
    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository


    def execute(self, idAccount, customer: Customer):
        account = Account(idAccount, customer.idCustomer)
        self.accountRepository.save(account)
