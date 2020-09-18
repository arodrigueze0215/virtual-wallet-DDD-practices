
from datetime import date
from django.contrib.auth.models import User
from customer.models import Customer
from account.models import (
    Account,
    Debit,
    Credit,
)
def customer_db_mother(**args):
    user = User.objects.create_user(
        username='any_username' if args.get('username') == None else args.get('username'),
        first_name='any_first_name' if args.get('first_name') == None else args.get('first_name'),
        last_name='any_last_name' if args.get('last_name') == None else args.get('last_name')
    )
    customer = Customer.objects.create(
        customer_id='100',
        user=user,
        person_number='111222333',
        phone_number= '888777222'
    )
    return customer

def account_db_mother(customer: Customer, **args):
    return Account.objects.create(
        account_id= '100' if args.get('account_id') == None else args.get('account_id'),
        customer = customer,
        balance = 0 if args.get('balance') == None else args.get('balance'),
        opening_date = date.today() if args.get('opening_date') == None else args.get('opening_date')
    )

def credit_db_mother(account_db:Account, **args):
    Credit.objects.create(
        account=account_db,
        ammount= 0 if args.get('amount') == None else args.get('amount'),
        transaction_date = date.today() if args.get('transaction_date') == None else args.get('transaction_date'),
        description = '' if args.get('description') == None else args.get('description')
    )

def debit_db_mother(account_db:Account, **args):
    Debit.objects.create(
        account=account_db,
        ammount= 0 if args.get('amount') == None else args.get('amount'),
        transaction_date = date.today() if args.get('transaction_date') == None else args.get('transaction_date'),
        description = '' if args.get('description') == None else args.get('description')
    )
