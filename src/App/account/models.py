import uuid

#Django
from django.db import models

#Transaction base model
from .transaction_model import TransactionModel

#Customer model
from customer.models import Customer


class Account(models.Model):
    _STATUS = (
        ('0', 'CLOSED'),
        ('1', 'OPEN'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    account_id = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=_STATUS, default='1')
    balance = models.PositiveIntegerField(default=0)
    opening_date = models.DateField(auto_now=False)

    def __str__(self):
        return f'{self.account_id} {self.customer} {self.status} {self.balance} {self.opening_date}'

    class Meta:
        app_label = 'account'

class Credit(TransactionModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return f'Account: {self.account}, Ammount: {self.ammount}'
