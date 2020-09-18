"""Url Account API module"""

#Django
from django.urls import path, include

from .views import (
    RegisterNewAccountController,
    DepositFundController,
    WithdrawController,
    CloseAccountController,    
)

urlpatterns = [
    path('account', RegisterNewAccountController.as_view(), name='register_new_account'),
    path('deposit', DepositFundController.as_view(), name='deposit_fund'),
    path('withdraw', WithdrawController.as_view(), name='withdraw'),
    path('account/close', CloseAccountController.as_view(), name='close_account')
]