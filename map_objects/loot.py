
class Loot:

    def __init__(self):
        self.xp = 0
        self.items = []
        self.claimed = []

    def reset(self):
        self.xp = 0
        self.items = []
        self.claimed = []

    def dissect(self, dead_entity):
        self.xp += dead_entity.combatant.xp
        self.items.extend(dead_entity.combatant.satchel.items)
        self.items.extend(dead_entity.combatant.equipment.drop_dead())
