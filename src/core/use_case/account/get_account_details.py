class GetAccountDetails():
    def __init__(self, accountRepository):
        self.accountRepository = accountRepository

    def execute(self, idAccount):
        return self.accountRepository.findById(idAccount)