from dialogue.dialogue_graph import DialogueNode, DialogueGraph
from dialogue.dialogue_graph import DialogueNodeOption as DNO


def get_samwise_dialogue():

    dialogue = DialogueGraph()

    root = get_samwise_node('root')
    root.add_result('a', 'second')
    root.add_result('b', 'ominous_dream')
    root.add_result('c', 'basic_exit')

    second = get_samwise_node('second')
    second.add_result('a', 'root')
    second.add_result('b', 'basic_exit')

    exit = get_samwise_node('exit')

    om_exit = get_samwise_node('ominous_exit')
    om_exit.add_result('a', 'exit')
    basic_exit = get_samwise_node('basic_exit')
    basic_exit.add_result('a', 'exit')

    om_dream = get_samwise_node('ominous_dream')
    om_dream.add_result('a', 'ominous_exit')


    dialogue.graph_dict['root'] = root
    dialogue.graph_dict['second'] = second
    dialogue.graph_dict['exit'] = exit
    dialogue.graph_dict['ominous_dream'] = om_dream
    dialogue.graph_dict['ominous_exit'] = om_exit
    dialogue.graph_dict['basic_exit'] = basic_exit

    return dialogue


def get_samwise_node(type):
    if type == 'root':
        words = "This game is gonna be great one day, don't you think?"
        options = [DNO("Definitely! What's your favorite part?"), DNO("Can I talk to you about a dream I had last night?", condition=['An Ominous Dream', 'Find Samwise']), DNO("Can't talk now, too much to do!")]
    elif type == 'second':
        words = 'The fact that I exist!'
        options = [DNO("Huh, I guess I never thought about it like that. Let's talk about that earlier thing"),
                   DNO("Can't talk now, too much to do!")]
    elif type == 'exit':
        words = ''
        options = []
    elif type == 'ominous_dream':
        words = "That's pretty crazy, but I wouldn't worry about it."
        options = [DNO("I guess you're right... see ya!")]
        signal = ('An Ominous Dream', 'COMPLETE')
    elif type == 'ominous_exit':
        words = "Let's talk again soon!"
        options = [DNO("[Leave]")]
    elif type == 'basic_exit':
        words = "Later."
        options = [DNO("[Leave]")]
    try:
        return DialogueNode(words, options, signal)
    except:
        return DialogueNode(words, options)
