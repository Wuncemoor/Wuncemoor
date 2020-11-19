
from abstracts.abstract_tile_component import AbstractTileFloor, ModalTileFloor
from config.image_objects import GRASS_TILE_FLOOR, DIRT_TILE_FLOOR


class GrassTileFloor(AbstractTileFloor):

    name = 'Grass'

    def __init__(self):
        super().__init__()
        self.image = GRASS_TILE_FLOOR


class DirtTileFloor(ModalTileFloor):
    """Floor component for Tile used to represent road. Currently the only type of road floor."""

    image_dict = DIRT_TILE_FLOOR
    name = 'Dirt Road'

    def __str__(self):
        static = 'class: DirtTileFloor | mode: '
        if self.mode is None:
            dynamic = 'NONE'
        elif self.image is None:
            dynamic = self.mode + ' | images: NONE'
        else:
            dynamic = self.mode + ' | image: ' + self.image.name
        return static + dynamic

    def __repr__(self):
        return "DirtTileFloor(" + repr(self.image) + ", " + repr(self.transition) + ", " + self.mode + "}"

