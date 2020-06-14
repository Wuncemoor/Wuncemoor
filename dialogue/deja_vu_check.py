def deja_vu_check(dialogue, current_node, option):

    nn_string = current_node.results.get(option)

    new_node = dialogue.graph_dict.get(nn_string)
    return new_node.visited


