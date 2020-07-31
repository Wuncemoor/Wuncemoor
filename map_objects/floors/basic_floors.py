from random import randint

from abstracts.abstract_tile_component import AbstractTileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import LIGHT_GRASS, DARK_GRASS, LIGHT_DIRT, DARK_DIRT


class GrassTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('grass') - 1)
        self.light_image = LIGHT_GRASS[num]
        self.dark_image = DARK_GRASS[num]

    name = 'Grass'


class DirtTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('dirt') - 1)
        self.light_image = LIGHT_DIRT[num]
        self.dark_image = DARK_DIRT[num]

    name = 'Dirt'


