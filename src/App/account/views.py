


import sys
sys.path.insert(1, '/home/arodriguez/projects/virtual-wallet')

#Django rest framework
from rest_framework.views import APIView
from rest_framework.response import Response


#core
from src.core.infrastructure.repository.account_repository import AccountRepository
from src.core.use_case.account.register_new_account import RegisterNewAccount
from src.core.use_case.customer.register_new_customer import RegisterNewCustomer
from src.core.infrastructure.repository.customer_repository import CustomerRepository

class RegisterNewAccountController(APIView):
    """Controller that let register a new Account"""


    def __init__(self):        
        self.accountRepository = AccountRepository()
        self.customerRepository = CustomerRepository()
        self.registerNewAccount = RegisterNewAccount(self.accountRepository)
        self.registerNewCustomer = RegisterNewCustomer(self.customerRepository)

    def post(self, request, format=None):
        customer_id = request.data.get('customer_id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        contact_number = request.data.get('contact_number')
        person_number = request.data.get('person_number')
        account_id = (request.data.get('account_id'))
        print('request.data', request.data)
        self.registerNewCustomer.execute(
            customer_id = customer_id,
            first_name = first_name,
            last_name = last_name,
            contact_number = contact_number,
            person_number = person_number
        )
        # Repositorio deberia ir en el execute del register new account
        costumer = self.customerRepository.findById(customer_id)
        self.registerNewAccount.execute(account_id, costumer)
        return Response()

