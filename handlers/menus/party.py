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
        self.formation = None

    @property
    def members(self):
        party = [member for member in (self.p1, self.p2, self.p3, self.p4) if member is not None]
        return party

    def move(self, dx, dy):
        self.x += dx
        self.y += dy