from dialogue.dialogue_graph import DialogueNode, DialogueGraph
from dialogue.dialogue_graph import DialogueNodeOption as DNO


def get_samwise_dialogue():

    dialogue = DialogueGraph()

    root = get_samwise_node('root')
    second = get_samwise_node('second')
    third = get_samwise_node('third')
    shop = get_samwise_node('shop')
    exit = get_samwise_node('exit')

    om_exit = get_samwise_node('ominous_exit')
    basic_exit = get_samwise_node('basic_exit')

    om_dream = get_samwise_node('ominous_dream')

    dialogue.graph_dict['root'] = root
    dialogue.graph_dict['second'] = second
    dialogue.graph_dict['third'] = third
    dialogue.graph_dict['shop'] = shop
    dialogue.graph_dict['exit'] = exit
    dialogue.graph_dict['ominous_dream'] = om_dream
    dialogue.graph_dict['ominous_exit'] = om_exit
    dialogue.graph_dict['basic_exit'] = basic_exit

    return dialogue


def get_samwise_node(type):
    if type == 'root':
        words = "This game is gonna be great one day, don't you think?"
        options = [DNO("Definitely! What's your favorite part?", 'second'), DNO("Can I talk to you about a dream I had last night?", 'ominous_dream', condition=['An Ominous Dream', 'Find Samwise']), DNO("Do you have anything for sale?", 'third'), DNO("Can't talk now, too much to do!", 'exit')]
    elif type == 'second':
        words = 'The fact that I exist!'
        options = [DNO("Huh, I guess I never thought about it like that. Let's talk about that earlier thing", 'root'),
                   DNO("Can't talk now, too much to do!", 'exit')]
    elif type == 'third':
        words = 'Kind of a weird question to ask a kid, but yeah actually I do!'
        options = [DNO('[Go to Shop]', 'shop')]
    elif type == 'exit':
        words = ''
        options = []
    elif type == 'shop':
        words = ''
        options = []
    elif type == 'ominous_dream':
        words = "That's pretty crazy, but I wouldn't worry about it."
        options = [DNO("I guess you're right... see ya!", 'ominous_exit')]
        signal = ('An Ominous Dream', 'COMPLETE')
    elif type == 'ominous_exit':
        words = "Let's talk again soon!"
        options = [DNO("[Leave]", 'exit')]
    elif type == 'basic_exit':
        words = "Later."
        options = [DNO("[Leave]", 'exit')]
    try:
        return DialogueNode(words, options, signal)
    except:
        return DialogueNode(words, options)
