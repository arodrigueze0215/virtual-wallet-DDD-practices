class ContactNumber():
    """Name Value Object."""

    def __init__(self, phone_number):
        self.phone_number = phone_number

    @staticmethod
    def create(phone_number):
        contactNumber = ContactNumber(phone_number)
        return contactNumber
