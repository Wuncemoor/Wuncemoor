from abstracts.abstract_structure import PrefabStructure
from abstracts.abstract_tile_component import AbstractTileFloor
from config.image_objects import OVERWORLD_TOWN, BUNDLE_ALPHA
from map_objects.rect import Rect
from map_objects.transition import Transition


class OverworldTownTileFloor(AbstractTileFloor):

    name = 'Town'

    def __init__(self, i, j):
        super().__init__()
        self.image = OVERWORLD_TOWN[j][i]

    def __repr__(self):
        return 'OverworldTownFloor()'


class OverworldTown(PrefabStructure):
    """Fills tiles with generic townfloor image, fills floor transitions based on given plot node"""

    _images = OVERWORLD_TOWN
    rect = Rect(0, 0, len(_images[0]), len(_images))
    is_interior = False

    def __init__(self, node):
        super().__init__()
        self.fill_tiles()
        self.set_transitions(node)

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = OverworldTownTileFloor(i, j)
                i += 1
            j += 1
            i = 0

    def set_transitions(self, node):
        trans = Transition('The entrance to ' + node.name.capitalize(), BUNDLE_ALPHA, node.name, 0, (node.entrance[0], node.entrance[1]))
        for row in self.tiles:
            for tile in row:
                tile.floor.transition = trans

