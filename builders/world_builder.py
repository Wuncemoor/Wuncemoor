from builders.dungeon_builders import OverworldBuilder, DungeonAlphaBuilder, DungeonBetaBuilder, DungeonGammaBuilder, \
    DungeonDeltaBuilder
from map_objects.dungeon import Dungeon


class DungeonDirector:
    """Assists WorldHandler by receiving high level commands and returning Dungeons (and occasionally other things).
    Dungeon creation is delegated to DungeonBuilders. """

    def __init__(self):
        self.builder = None

    def overworld(self):
        self.builder = OverworldBuilder()
        overworld = self.get_dungeon()
        nodes = self.builder.apply_core_plot_nodes(overworld.maps[0])

        return overworld, nodes

    def core_plot(self, nodes):
        self.builder = DungeonAlphaBuilder(nodes[0])
        alpha = self.get_dungeon()
        self.builder = DungeonBetaBuilder(nodes[1])
        beta = self.get_dungeon()
        self.builder = DungeonGammaBuilder(nodes[2])
        gamma = self.get_dungeon()
        self.builder = DungeonDeltaBuilder(nodes[3])
        delta = self.get_dungeon()
        return alpha, beta, gamma, delta

    def get_dungeon(self):
        dungeon = Dungeon('NAME_UNDEFINED', 'FLOORS_UNDEFINED', 'MAPS_UNDEFINED', 'NODEPOWER_UNDEFINED')

        name = self.builder.get_name()
        dungeon.name = name

        floors = self.builder.get_floors()
        dungeon.floors = floors

        maps = self.builder.get_maps()
        dungeon.maps = maps

        np = self.builder.get_np()
        dungeon.np = np

        return dungeon



