
#Core
from src.core.domain.customer.customer import Customer
from abc import ABCMeta

class CustomerRepository(metaclass=ABCMeta):    

    def findById(self, customer_id):
        pass

    def save(self, customer: Customer):
        pass