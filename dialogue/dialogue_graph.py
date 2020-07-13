class DialogueGraph:

    def __init__(self):
        self.graph_dict = {}
        self.conversation = 'root'


class DialogueNode:

    def __init__(self, words, options_text, signal=None):
        self.words = words
        self.options_text = options_text
        self.visited = False
        self.signal = signal


class DialogueNodeOption:

    def __init__(self, text, path, condition=None):
        self.text = text
        self.path = path
        self.condition = condition

