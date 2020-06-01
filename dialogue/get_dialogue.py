from dialogue.dialogue_graph import DialogueNode, DialogueGraph


def get_samwise_dialogue():

    dialogue = DialogueGraph()

    root = get_samwise_root()
    root.add_result('a', None)

    dialogue.graph_dict['root'] = root

    return dialogue


def get_samwise_root():
    words = "This game is gonna be great one day, don't you think?"
    options = ['Duh.']
    return DialogueNode(words, options)
