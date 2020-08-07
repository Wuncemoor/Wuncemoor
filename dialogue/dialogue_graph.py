class DialogueGraph:
    """Holds a dict with all accessible DialogueNodes in a conversation"""

    def __init__(self):
        self.graph_dict = {}
        self.conversation = 'root'


class DialogueNode:
    """A single point in a conversation. Has words being directed at Player and can broadcast a signal upon
    activation., Possible responses change text color if they have already been used """

    def __init__(self, words, options_text, signal=None):
        self.words = words
        self.options_text = options_text
        self.visited = False
        self.signal = signal


class DialogueNodeOption:
    """A single pathway out of a DialogueNode. May only be conditionally available to the Player."""

    def __init__(self, text, path, condition=None):
        self.text = text
        self.path = path
        self.condition = condition

