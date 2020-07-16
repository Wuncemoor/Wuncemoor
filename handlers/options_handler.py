from enums.game_states import GameStates, MenuStates, EncounterStates
from handlers.logic.options import title_options, Options, encounter_options, encounter_targeting_options


class OptionsHandler:

    def __init__(self):
        self.current = title_options()

    @property
    def state(self):
        return self.owner.state

    @property
    def handler(self):
        return self.owner.state_handler

    @staticmethod
    def wrap(options):
        return Options(options)

    def wrap_and_set(self, options):
        self.current = self.wrap(options)


    @property
    def mapping(self):
        maps = {
            GameStates.TITLE: self.title,
            # GameStates.ENCOUNTER: self.encounter,
            # GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            # GameStates.REWARD: self.reward,
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
        elif self.handler.state == EncounterStates.THINKING:
            self.traverse_list(path[1])
        elif self.handler.state == EncounterStates.FIGHT_TARGETING:
            self.traverse_combat(path)

    def traverse_combat(self, path):
        

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

        return option.logic

    def title(self):
        self.current = title_options()

    def menus(self):
        return self.handler.menu.options

    def get(self):
            opts_dict = {
                EncounterStates.THINKING: encounter_options(),
                EncounterStates.FIGHT_TARGETING: encounter_targeting_options(self.handler.combat.grid),

            }
            return opts_dict.get(self.owner.state)



