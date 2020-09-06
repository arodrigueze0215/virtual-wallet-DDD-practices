class PersonNumber():
    """Name Value Object."""

    def __init__(self, person_number):
        self.person_number = person_number

    @staticmethod
    def create(person_number):
        personNumber = PersonNumber(person_number)
        return personNumber

    def __str__(self):
        return f'{self.person_number}'
