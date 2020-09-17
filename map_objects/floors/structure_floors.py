from abstracts.abstract_tile_component import AbstractTileFloor
from config.image_objects import INN_FLOOR_S


class WoodTileFloor(AbstractTileFloor):

    name = 'Wood Floor'

    def __init__(self):
        super().__init__()
        self.light_image = INN_FLOOR_S
        self.dark_image = INN_FLOOR_S

    def __repr__(self):
        return 'DirtTileFloor'


