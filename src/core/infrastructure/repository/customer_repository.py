import uuid

#Django 
from django.contrib.auth.models import User

#models
from model.models import Customer as CustomerDb

#Core
from src.core.domain.customer.customer import Customer
from src.core.domain.customer.name import Name
from src.core.domain.customer.contact_number import ContactNumber
from src.core.domain.customer.person_number import PersonNumber

class CustomerRepository():
    
    def __init__(self):
        pass

    def findById(self, customer_id):
        """This return a Customer object that was found by ID from de DB"""
        customer_db = CustomerDb.objects.get(customer_id=customer_id)
        if customer_db == None:
            return None
        idCustomer = customer_db.customer_id
        fullName = Name.create(customer_db.user.first_name, customer_db.user.last_name)
        contactNumber = ContactNumber.create(customer_db.phone_number)
        personNumber = PersonNumber.create(customer_db.person_number)
        customer = Customer.create(idCustomer, fullName, personNumber, contactNumber)

        return customer

    def getCustomerDBObject(self, customer_id):
        """This return a Customer DB object that was found by ID from de DB"""
        customer_db = CustomerDb.objects.get(customer_id=customer_id)
        if customer_db == None:
            return None

        return customer_db

    def save(self, customer):
        customer_id = customer.idCustomer
        first_name = customer.name.name
        last_name = customer.name.last_name
        username = f'{first_name}.{last_name}_{uuid.uuid4()}'
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        customer_db = CustomerDb()
        customer_db.customer_id = customer_id
        customer_db.user = user
        customer_db.person_number = customer.person_number.person_number
        customer_db.contact_number = customer.contact_number.phone_number
        customer_db.save()