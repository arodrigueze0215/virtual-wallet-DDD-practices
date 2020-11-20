from src.core.domain.account.account import Account
from src.core.domain.transaction.debit import Debit
from src.core.domain.account.repository import AccountRepository
from src.core.domain.transaction.debit_repository import DebitRepository

#Share
from src.core.share.event_driven.event_bus import EventBus
class WithDrawFund(object):
    def __init__(self, debit_repository: DebitRepository, event_bus:EventBus):
        self.debit_repository = debit_repository
        self.event_bus = event_bus


    def execute(self, account_id, amount, description):
        debit = Debit.withDraw(account_id, amount, description)
        self.debit_repository.save(debit)
        self.event_bus.publish(debit.get_all_domain_event())