
from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository
from src.core.domain.customer.repository import CustomerRepository

#share
from src.core.share.event_driven.event_bus import EventBus
class RegisterNewAccount():
    
    def __init__(self, accountRepository: AccountRepository, customerRepository: CustomerRepository, event_bus: EventBus):
        self.accountRepository = accountRepository
        self.customerRepository = customerRepository
        self.event_bus = event_bus


    def execute(self, idAccount, customer_id):
        account = Account.create(idAccount, customer_id)
        self.accountRepository.save(account)
        self.event_bus.publish(account.get_all_domain_event())
