from src.core.use_case.customer.register_new_customer import RegisterNewCustomer
from src.core.share.event_driven.event_bus import EventBus
from src.core.share.event_driven.subscriptions_handle import SubscriptionHandle
class  AfterAccountWasCreated(SubscriptionHandle):
    """
     The Main task of this class is to launch the execute method after Account
     was created
    """
    ACCOUNT_WAS_CREATED = 'AccountWasCreated'
    def __init__(self, register_new_customer: RegisterNewCustomer, event_bus: EventBus, **kargs):
        super().__init__(AfterAccountWasCreated.ACCOUNT_WAS_CREATED, event_bus)
        self.register_new_customer = register_new_customer
        self.kargs = kargs

    def execute(self):
        self.register_new_customer.execute(
            customer_id = self.kargs.get('customer_id'),
            first_name = self.kargs.get('first_name'),
            last_name = self.kargs.get('last_name'),
            contact_number = self.kargs.get('contact_number'),
            person_number = self.kargs.get('person_number')
        )