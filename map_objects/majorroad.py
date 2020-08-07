from map_objects.transition import Transition
from abstracts.abstract_structure import AbstractStructure
from abstracts.abstract_tile_component import ModalTileFloor
from config.image_objects import LIGHT_ROAD, DARK_ROAD, BUNDLE_ALPHA


class RoadTileFloor(ModalTileFloor):
    """Floor component for Tile used to represent road. Currently the only type of road floor."""

    light_dict = LIGHT_ROAD
    dark_dict = DARK_ROAD
    name = 'Road'

    def __str__(self):
        static = 'class: RoadTileFloor | mode: '
        if self.mode is None:
            dynamic = 'NONE'
        elif (self.light_image or self.dark_image) is None:
            dynamic = self.mode + ' | images: NONE'
        else:
            dynamic = self.mode + ' | light_image: ' + self.light_image.name + ' | dark_image: ' + self.dark_image.name
        return static + dynamic

    def __repr__(self):
        return "RoadTileFloor(" + repr(self.light_image) + ", " + repr(self.dark_image) + ", " + repr(self.transition) + ", " + self.mode + "}"


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
                row[0].floor.transition = trans
                row[-1].floor.transition = trans

        elif dimension == 'horizontal':
            for row in (self.tiles[0], self.tiles[-1]):
                for tile in row:
                    tile.floor.transition = trans
