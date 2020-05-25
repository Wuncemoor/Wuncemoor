import random
from maps.world_map.plot_node import PlotNode


def get_core_plot_nodes(width, height):

    xys = get_intro_nodes(width, height)
    return xys


def get_intro_nodes(width, height):
    tw, th = 8, 4
    spawn = [(5, 20), (70, 20), (5, 20), (5, 5)]
    delta = [-30, -30, -50]
    name = ['town', 'second_town', 'third_town', 'fourth_town']
    nodes_to_make = 4
    observed_node = 1
    completed_nodes = 0
    buffer = 5
    nodes = []

    make_nodes(nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name, buffer)
    return nodes


def make_nodes(nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name, buffer):
    if nodes_to_make == 0:
        pass
    else:
        ntm, cn, on, n = change_nodes(nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name,
                   buffer)
        make_nodes(ntm, cn, on, n, width, height, tw, th, spawn, delta, name, buffer)


def change_nodes(nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name,
                   buffer):
    xy_options, x_options, y_options = get_options(width, height, nodes, delta, tw, th, completed_nodes)
    if len(x_options) == 0 or len(y_options) == 0:
        nodes.pop()
        completed_nodes -= 1
        observed_node -= 1
        nodes_to_make += 1

    else:
        rand_xy = random.choice(xy_options)
        nn = PlotNode(name[completed_nodes], rand_xy[0], rand_xy[1], spawn[completed_nodes])
        apply_noflyzone(nn, nodes, rand_xy, tw, th, buffer)
        nodes.append(nn)
        completed_nodes += 1
        observed_node += 1
        nodes_to_make -= 1

    return nodes_to_make, completed_nodes, observed_node, nodes



def get_options(width, height, nodes, delta, tw, th, completed_nodes):
    xy_options, y_options, x_options = [], [], []
    no_fly = []
    for node in nodes:
        no_fly.extend(node.no_fly_zone)

    if completed_nodes == 0:
        for y in range(0, height - 1):
            if 0 <= y < (height - th):
                for x in range(0, width - 1):
                    if 0 <= x < (width - tw):
                        xy_options.append([x, y])
                        x_options.append(x)
                        y_options.append(y)
    else:
        for y in range(delta[completed_nodes - 1] + nodes[completed_nodes - 1].y, abs(delta[completed_nodes - 1]) + nodes[completed_nodes - 1].y + 1):
            if 0 <= y < (height - th):
                for x in range(delta[completed_nodes - 1] + nodes[completed_nodes - 1].x,
                               abs(delta[completed_nodes - 1]) + nodes[completed_nodes - 1].x + 1):
                    if 0 <= x < (width - tw) and [x, y] not in no_fly:
                        xy_options.append([x, y])
                        x_options.append(x)
                        y_options.append(y)
    return xy_options, x_options, y_options


def apply_noflyzone(node, nodes, rand_xy, tw, th, buffer):
    no_fly = []
    for node in nodes:
        no_fly.extend(node.no_fly_zone)
    for j in range(rand_xy[1] - th - buffer, rand_xy[1] + th + buffer + 1):
        for i in range(rand_xy[0] - tw - buffer, rand_xy[0] + tw + buffer + 1):
            if [i, j] not in no_fly:
                node.no_fly_zone.append([i, j])

