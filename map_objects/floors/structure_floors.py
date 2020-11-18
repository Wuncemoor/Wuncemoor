from abstracts.abstract_tile_component import AbstractTileFloor, ModalTileFloor
from config.image_objects import INN_FLOOR_S, DIRT_ROAD


class WoodTileFloor(AbstractTileFloor):

    name = 'Wood Floor'

    def __init__(self):
        super().__init__()
        self.image = INN_FLOOR_S

    def __repr__(self):
        return 'WoodTileFloor'


class DirtRoadTileFloor(ModalTileFloor):
    """Floor component for Tile used to represent road. Currently the only type of road floor."""

    image_dict = DIRT_ROAD
    name = 'Dirt Road'

    def __str__(self):
        static = 'class: DirtRoadTileFloor | mode: '
        if self.mode is None:
            dynamic = 'NONE'
        elif self.image is None:
            dynamic = self.mode + ' | images: NONE'
        else:
            dynamic = self.mode + ' | image: ' + self.image.name
        return static + dynamic

    def __repr__(self):
        return "DirtRoadTileFloor(" + repr(self.image) + ", " + repr(self.transition) + ", " + self.mode + "}"