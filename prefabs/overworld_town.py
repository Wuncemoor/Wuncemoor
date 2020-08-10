from abstracts.abstract_maps import PrefabTiles2D
from abstracts.abstract_structure import PrefabStructure
from abstracts.abstract_tile_component import AbstractTileFloor
from config.image_objects import OVERWORLD_TOWN, BUNDLE_ALPHA
from dungeons.tile_mixins import InitFakeTiles
from map_objects.transition import Transition


class OverworldTownFloor(AbstractTileFloor):

    name = 'Town'

    def __init__(self, i, j):
        super().__init__()
        self.light_image = OVERWORLD_TOWN[0][j][i]
        self.dark_image = OVERWORLD_TOWN[1][j][i]

    def __repr__(self):
        return 'OverworldTownFloor()'


class OverworldTown(PrefabStructure):
    """Variant = PlotNode"""
    def __init__(self, node):
        super().__init__(node)
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = OverworldTownFloor(i, j)
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        trans = Transition('The entrance to ' + self.variant.name.capitalize(), BUNDLE_ALPHA, self.variant.name, 0, (self.variant.entrance[0], self.variant.entrance[1]))
        for row in self.tiles:
            for tile in row:
                tile.floor.transition = trans

