from ECS.__entity.transition import Transition
from abstracts.abstract_maps import ProceduralTiles2D
from abstracts.abstract_structure import AbstractStructure
from abstracts.abstract_tile_component import ModalTileFloor
from config.image_objects import LIGHT_ROAD, DARK_ROAD, BUNDLE_ALPHA


class RoadTileFloor(ModalTileFloor):
    """Floor component for Tile used to represent road. Currently the only type of road floor."""

    light_dict = LIGHT_ROAD
    dark_dict = DARK_ROAD
    name = 'Road'


class MajorRoad(AbstractStructure):
    """A unique Structure that connects all dungeons to the overworld. variant is the node that OverworldBuilder made
    for this map """

    def fill_tiles(self):
        for row in self.tiles:
            for tile in row:
                tile.floor = RoadTileFloor()

    def set_transitions(self, dimension):
        trans = Transition('Road leaving town', BUNDLE_ALPHA, 'overworld', 0, (self.variant.x, self.variant.y))
        if dimension == 'vertical':
            for row in self.tiles:
                for tile in (row[0], row[-1]):
                    tile.floor.transition = trans
        elif dimension == 'horizontal':
            for row in (self.tiles[0], self.tiles[-1]):
                for tile in row:
                    tile.floor.transition = trans

# class Road:
#
#     def __init__ (self, rect, go_to_dungeon=None, go_to_floor=None, go_to_xy=None, transitions_img=None):
#         self.rect = rect
#         self.go_to_dungeon = go_to_dungeon
#         self.go_to_floor = go_to_floor
#         self.go_to_xy = go_to_xy
#         self.transitions = []
#         self.transitions_img = transitions_img
#
#     def set_transitions(self, dimension):
#         stairs = Transition('Stairs', self.transitions_img, self.go_to_dungeon, self.go_to_floor, self.go_to_xy)
#         if dimension == 'vertical':
#             for j in range(self.rect.y1, self.rect.y2):
#                 self.transitions.append(Entity(self.rect.x1, j, transition=stairs))
#                 self.transitions.append(Entity(self.rect.x2-1, j, transition=stairs))
#
#         elif dimension == 'horizontal':
#             for i in range(self.rect.x1, self.rect.x2):
#                 self.transitions.append(Entity(i, self.rect.y1, transition=stairs))
#                 self.transitions.append(Entity(i, self.rect.y2-1, transition=stairs))
