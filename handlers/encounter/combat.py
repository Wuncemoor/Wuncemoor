
from builders.mob_builder import MobBuilder, MobDirector
from handlers.menus.party import Party
from misc_functions.mob_chances import MobChances
from misc_functions.random_utils import random_choice_from_dict


class Combat:
    """Created by EncounterHandler at the start of CombatEncounter"""
    def __init__(self, party, tile):
        self.party = party
        self.enemies = self.get_mob_party(tile)
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        grid = CombatGrid()
        if self.party.formation is 'Unorganized':
            grid.rows[3].extend(self.party.members)
        else:
            pass
        if self.enemies.formation is 'Unorganized':
            grid.rows[4].extend(self.enemies.members)
        else:
            pass

        return grid

    def get_mob_party(self, tile):
        mp = Party(self.get_mob(tile))
        return mp

    @staticmethod
    def get_mob(tile):
        mob_chances = MobChances(tile.type, tile.subtype, tile.np)
        mcs = mob_chances.get_mob_chances()
        monster_choice = random_choice_from_dict(mcs)

        mob_builder = MobBuilder(0, monster_choice)
        mob_director = MobDirector()
        mob_director.set_builder(mob_builder)
        mob = mob_director.get_mob()
        return mob

    def destroy(self, entity):
        self.enemies.remove(entity)
        self.grid.remove(entity)


class CombatGrid:
    """Holds combatants in rows, held by Combat"""

    def __init__(self):
        self.rows = [[], [], [], [], [], [], [], []]
        self.x = 4
        self.y = 0

    def remove(self, entity):
        for row in self.rows:
            try:
                row.remove(entity)
            except ValueError:
                pass



