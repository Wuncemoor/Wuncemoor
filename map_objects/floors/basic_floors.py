from random import randint

from abstracts.abstract_tile_component import AbstractTileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import GRASS


class GrassTileFloor(AbstractTileFloor):

    name = 'Grass'

    def __init__(self):
        super().__init__()
        self.light_image = GRASS
        self.dark_image = GRASS


class DirtTileFloor(AbstractTileFloor):

    name = 'Dirt'

    def __init__(self):
        super().__init__()
        self.light_image = GRASS
        self.dark_image = GRASS

    def __repr__(self):
        return 'DirtTileFloor'

