
from datetime import date

#Django
from django.urls import reverse
from django.contrib.auth.models import User

# Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

#models
from .models import Account
from customer.models import Customer


class APIAccountTest(APITestCase):
    
    def test_register_new_account(self):
        """
            Test Api to register new Account
        """
        url = reverse('register_new_account')
        data = { 'customer_id':'2',
                 'first_name':'Rafa',
                 'last_name':'Rodriguez',
                 'contact_number':'111',
                 'person_number':'321',
                 'account_id':'2'
            }

        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestUseCaseDepositFundExistingAccount(APITestCase):
    """Allow a customer to deposit funds into an existing account."""

    def test_api_allow_customer_deposit_funds_an_existing_account(self):

        self._given_created_customer()
        self._given_an_existing_account()
        self._when_deposit_fund_into_account()
        self._then_verify_whether_the_account_got_deposit()

    def _given_created_customer(self):
        user = User.objects.create_user(username='any_username', first_name='any_first_name', last_name='any_last_name')
        self.customer = Customer.objects.create(
            customer_id='100',
            user=user,
            person_number='111222333',
            phone_number= '888777222'
        )

    def _given_an_existing_account(self):
        Account.objects.create(
            account_id='100',
            customer = self.customer,
            balance = 0,
            opening_date = date.today()
        )
    
    def _when_deposit_fund_into_account(self):
        url = reverse('deposit_fund')
        data = {
            'account_id': '100',
            'amount': 100,
            'description': 'A deposit of 100'
        }
        self.response = self.client.post(url, data, format='json')
        

    
    def _then_verify_whether_the_account_got_deposit(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)