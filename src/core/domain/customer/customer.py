from src.core.domain.customer.name import Name
from src.core.domain.customer.contact_number import ContactNumber
from src.core.domain.customer.person_number import PersonNumber
class Customer(object):
    
    def __init__(self, idCustomer, name: Name, personNumber: PersonNumber, contactNumber: ContactNumber):
        self.idCustomer = idCustomer
        self.name = name
        self.person_number = personNumber
        self.contact_number = contactNumber

    @staticmethod
    def create(idCustomer, name: Name, personNumber: PersonNumber, contactNumber: ContactNumber):
        """create a customer object and then return the instance"""
        customer = Customer(idCustomer, name, personNumber, contactNumber)
        return customer

    def __str__(self):
        return f'{self.idCustomer}, {self.name}, {self.person_number}'