from dataclasses import dataclass, field
from typing import Union, Dict, List

from data_structures.menu_tools import LogicList
from enums.game_states import MenuStates, MenuSubStates
from handlers.logic.menus_logic import menus_goto_submenu, menus_goto_selected_options


class Journal:
    def __init__(self):
        self.superstate = MenuStates.JOURNAL
        self.state = MenuSubStates.BASE
        self.current_quests = LogicList([], menus_goto_selected_options)
        self.completed_quests = LogicList([], menus_goto_selected_options)
        self.codex = LogicList([], menus_goto_selected_options)
        self.convo_history = LogicList([], menus_goto_selected_options)
        self.menu = self.initialize_menu()
        self.submenu = None

    def initialize_menu(self):
        return LogicList([self.current_quests, self.completed_quests, self.codex, self.convo_history], menus_goto_submenu)

    def change_state(self, state, options):
        self.state = self.state.__class__(state)
        if state == 1:
            self.submenu = None
            self.menu.unlock()
            options.current = self.menu
        elif state == 2:
            self.menu.lock()
            self.submenu = self.menu.pointer_data
            self.submenu.unlock()
            options.current = self.submenu
            if len(options.current) == 0:
                self.change_state(1, options)
        elif state == 3:
            self.submenu.lock()
            entity = self.submenu.pointer_data
            options.get(component=entity)


    def update_plot(self, signal):
        for quest in self.current_quests:
            if quest.title == signal[0]:
                quest.traverse_plot(signal[1])
                if not quest.current_node.condition:
                    self.finish_quest(quest)

    def finish_quest(self, quest):
        self.completed_quests.append(quest)
        self.current_quests.remove(quest)

    def transduce_all(self, dialogue_partner_name):
        responses = []
        for quest in self.current_quests:
            response = self.transduce(quest, dialogue_partner_name)
            if response is not None:
                responses.append(response)
        return responses

    def transduce(self, quest, dialogue_partner):
        if quest.current_node.cares_about(dialogue_partner):
            return [quest.title, quest.current_node.title]
        return None

    def get_sub(self):
        sj_dict = [self.current_quests, self.completed_quests, self.codex, self.convo_history]

        return sj_dict[self.options.choice]


@dataclass
class QuestNode:

    title: str
    info: str
    condition: Union[str, None] = None
    plot_paths: Union[Dict, None] = None

    def cares_about(self, maybe_care):
        if maybe_care is self.condition:
            return True
        return False


@dataclass
class Quest:

    title: str
    current_node: Union[QuestNode, None]
    plot: List = field(default_factory=list)
    starred: bool = False
    part_of_main_storyline: bool = False

    def traverse_plot(self, signal):
        self.current_node = self.current_node.plot_paths.get(signal)
        self.plot.append(self.current_node)



