class DialogueGraph:

    def __init__(self):
        self.graph_dict = {}
        self.current_convo = 'root'


class DialogueNode:

    def __init__(self, words, options):
        self.words = words
        self.options = options
        self.visited = False
        self.results = {}

    def add_result(self, key, val):
        self.results[key] = val
