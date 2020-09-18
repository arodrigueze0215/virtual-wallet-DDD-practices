import sys
sys.path.insert(1, '/Users/arodriguez/personal_projects/virtual-wallet-DDD-practices')
#Django rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#core
from src.core.infrastructure.repository.account_repository import AccountRepository
from src.core.use_case.account.register_new_account import RegisterNewAccount
from src.core.use_case.customer.register_new_customer import RegisterNewCustomer
from src.core.infrastructure.repository.customer_repository import CustomerRepository
from src.core.use_case.account.deposit_fund_in_account import DepositFundInAccount
from src.core.use_case.account.withdraw_fund import WithDrawFund

class RegisterNewAccountController(APIView):
    """Controller that let register a new Account"""


    def __init__(self):        
        self.accountRepository = AccountRepository()
        self.customerRepository = CustomerRepository()
        self.registerNewAccount = RegisterNewAccount(self.accountRepository, self.customerRepository)
        self.registerNewCustomer = RegisterNewCustomer(self.customerRepository)

    def post(self, request, format=None):
        customer_id = request.data.get('customer_id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        contact_number = request.data.get('contact_number')
        person_number = request.data.get('person_number')
        account_id = (request.data.get('account_id'))
        self.registerNewCustomer.execute(
            customer_id = customer_id,
            first_name = first_name,
            last_name = last_name,
            contact_number = contact_number,
            person_number = person_number
        )
        # Repositorio deberia ir en el execute del register new account
        self.registerNewAccount.execute(account_id, customer_id)
        return Response(status=status.HTTP_201_CREATED)

class DepositFundController(APIView):
    """Api controller to deposit a fund on an account"""

    def __init__(self):
        self.accountRepository = AccountRepository()
        self.depositFundInAccount = DepositFundInAccount(self.accountRepository)

    def post(self, request, format=None):
        account_id = request.data.get('account_id')
        amount = request.data.get('amount')
        description = request.data.get('description')
        self.depositFundInAccount.execute(account_id, amount=amount, description=description)
        return Response(status=status.HTTP_200_OK)

class WithdrawController(APIView):

    def __init__(self):
        self.accountRepository = AccountRepository()
        self.withDraw = WithDrawFund(self.accountRepository)

    def post(self, request, format=None):
        account_id = request.data.get('account_id')
        amount = request.data.get('amount')
        description = request.data.get('description')
        self.withDraw.execute(account_id,amount,description)
        return Response(status=status.HTTP_200_OK)

