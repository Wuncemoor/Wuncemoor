from abstracts.abstract_structure import PrefabStructure
from abstracts.abstract_tile_component import AbstractTileFloor
from config.image_objects import OVERWORLD_TOWN, BUNDLE_ALPHA
from world_objects.rect import Rect
from world_objects.transition import Transition


class OverworldTownTileFloor(AbstractTileFloor):

    name = 'Town'

    def __init__(self, image):
        super().__init__()
        self.image = image

    def __repr__(self):
        return 'OverworldTownFloor()'


class OverworldTown(PrefabStructure):
    """Fills tiles with generic townfloor image, fills floor transitions based on given plot node"""

    _floors = None
    _decorations = [[OverworldTownTileFloor(img) for img in row] for row in OVERWORLD_TOWN]
    _blockers = None
    _overhead = None
    rect = Rect(0, 0, len(_decorations[0]), len(_decorations))
    is_interior = False

    def __init__(self, node):
        super().__init__()
        self.set_transitions(node)

    def set_transitions(self, node):
        trans = Transition('The entrance to ' + node.name.capitalize(), BUNDLE_ALPHA, node.name, 0, (node.entrance[0], node.entrance[1]))
        for row in self.tiles:
            for tile in row:
                tile.floor.transition = trans

