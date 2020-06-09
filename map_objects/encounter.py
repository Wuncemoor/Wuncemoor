from enums.game_states import EncounterStates
from map_objects.loot import Loot

class Encounter:

    def __init__(self, background, event, options):
        self.background = background
        self.event = event
        self.options = options
        self.current_option = 0
        self.state = EncounterStates.THINKING
        self.loot = Loot()

    def add_loot(self, dead_entity):
        self.loot.items.extend(dead_entity.combatant.inventory.items)



