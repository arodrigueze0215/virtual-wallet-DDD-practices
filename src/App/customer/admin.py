from django.contrib import admin

# Register your models here.
from .models import Customer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customer Admin model
    """
    list_display = ('customer_id', 'user', 'person_number', 'phone_number')