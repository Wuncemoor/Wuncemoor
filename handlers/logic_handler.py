from enums.game_states import GameStates
from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables


class LogicHandler:

    @property
    def mapping(self):
        state = self.owner.state
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.loot,
            GameStates.SHOW_MAP: self.map,
        }
        return maps.get(state)

    def translate(self, output):
        self.mapping(output)

    def title(self, output):
        traverse_menu = output.get('traverse_menu')
        choose_option = output.get('choose_menu_option')
        handler = self.owner.title

        if traverse_menu:
            if (traverse_menu < 0 and handler.option == 0) or (traverse_menu > 0 and handler.option == 2):
                pass
            else:
                handler.option += traverse_menu
        elif choose_option:
            if handler.option == 0:
                dungeons, world, overworld_tiles, log, party = get_game_variables()
                self.owner.preplay(dungeons, world, overworld_tiles, party)
            elif handler.option == 1:
                dungeons, world, overworld_tiles, log, party = load_game()
                self.owner.preplay(dungeons, world, overworld_tiles, party)
            elif handler.option == 2:
                self.owner.quit()

