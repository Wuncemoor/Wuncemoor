from enums.game_states import GameStates
from handlers.logic.logic_chunks import NewGame, LoadGame, QuitGame


class OptionsHandler:
    def __init__(self):
        self.title = self.title_options()

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
        if (amount < 0 and self.mapping.choice == 0) or (amount > 0 and self.mapping.choice >=
                                                         (len(self.mapping.options) - 1)):
            pass
        else:
            self.mapping.choice += amount

    def choose(self):
        state = self.mapping
        option = state.options[state.choice]

        return option.logic

    @staticmethod
    def title_options():
        options = Options([NewGame, LoadGame, QuitGame])
        return options


class Options:
    def __init__(self, options):
        self.options = options
        self.choice = 0
