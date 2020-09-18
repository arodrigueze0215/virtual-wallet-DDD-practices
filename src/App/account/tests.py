#Django
from django.urls import reverse
from django.contrib.auth.models import User

# Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

#models
from .models import Account
from customer.models import Customer

#utils
from uilts.objects_mother import (
    customer_db_mother,
    account_db_mother,
)


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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestUseCaseDepositFundExistingAccount(APITestCase):
    """Allow a customer to deposit funds into an existing account."""

    def test_api_allow_customer_deposit_funds_an_existing_account(self):

        self._given_created_customer()
        self._given_an_existing_account()
        self._when_deposit_fund_into_account()
        self._then_verify_whether_the_account_got_deposit()

    def _given_created_customer(self):
        self.customer = customer_db_mother()

    def _given_an_existing_account(self):
        account_db_mother(self.customer)

    
    def _when_deposit_fund_into_account(self):
        url = reverse('deposit_fund')
        data = {
            'account_id': '100',
            'amount': 100,
            'description': 'A deposit of 100'
        }
        self.response = self.client.post(url, data, format='json')
        

    
    def _then_verify_whether_the_account_got_deposit(self):
        account = Account.objects.get(account_id='100')

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(account.balance, 100)

class TestUseCaseCustomerWithdrawFundsExistingAccount(APITestCase):

    
    def test_allow_the_customer_to_withdraw_funds_from_an_existing_account(self):
        self._given_an_existing_account_with_balance_100()
        self._when_customer_withdraw_from_existing_account()
        self._then_verify_whether_account_has_updated_balance()

    def _given_an_existing_account_with_balance_100(self):
        customer = customer_db_mother(first_name='Andressito')
        account_db_mother(customer, balance=1000, account_id='123')


    def _when_customer_withdraw_from_existing_account(self):
        url = reverse('withdraw')
        data = {
            'account_id': '123',
            'amount': 100,
            'description': 'A withdraw of 100'
        }
        self.response = self.client.post(url, data, format='json')
    
        
    def _then_verify_whether_account_has_updated_balance(self):
        account = Account.objects.get(account_id='123')
        print('account', account)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(account.balance, 900)


