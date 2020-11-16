import unittest
from unittest.mock import MagicMock

#core
from src.core.infrastructure.subscribers.after_account_was_created import AfterAccountWasCreated
from src.core.use_case.customer.register_new_customer import RegisterNewCustomer
from src.core.infrastructure.repository_in_memory.customer_repository import CustomerRepository
from src.core.infrastructure.repository_in_memory.account_repository import AccountRepository
from src.core.use_case.account.register_new_account import RegisterNewAccount

#share
from src.core.share.event_driven.event_bus import EventBus
class TestLaunchAccountWasCreatedEventDomain(unittest.TestCase):
    """
    Unit Test for launch AccountWasCreated Domain Event
    """
    def test_launch_account_was_created_domain_event(self):
        accountRepository = AccountRepository()
        customer_repository = CustomerRepository()
        event_bus = EventBus()
        registerNewAccount = RegisterNewAccount(accountRepository, customer_repository, event_bus)
        register_newCustomer = RegisterNewCustomer(customer_repository)
        idAccount = 1
        customer_id = 1
        after_account_was_created = AfterAccountWasCreated(register_newCustomer, event_bus, 
            customer_id = customer_id,
            first_name = 'Andres',
            last_name = 'Rodriguez',
            contact_number = '3112673404',
            person_number = '1088997602')
        after_account_was_created()
        registerNewAccount.execute(idAccount, customer_id)

        customer = customer_repository.findById(1)
        self.assertEquals(customer.idCustomer, 1)
