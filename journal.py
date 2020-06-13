from enums.game_states import MenuStates
class Journal:
    def __init__(self):
        self.current_quests = []
        self.completed_quests = []
        self.codex = []
        self.convo_history = []
        self.superstate = MenuStates.JOURNAL
        self.options = ['current', 'completed', 'codex', 'convo']

class Quest:
    def __init__(self, title, graph):
        self.title = title
        self.plot = []
        self.graph = graph
        self.current_node = None


class QuestNode:
    def __init__(self, title, info):
        self.title = title
        self.info = info
