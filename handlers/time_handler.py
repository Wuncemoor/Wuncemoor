class TimeHandler:

    def __init__(self, observers):
        self.observers = observers
        self.year = -65
        self.month = 1
        self.day = 1
        self.hour = 6

    def goes_on(self):
        for party in self.observers:
            for member in party.members:
                member.age.become_older([0, 0, 0, 1])
        self.hour += 1
        self.new_day()

    def new_day(self):
        if self.hour > 23:
            self.hour -= 24
            self.day += 1
            self.new_month()

    def new_month(self):
        if self.day > 30:
            self.day -= 30
            self.month += 1
            self.new_year()

    def new_year(self):
        if self.month > 12:
            self.month -= 12
            self.year += 1

    def travel(self, time):
        self.year += time[0]
        self.month += time[1]
        self.new_year()
        self.day += time[2]
        self.new_month()
        self.hour += time[3]
        self.new_day()

    def apply_dilation(self, dungeon):
        for dmap in dungeon.maps:
            for entity in dmap.entities:
                if entity.age:
                    diff = map(lambda x, y: x - y, self.stamp(), dungeon.time_dilation)
                    entity.age.become_older(list(diff))
            for noncom in dmap.noncombatants:
                if noncom.age:
                    diff = map(lambda x, y: x - y, self.stamp(), dungeon.time_dilation)
                    noncom.age.become_older(list(diff))

    def stamp(self):
        return [self.year, self.month, self.day, self.hour]