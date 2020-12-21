from data_structures.menu_tools import LogicList
from enums.game_states import MenuStates
from handlers.logic.menus_logic import menus_goto_submenu


class Journal:
    def __init__(self):
        self.current_quests = []
        self.completed_quests = []
        self.codex = []
        self.convo_history = []
        self.superstate = MenuStates.JOURNAL
        self.menu = self.initialize_menu()
        self.submenu = None

    def initialize_menu(self):
        return LogicList([self.current_quests, self.completed_quests, self.codex, self.convo_history], menus_goto_submenu)

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


class Quest:
    def __init__(self, title, current_node):
        self.title = title
        self.plot = []
        self.current_node = current_node

    def traverse_plot(self, signal):
        self.current_node = self.current_node.plot_paths.get(signal)
        self.plot.append(self.current_node)


class QuestNode:
    def __init__(self, title, info, condition=None, plot_paths=None):
        self.title = title
        self.info = info
        self.condition = condition
        self.plot_paths = plot_paths

    def cares_about(self, maybe_care):
        if maybe_care is self.condition:
            return True
        return False
