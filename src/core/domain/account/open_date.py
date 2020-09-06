from datetime import date
class OpenDate(object):
    def __init__(self):
        self.date = date.today()

    @staticmethod
    def create():
        openDate = OpenDate()
        return openDate

    def __str__(self):
        return f'{self.date}'
        