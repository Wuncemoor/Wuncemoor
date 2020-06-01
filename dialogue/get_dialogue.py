from dialogue.dialogue_graph import DialogueNode, DialogueGraph


def get_samwise_dialogue():

    dialogue = DialogueGraph()

    root = get_samwise_node('root')
    root.add_result('a', 'second')
    root.add_result('b', 'exit')

    second = get_samwise_node('second')
    second.add_result('a', 'root')
    second.add_result('b', 'exit')

    exit = get_samwise_node('exit')


    dialogue.graph_dict['root'] = root
    dialogue.graph_dict['second'] = second
    dialogue.graph_dict['exit'] = exit

    return dialogue


def get_samwise_node(type):
    if type == 'root':
        words = "This game is gonna be great one day, don't you think?"
        options = ["Definitely! What's your favorite part?", "Can't talk now, too much to do!"]
        return DialogueNode(words, options)
    elif type == 'second':
        words = 'The fact that I exist!'
        options = ["Huh, I guess I never thought about it like that. Let's talk about that earlier thing",
                   "Can't talk now, too much to do!"]
        return DialogueNode(words, options)
    elif type == 'exit':
        words = ''
        options = []
        return DialogueNode(words, options)
