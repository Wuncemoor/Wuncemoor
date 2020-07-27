from random import randint

from abstracts.abstract_structural import TileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import LIGHT_GRASS, DARK_GRASS, LIGHT_DIRT, DARK_DIRT


class GrassTileFloor(TileFloor):

    num = randint(0, IMAGE_OPTIONS.get('grass') - 1)
    name = 'Grass'
    image = LIGHT_GRASS[num]
    image2 = DARK_GRASS[num]


class DirtTileFloor(TileFloor):

    num = randint(0, IMAGE_OPTIONS.get('dirt') - 1)
    name = 'Dirt'
    image = LIGHT_DIRT[num]
    image2 = DARK_DIRT[num]
