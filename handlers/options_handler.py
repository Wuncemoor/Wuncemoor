from enums.game_states import GameStates
from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables


class OptionsHandler:
    def __init__(self):
        self.title = Options(['Start A New Game', 'Continue Previous Game', 'Quit'])

    @property
    def mapping(self):
        state = self.owner.state
        maps = {
            GameStates.TITLE: self.title,
            # GameStates.LIFE: self.life,
            # GameStates.ENCOUNTER: self.encounter,
            # GameStates.DIALOGUE: self.dialogue,
            # GameStates.MENUS: self.menus,
            # GameStates.REWARD: self.loot,
            # GameStates.SHOW_MAP: self.map,
        }
        return maps.get(state)

    def traverse(self, amount):
        print(amount)
        print(self.mapping)
        if (amount < 0 and self.mapping.choice == 0) or (amount >= len(self.mapping.options)):
            pass
        else:
            self.mapping.choice += amount

    def choose(self):
        state = self.mapping
        choice = self.mapping.choice
        if choice == 0:
            dungeons, world, overworld_tiles, party = get_game_variables()
            self.owner.preplay(dungeons, world, overworld_tiles, party)
        elif choice == 1:
            dungeons, world, overworld_tiles, party = load_game()
            self.owner.preplay(dungeons, world, overworld_tiles, party)
        elif choice == 2:
            self.owner.quit()


class Options:
    def __init__(self, options):
        self.options = options
        self.choice = 0

class Option:
    def __init__(self):
