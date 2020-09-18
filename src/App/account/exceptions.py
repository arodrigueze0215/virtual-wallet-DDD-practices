"""Account Exceptions"""

#rest framework
from rest_framework.exceptions import APIException
from rest_framework import status

#Core
from src.core.domain.exceptions import DontAllowWithdawMoreThanExistingFunds

class WithdawMoreThanExistingFunds(DontAllowWithdawMoreThanExistingFunds, APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = 'Dont allow withdaw more than existing Funds.'
    default_code = 'DontAllowWithdawMoreThanExistingFunds'
