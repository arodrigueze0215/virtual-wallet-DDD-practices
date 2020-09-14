
from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository
from src.core.domain.customer.repository import CustomerRepository
class RegisterNewAccount():
    
    def __init__(self, accountRepository: AccountRepository, customerRepository: CustomerRepository):
        self.accountRepository = accountRepository
        self.customerRepository = customerRepository


    def execute(self, idAccount, customer_id):
        customer = self.customerRepository.findById(customer_id)
        account = Account(idAccount, customer.idCustomer)
        self.accountRepository.save(account)
