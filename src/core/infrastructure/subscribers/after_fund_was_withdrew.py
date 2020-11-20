from src.core.use_case.account.decrease_balance_account import DecreaseBalanceAccount
from src.core.share.event_driven.event_bus import EventBus
from src.core.share.event_driven.subscriptions_handle import SubscriptionHandle
class  AfterFundWasWithDrew(SubscriptionHandle):
    """
     The Main task of this class is to launch the execute method after Account
     was created
    """
    FUND_WAS_DEPOSITED = 'FundWasWithDrew'
    def __init__(self, decrease_balance_account: DecreaseBalanceAccount, event_bus: EventBus, **kargs):
        super().__init__(AfterFundWasWithDrew.FUND_WAS_DEPOSITED, event_bus)
        self.decrease_balance_account = decrease_balance_account
        self.kargs = kargs

    def execute(self):
        account_id = self.kargs.get('account_id')
        self.decrease_balance_account.execute(account_id)