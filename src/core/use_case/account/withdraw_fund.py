from src.core.domain.account.account import Account
class WithDrawFund(object):
    def __init__(self, accountRepository):
        self.accountRepository = accountRepository


    def execute(self, account: Account, amount, description):
        account.withDraw(amount, description)
        self.accountRepository.save(account)