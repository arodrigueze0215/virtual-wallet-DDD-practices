from src.core.domain.account.account import Account
from src.core.domain.account.repository import AccountRepository
class WithDrawFund(object):
    def __init__(self, accountRepository: AccountRepository):
        self.accountRepository = accountRepository


    def execute(self, account_id, amount, description):
        account = self.accountRepository.findById(account_id)
        account.withDraw(amount, description)
        self.accountRepository.addWithdraw(account)