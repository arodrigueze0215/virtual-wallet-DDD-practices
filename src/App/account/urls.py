"""Url Account API module"""

#Django
from django.urls import path, include

from .views import (RegisterNewAccountController, DepositFundController)

urlpatterns = [
    path('account', RegisterNewAccountController.as_view(), name='register_new_account'),
    path('deposit', DepositFundController.as_view(), name='deposit_fund')
]