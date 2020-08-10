import random
from dungeons.overworld.plot_node import PlotNode
from prefabs.overworld_town import OverworldTown


class PlotMixin:
    """Mixin for OverworldBuilder. Creates PlotNodes to mark coordinates of core plot locations"""

    def apply_core_plot_nodes(self, overworld):

        nodes = self.get_core_plot_nodes(overworld)
        self.add_towns(overworld, nodes)

        return nodes

    def get_core_plot_nodes(self, overworld):

        nodes = self.get_intro_nodes(overworld.width, overworld.height)
        return nodes

    def get_intro_nodes(self, width, height):
        tw, th = 8, 4
        spawn = [(5, 20), (70, 20), (5, 20), (5, 5)]
        delta = [-30, -30, -50]
        name = ['alpha', 'beta', 'gamma', 'delta']
        nodes_to_make = 4
        observed_node = 1
        completed_nodes = 0
        buffer = 5
        nodes = []

        self.make_nodes(nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name, buffer)
        return nodes

    def make_nodes(self, nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name, buffer):
        if nodes_to_make == 0:
            pass
        else:
            ntm, cn, on, n = self.change_nodes(nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name,
                       buffer)
            self.make_nodes(ntm, cn, on, n, width, height, tw, th, spawn, delta, name, buffer)

    def change_nodes(self, nodes_to_make, completed_nodes, observed_node, nodes, width, height, tw, th, spawn, delta, name,
                       buffer):
        xy_options, x_options, y_options = self.get_options(width, height, nodes, delta, tw, th, completed_nodes)
        if len(x_options) == 0 or len(y_options) == 0:
            nodes.pop()
            completed_nodes -= 1
            observed_node -= 1
            nodes_to_make += 1

        else:
            rand_xy = random.choice(xy_options)
            nn = PlotNode(name[completed_nodes], rand_xy[0], rand_xy[1], spawn[completed_nodes])
            self.apply_noflyzone(nn, nodes, rand_xy, tw, th, buffer)
            nodes.append(nn)
            completed_nodes += 1
            observed_node += 1
            nodes_to_make -= 1

        return nodes_to_make, completed_nodes, observed_node, nodes

    @staticmethod
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
            for y in range(delta[completed_nodes - 1] + nodes[completed_nodes - 1].y,
                           abs(delta[completed_nodes - 1]) + nodes[completed_nodes - 1].y + 1):
                if 0 <= y < (height - th):
                    for x in range(delta[completed_nodes - 1] + nodes[completed_nodes - 1].x,
                                   abs(delta[completed_nodes - 1]) + nodes[completed_nodes - 1].x + 1):
                        if 0 <= x < (width - tw) and [x, y] not in no_fly:
                            xy_options.append([x, y])
                            x_options.append(x)
                            y_options.append(y)
        return xy_options, x_options, y_options

    @staticmethod
    def apply_noflyzone(node, nodes, rand_xy, tw, th, buffer):
        no_fly = []
        for node in nodes:
            no_fly.extend(node.no_fly_zone)
        for j in range(rand_xy[1] - th - buffer, rand_xy[1] + th + buffer + 1):
            for i in range(rand_xy[0] - tw - buffer, rand_xy[0] + tw + buffer + 1):
                if [i, j] not in no_fly:
                    node.no_fly_zone.append([i, j])

    def add_towns(self, overworld, nodes):
        for node in nodes:
            self.add_town(overworld, node)

    @staticmethod
    def add_town(overworld, node):
        town = OverworldTown(node)
        y, x = 0, 0
        for j in range(node.y, node.y + len(node.images[0])):
            for i in range(node.x, node.x + len(node.images[0][0])):
                overworld.tiles[j][i].floor = town.tiles[y][x].floor
                x += 1
            y += 1
            x = 0
