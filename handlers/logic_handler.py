from enums.game_states import GameStates
from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables


class LogicHandler:

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

    def translate(self, output):
        self.mapping(output)

    def title(self, output):
        options = self.owner.options

        if 'traverse_menu' in output:
            options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            options.choose()
