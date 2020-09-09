from src.core.domain.customer.customer import Customer
from src.core.domain.customer.name import Name
from src.core.domain.customer.contact_number import ContactNumber
from src.core.domain.customer.person_number import PersonNumber
from src.core.domain.customer.repository import CustomerRepository
class RegisterNewCustomer():
    def __init__(self, customerRepository: CustomerRepository):
        self.customerRepository = customerRepository

    def execute(self, **args):
        idCustomer = args.get('customer_id')
        fullName = Name.create(args.get('first_name'), args.get('last_name'))
        contactNumber = ContactNumber.create(args.get('contact_number'))
        personNumber = PersonNumber.create(args.get('person_number'))
        customer = Customer.create(idCustomer, fullName, personNumber, contactNumber)
        self.customerRepository.save(customer)