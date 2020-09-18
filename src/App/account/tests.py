#Django
from django.urls import reverse
from django.contrib.auth.models import User

# Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

#models
from .models import Account
from customer.models import Customer

#Exceptions
from .exceptions import WithdawMoreThanExistingFunds

#utils
from uilts.objects_mother import (
    customer_db_mother,
    account_db_mother,
    debit_db_mother,
    credit_db_mother,
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
        self._given_an_existing_account_with_balance_1000('123')
        self._when_customer_withdraw_from_existing_account()
        self._then_verify_whether_account_has_updated_balance()

    def test_do_not_allow_the_Customer_to_Withdraw_more_than_the_existing_funds(self):
        self._given_an_existing_account_with_balance_1000('2')
        self._when_customer_withdraw_more_than_existing_funds()
        self._then_raise_exception_denying_the_withdraw()


    def _given_an_existing_account_with_balance_1000(self, account_id):
        customer = customer_db_mother(first_name='Andressito')
        account_db_mother(customer, balance=1000, account_id=account_id)


    def _when_customer_withdraw_from_existing_account(self):
        url = reverse('withdraw')
        data = {
            'account_id': '123',
            'amount': 100,
            'description': 'A withdraw of 100'
        }
        self.response = self.client.post(url, data, format='json')

    def _when_customer_withdraw_more_than_existing_funds(self):
        url = reverse('withdraw')
        data = {
            'account_id': '2',
            'amount': 1200,
            'description': 'A withdraw of 1200'
        }
        self.response = self.client.post(url, data, format='json')    
        
    def _then_verify_whether_account_has_updated_balance(self):
        account = Account.objects.get(account_id='123')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(account.balance, 900)

    def _then_raise_exception_denying_the_withdraw(self):
        self.assertRaises(WithdawMoreThanExistingFunds)
        self.assertEqual(self.response.status_code, status.HTTP_406_NOT_ACCEPTABLE)


class TestUseCaseAllowCustomerToCloseAccountIfBalanceIsZero(APITestCase):

    def test_dont_allow_the_customer_to_close_a_Checking_Account_only_if_it_has_balance(self):        
        self._given_an_account_with_balance()
        self._when_customer_tries_close_account('1')
        self._then_varify_is_still_account_opened()

    def test_allow_the_customer_to_close_a_Checking_Account_only_if_it_has_balance_zero(self):
        self._given_an_account_without_balance()
        self._when_customer_tries_close_account('2')
        self._then_varify_is_account_closed()


    def _given_an_account_without_balance(self):
        customer = customer_db_mother()
        self.account = account_db_mother(customer, account_id='2', balance=0)
    
    def _given_an_account_with_balance(self):
        customer = customer_db_mother()
        self.account = account_db_mother(customer, account_id='1', balance=500)

    def _when_customer_tries_close_account(self, account_id):
        url = reverse('close_account')
        data = { 'account_id': account_id }
        self.response = self.client.post(url, data, format='json')
    
    def _then_varify_is_still_account_opened(self):
        account = Account.objects.get(account_id='1')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(account.balance, 500)
        self.assertEqual(account.status, '1')

    def _then_varify_is_account_closed(self):
        account = Account.objects.get(account_id='2')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.status, '0')