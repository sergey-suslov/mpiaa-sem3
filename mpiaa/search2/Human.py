class Human:
    def __init__(self, first_name, last_name, day, month, year):
        self.first_name = first_name
        self.last_name = last_name
        self.day = day
        self.age = str(2016 - int(year))
        self.month = month
        self.year = year

