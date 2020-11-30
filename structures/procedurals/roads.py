from world_objects.floors.outside_floors import DirtTileFloor
from world_objects.transition import Transition
from abstracts.abstract_structure import ProceduralStructure
from config.image_objects import BUNDLE_ALPHA


class Road(ProceduralStructure):
    """A Structure that represents a road for players to travel on."""
    is_interior = False

    def __init__(self, rect, variant=None):
        super().__init__(rect, variant)

    def fill_tiles(self):
        for row in self.tiles:
            for tile in row:
                tile.floor = DirtTileFloor()

    def set_transitions(self):
        pass


class MajorRoad(Road):
    """A unique Road that connects all dungeons to the overworld. variant is the node that OverworldBuilder made
    for this map """

    def __init__(self, rect, variant):
        super().__init__(rect, variant)

    def set_transitions(self, dimension):
        trans = Transition('Road leaving town', BUNDLE_ALPHA, 'overworld', 0, (self.variant.x, self.variant.y))
        if dimension == 'vertical':
            for row in self.tiles:
                row[0].floor.transition = trans
                row[-1].floor.transition = trans

        elif dimension == 'horizontal':
            for row in (self.tiles[0], self.tiles[-1]):
                for tile in row:
                    tile.floor.transition = trans
