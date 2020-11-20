from src.core.domain.customer.customer import Customer
from src.core.domain.transaction.credit import Credit
from src.core.domain.transaction.credit_repository import CreditRepository
from src.core.share.event_driven.event_bus import EventBus
class DepositFundInAccount(object):

    def __init__(self, creditRepository:CreditRepository, event_bus: EventBus):
        self.creditRepository = creditRepository
        self.event_bus = event_bus

    def execute(self, idAccount, amount, description):
        deposit = Credit.makeCredit(idAccount, amount, description)
        self.creditRepository.save(deposit)
        self.event_bus.publish(deposit.get_all_domain_event())