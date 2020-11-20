from src.core.use_case.account.increase_balance_account import IncreaseBalanceAccount
from src.core.share.event_driven.event_bus import EventBus
from src.core.share.event_driven.subscriptions_handle import SubscriptionHandle
class  AfterFundWasDeposited(SubscriptionHandle):
    """
     The Main task of this class is to launch the execute method after Account
     was created
    """
    FUND_WAS_DEPOSITED = 'FundWasDeposited'
    def __init__(self, increase_balance_account: IncreaseBalanceAccount, event_bus: EventBus, **kargs):
        super().__init__(AfterFundWasDeposited.FUND_WAS_DEPOSITED, event_bus)
        self.increase_balance_account = increase_balance_account
        self.kargs = kargs

    def execute(self):
        account_id = self.kargs.get('account_id')
        self.increase_balance_account.execute(account_id)