from enums.game_states import MenuStates


class Party:
    def __init__(self, hero):
        self.superstate = MenuStates.PARTY
        self.p1 = hero
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.options = None
        self.inventory = None
        self.map = None
        self.focus = None
        self.x = None
        self.y = None
        self.sub = None
        self.formation = 'Unorganized'
        self.move_speed = 'Normal'
        self.rations = 'None'


    @property
    def member_slots(self):
        slots = [self.p1, self.p2, self.p3, self.p4]
        return slots
    @property
    def members(self):
        party = [member for member in (self.p1, self.p2, self.p3, self.p4) if member is not None]
        return party

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def remove(self, entity):
        if self.p1 is entity:
            self.p1 = None
        elif self.p2 is entity:
            self.p2 = None
        elif self.p3 is entity:
            self.p3 = None
        elif self.p4 is entity:
            self.p4 = None


