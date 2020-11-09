class Age:
    """Component for Entities to get older"""

    def __init__(self, year, month, day, hour, birthday):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.birthday = birthday

    def become_older(self, diff):
        year, month, day, hour = diff

        self.year += year
        self.month += month
        self.day += day
        self.hour += hour

        if self.hour < 0:
            self.hour += 24
            self.day -= 1
        if self.day < 0:
            self.day += 30
            self.month -= 1
        if self.month < 0:
            self.month += 12
            self.year -= 1

        while self.hour > 23:
            self.day += 1
            self.hour -= 24
        while self.day > 30:
            self.month += 1
            self.day -= 30
        while self.month > 12:
            self.year += 1
            self.month -= 12
