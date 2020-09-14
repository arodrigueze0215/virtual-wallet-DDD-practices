import unittest
from src.core.domain.exceptions import DontAllowWithdawMoreThanExistingFunds
from src.core.domain.customer.name import Name
from src.core.domain.customer.contact_number import ContactNumber
from src.core.domain.customer.person_number import PersonNumber
from src.core.domain.customer.customer import Customer
from src.core.domain.account.account import Account
from src.core.infrastructure.repository_in_memory.account_repository import AccountRepository
from src.core.infrastructure.repository_in_memory.customer_repository import CustomerRepository
from src.core.use_case.customer.register_new_customer import RegisterNewCustomer
from src.core.use_case.account.register_new_account import RegisterNewAccount
from src.core.use_case.account.deposit_fund_in_account import DepositFundInAccount
from src.core.use_case.account.withdraw_fund import WithDrawFund
from src.core.use_case.account.close_account import CloseAccount
from src.core.use_case.account.get_account_details import GetAccountDetails

class TestUseCaseRegisterNewAccount(unittest.TestCase):

    def setUp(self):
        self.accountRepository = AccountRepository()
        self.customerRepository = CustomerRepository()
        self.registerNewAccount = RegisterNewAccount(self.accountRepository, self.customerRepository)
        self.registerNewCustomer = RegisterNewCustomer(self.customerRepository)
        self.idAccount = 1

    def test_customer_could_register_new_checking_account_with_personal_details(self):
        self._given_created_customer()
        self._when_customer_register_new_account()
        self._then_save_the_new_account_in_repository()

    def _given_created_customer(self):
        self.customer_id = 1
        self.registerNewCustomer.execute(
            customer_id = self.customer_id,
            first_name = 'Andres',
            last_name = 'Rodriguez',
            contact_number = '3112673404',
            person_number = '1088997602'
        )

    def _when_customer_register_new_account(self):
        self.registerNewAccount.execute(self.idAccount, self.customer_id)

    def _then_save_the_new_account_in_repository(self):
        account = self.accountRepository.findById(self.idAccount)
        self.assertEqual(account.id, self.idAccount)

class TestUseCaseDepositFundExistingAccount(unittest.TestCase):
    """Allow a customer to deposit funds into an existing account."""

    def setUp(self):
        self.accountRepository = AccountRepository()
        self.depositFundInAccount = DepositFundInAccount(self.accountRepository)
    
    def test_allow_customer_deposit_funds_an_existing_account(self):
        self._given_created_customer()
        self._given_an_existing_account()
        self._when_deposit_fund_into_account()
        self._then_verify_whether_account_has_balance()        

    def _given_created_customer(self):
        idCustomer = 1
        fullName = Name.create("Andres", "Rodriguez")
        contactNumber = ContactNumber.create('3102434466')
        personNumber = PersonNumber.create('10888999602')
        self.customer = Customer.create(idCustomer, fullName, personNumber, contactNumber)
    
    def _given_an_existing_account(self):
        self.idAccount = 1
        idCustomer = 1
        self.account = Account.create(self.idAccount, idCustomer)
        self.accountRepository.save(self.account)
    
    def _when_deposit_fund_into_account(self):
        amount = 100
        description = 'A deposit of 100'
        self.depositFundInAccount.execute(self.idAccount, amount, description)
    
    def _then_verify_whether_account_has_balance(self):
        account = self.accountRepository.findById(self.account.id)
        self.assertEqual(account.balance, 100)

class TestUseCaseCustomerWithdrawFundsExistingAccount(unittest.TestCase):
    """Allow the customer to withdraw funds from an existing account."""

    def setUp(self):
        self.accountRepository = AccountRepository()
        self.withdrawFund = WithDrawFund(self.accountRepository)

    def test_allow_the_customer_to_withdraw_funds_from_an_existing_account(self):
        self._given_an_existing_account()
        self._when_customer_withdraw_from_existing_account()
        self._then_verify_whether_account_has_balance()
    
    def _given_an_existing_account(self):
        idAccount = 1
        idCustomer = 1
        self.account = Account.create(idAccount, idCustomer)
        self.account.makeCredit(300, 'A deposit of 300')

    def _when_customer_withdraw_from_existing_account(self):
        amount = 10
        description = 'A withdraw of 10 from ATM'
        self.withdrawFund.execute(self.account, amount, description)

    def _then_verify_whether_account_has_balance(self):
        account = self.accountRepository.findById(self.account.id)
        self.assertEqual(account.balance, 290)

class TestUseCaseAllowCustomerToCloseAccountIfBalanceIsZero(unittest.TestCase):

    def setUp(self):
        self.accountRepository = AccountRepository()
        self.closeAccount = CloseAccount(self.accountRepository)
        self._given_a_deposit_funds()

    def test_allow_the_customer_to_close_a_Checking_Account_only_if_the_balance_is_zero(self):        
        self._given_a_300_withdraw_funds()
        self._when_customer_tries_close_account()
        self._then_varify_is_closed_account_status()

    def test_allow_the_customer_to_close_a_Checking_Account_with_balance(self):
        self._given_a_200_withdraw_funds()
        self._when_customer_tries_close_account_with_an_existing_balance()
        self._then_varify_is_not_closed_account_status()
    
    def _given_a_deposit_funds(self):
        idAccount = 1
        idCustomer = 1
        self.account = Account.create(idAccount, idCustomer)
        self.account.makeCredit(300, 'A deposit of 300')

    def _given_a_300_withdraw_funds(self):
        self.account.withDraw(300, 'A withdraw of 300 from ATM')
    
    def _given_a_200_withdraw_funds(self):
        self.account.withDraw(200, 'A withdraw of 200 from ATM')

    def _when_customer_tries_close_account(self):
        self.closeAccount.execute(self.account)

    def _when_customer_tries_close_account_with_an_existing_balance(self):
        self.closeAccount.execute(self.account)

    def _then_varify_is_closed_account_status(self):
        isClosed = self.accountRepository.isClosed(self.account.id)
        self.assertEqual(isClosed, True)

    def _then_varify_is_not_closed_account_status(self):
        isClosed = self.accountRepository.isClosed(self.account.id)
        self.assertEqual(isClosed, False)

class TestUseCaseDontAllowWithdrawMorThanExistingFunds(unittest.TestCase):
    def setUp(self):
        self.accountRepository = AccountRepository()
        self.withdrawFund = WithDrawFund(self.accountRepository)

    def test_do_not_allow_the_Customer_to_Withdraw_more_than_the_existing_funds(self):
        self._given_an_existing_account()
        self._when_customer_withdraw_from_existing_account()
    
    def _given_an_existing_account(self):
        idAccount = 1
        idCustomer = 1
        self.account = Account.create(idAccount, idCustomer)
        self.account.makeCredit(300, 'A deposit of 300')

    def _when_customer_withdraw_from_existing_account(self):
        amount = 400
        description = 'A withdraw of 400 from ATM'
        with self.assertRaises(DontAllowWithdawMoreThanExistingFunds):
            self.withdrawFund.execute(self.account, amount, description)

class TestUseCaseAllowGetAccountDetails(unittest.TestCase):
    def setUp(self):
        self.accountRepository = AccountRepository()
        self.getAccountDetails = GetAccountDetails(self.accountRepository)

    def test_get_account_details(self):
        self._given_an_existing_account()
        idAccount = 1
        account_detail = self.getAccountDetails.execute(idAccount)
        self.assertEqual(account_detail.id, idAccount)

    def _given_an_existing_account(self):
        idAccount = 1
        idCustomer = 1
        account = Account.create(idAccount, idCustomer)
        account.makeCredit(300, 'A deposit of 300')
        self.accountRepository.save(account)


class TestUseAllowGetCustomerDetails(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
