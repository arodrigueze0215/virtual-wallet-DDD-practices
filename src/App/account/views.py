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
from src.core.use_case.account.close_account import CloseAccount
from src.core.use_case.account.get_account_details import GetAccountDetails

from .exceptions import WithdawMoreThanExistingFunds

class AccountController(APIView):
    """Controller Account"""


    def __init__(self):        
        self.accountRepository = AccountRepository()
        self.customerRepository = CustomerRepository()
        self.registerNewAccount = RegisterNewAccount(self.accountRepository, self.customerRepository)
        self.registerNewCustomer = RegisterNewCustomer(self.customerRepository)
        self.getAccountDetails = GetAccountDetails(self.accountRepository)

    def get(self, request, format=None):
        account_id = request.query_params.get('id')
        account = self.getAccountDetails.execute(account_id)
        return Response(status=status.HTTP_200_OK)



    def post(self, request, format=None):
        customer_id = request.data.get('customer_id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        contact_number = request.data.get('contact_number')
        person_number = request.data.get('person_number')
        account_id = request.data.get('account_id')
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
        self.depositFundInAccount.execute(account_id, amount=int(amount), description=description)
        return Response(status=status.HTTP_200_OK)

class WithdrawController(APIView):

    def __init__(self):
        self.accountRepository = AccountRepository()
        self.withDraw = WithDrawFund(self.accountRepository)

    def post(self, request, format=None):
        account_id = request.data.get('account_id')
        amount = request.data.get('amount')
        description = request.data.get('description')
        try:
            self.withDraw.execute(account_id, int(amount), description)
            return Response(status=status.HTTP_200_OK)
        except:
            raise WithdawMoreThanExistingFunds
            
            

class CloseAccountController(APIView):
     
    def __init__(self):
        self.accountRepository = AccountRepository()
        self.closeAccount =CloseAccount(self.accountRepository)

    def post(self, request, format=None):
        account_id = request.data.get('account_id')
        self.closeAccount.execute(account_id)
        return Response(status=status.HTTP_200_OK)


