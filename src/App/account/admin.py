"""Account model Admin"""
#Django
from django.contrib import admin

#Models
from .models import (
    Account,
    Credit,
    Debit
)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Account Admin model """
    list_display = ('customer', 'account_id','status', 'balance', 'opening_date')
@admin.register(Credit)
class Credit(admin.ModelAdmin):
    """ Credit Admin model"""
    list_display = ('account', 'ammount', 'transaction_date', 'description')

@admin.register(Debit)
class Debit(admin.ModelAdmin):
    """ Credit Admin model"""
    list_display = ('account', 'ammount', 'transaction_date', 'description')




