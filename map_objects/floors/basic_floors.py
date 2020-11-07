from random import randint

from abstracts.abstract_tile_component import AbstractTileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import LIGHT_GRASS, DARK_GRASS, LIGHT_DIRT, DARK_DIRT, GRASS


class GrassTileFloor(AbstractTileFloor):

    name = 'Grass'

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('grass') - 1)
        self.light_image = GRASS
        self.dark_image = GRASS


class DirtTileFloor(AbstractTileFloor):

    name = 'Dirt'

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('dirt') - 1)
        self.light_image = LIGHT_DIRT[num]
        self.dark_image = DARK_DIRT[num]

    def __repr__(self):
        return 'DirtTileFloor'

