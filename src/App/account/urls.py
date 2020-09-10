"""Url Account API module"""

#Django
from django.urls import path, include

from .views import RegisterNewAccountController

urlpatterns = [
    path('', RegisterNewAccountController.as_view())
]