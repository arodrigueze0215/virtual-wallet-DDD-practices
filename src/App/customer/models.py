import uuid

#Django
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    customer_id = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_number = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.get_full_name()}'

    @property
    def customer_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
