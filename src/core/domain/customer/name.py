class Name(object):
    """Name Value Object."""

    def __init__(self,name, last_name):
        self.name = name
        self.last_name = last_name

    @staticmethod
    def create(name, last_name):
        name = Name(name, last_name)
        return name

    def __str__(self):
        return f'{self.name}, {self.last_name}'