from enums.game_states import GameStates, MenuStates
from handlers.logic.options import title_options, party_options, inventory_options, journal_options


class OptionsHandler:

    def __init__(self):
        self.current = title_options()

    @property
    def state(self):
        return self.owner.state

    @property
    def handler(self):
        return self.owner.state_handler

    @property
    def mapping(self):
        maps = {
            GameStates.TITLE: self.title,
            # GameStates.LIFE: self.life,
            # GameStates.ENCOUNTER: self.encounter,
            # GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            # GameStates.REWARD: self.loot,
            # GameStates.SHOW_MAP: self.map,
        }
        return maps.get(self.state)()

    def traverse(self, amount):
        if self.state == GameStates.TITLE:
            self.traverse_int(amount)
        elif self.handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and self.handler.display is None:
            self.traverse_int(amount[0])
        elif self.handler.state in MenuStates.JOURNAL:
            self.traverse_int(amount[1])

    def traverse_int(self, amount):
        if (amount < 0 and self.current.choice == 0) or (amount > 0 and self.current.choice >=
                                                         (len(self.current.options) - 1)):
            pass
        else:
            self.current.choice += amount

    def choose(self):
        option = self.current.options[self.current.choice]

        return option.logic

    def title(self):
        self.current = title_options()

    def menus(self):
        key = self.handler.state
        dict = {
            MenuStates.PARTY: party_options(),
            MenuStates.INVENTORY: inventory_options(),
            MenuStates.JOURNAL: journal_options(),
            MenuStates.MAP: map_options(),
        }
        self.current = dict.get(key)


