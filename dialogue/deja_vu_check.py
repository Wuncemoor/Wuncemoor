def deja_vu_check(dialogue_handler, option):

    dialogue = dialogue_handler.partner.noncombatant.dialogue

    nn_string = dialogue_handler.real_io.get(str(option))

    new_node = dialogue.graph_dict.get(nn_string)
    return new_node.visited


