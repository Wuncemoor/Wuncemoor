from enums.game_states import GameStates, MenuStates
from handlers.logic.options import title_options, Options


class OptionsHandler:

    def __init__(self):
        self.current = title_options()

    @property
    def state(self):
        return self.owner.state

    @property
    def handler(self):
        return self.owner.state_handler

    def wrap_and_set(self, options):
        self.current = Options(options)

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

    def traverse(self, path):
        if self.state == GameStates.TITLE:
            self.traverse_list(path)
        elif self.state == GameStates.DIALOGUE:
            self.traverse_graph(path)
        elif self.handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and self.handler.menu.sub is None:
            self.traverse_list(path[0])
        elif self.handler.state == MenuStates.JOURNAL:
            self.traverse_list(path[1])

    def traverse_list(self, amount):
        if (amount < 0 and self.current.choice == 0) or (amount > 0 and self.current.choice >=
                                                         (len(self.current.options) - 1)):
            pass
        else:
            self.current.choice += amount

    def traverse_graph(self, path):
        key = chr(path)

        if key in self.handler.real_io.keys():
            self.current.conversation = self.handler.real_io.get(key)
            current_node = self.current.graph_dict.get(self.current.conversation)
            current_node.visited = True
            self.handler.set_real_talk()
            self.handler.broadcast_choice(current_node.signal)

            if self.current.conversation == 'exit':
                self.current.conversation = 'root'
                self.owner.state_handler = self.owner.life
                self.current = None


    def choose(self):
        option = self.current.options[self.current.choice]
        print(option)

        return option.logic

    def title(self):
        self.current = title_options()

    def menus(self):
        return self.handler.menu.options



