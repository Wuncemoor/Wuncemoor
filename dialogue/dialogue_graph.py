class DialogueGraph:

    def __init__(self):
        self.graph_dict = {}
        self.current_convo = 'root'


class DialogueNode:

    def __init__(self, words, options, signal=None):
        self.words = words
        self.options = options
        self.visited = False
        self.results = {}
        self.signal = signal

    def add_result(self, key, val):
        self.results[key] = val

class DialogueNodeOption:

    def __init__(self, text, condition=None):
        self.text = text
        self.condition = condition
