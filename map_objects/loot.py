
class Loot:

    def __init__(self):
        self.xp = 0
        self.items = []
        self.claimed = []

    def add_loot(self, dead_entity):
        self.items.extend(dead_entity.combatant.satchel.items)
        self.items.extend(dead_entity.combatant.equipment.drop_dead())

    def reset(self):
        self.xp = 0
        self.items = []
        self.claimed = []
