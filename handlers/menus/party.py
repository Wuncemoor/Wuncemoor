from enums.game_states import MenuStates


class Party:
    def __init__(self, hero):
        self.p1 = hero
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.superstate = MenuStates.PARTY
        self.options = []
        self.inventory = None
        self.focus = None

    def members(self):
        party = [member for member in (self.p1, self.p2, self.p3, self.p4) if member is not None]
        return party
