""" Django models utilities"""
import uuid

#Django
from django.db import models

class TransactionModel(models.Model):
    """
    TransactionModel is a base model that acts as an abstract base
    class witch models like credit and debit will inherit. This class provides
    a commons atribures like:
     + ammunt: value of transaction
     + transaction_date: date of transaction
     + description: a short description about transaction

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=False)
    ammount = models.PositiveIntegerField()
    transaction_date = models.DateField(auto_now=False)
    description = models.CharField(max_length=1500)

    class Meta:
        abstract = True
        ordering = ['transaction_date']