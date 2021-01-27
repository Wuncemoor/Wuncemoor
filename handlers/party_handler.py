

class PartyHandler:
    def __init__(self, hero):
        self.p1 = hero
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.char_sheet = None
        self.inventory = None
        self.journal = None
        self.map = None
        self.focus = None
        self.x = None
        self.y = None
        self.direction = (0, 1)
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

    def move(self, dxdy: tuple) -> None:
        self.x += dxdy[0]
        self.y += dxdy[1]

    def teleport(self, go_to_xy: tuple) -> None:
        self.x, self.y = go_to_xy

    def change_direction(self, new_direction):
        if self.direction != new_direction:
            self.direction = new_direction
            for member in self.members:
                member.combatant.images.sprite = member.combatant.images.sprite_dict.get(new_direction)

    def remove(self, entity):
        if self.p1 is entity:
            self.p1 = None
        elif self.p2 is entity:
            self.p2 = None
        elif self.p3 is entity:
            self.p3 = None
        elif self.p4 is entity:
            self.p4 = None