class Age:
    """Component for Entities to get older"""

    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    @property
    def birthday(self):
        if self.month == 0:
            m = 1
        else:
            m = 13 - self.month
        if self.day == 0:
            d = 1
        else:
            d = 31 - self.day
        return m, d

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
