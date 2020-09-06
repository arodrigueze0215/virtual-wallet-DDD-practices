
#Core
from src.core.domain.customer.customer import Customer
from src.core.domain.customer.name import Name
from src.core.domain.customer.contact_number import ContactNumber
from src.core.domain.customer.person_number import PersonNumber

class CustomerRepository():
    
    def __init__(self):
        self.store = {}

    def findById(self, customer_id):
        """This return a Customer object that was found by ID from store"""
        return self.store[customer_id]


    def save(self, customer: Customer):
        self.store[customer.idCustomer] = customer