from random import randint

from abstracts.abstract_structural import TileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import LIGHT_GRASS, DARK_GRASS, LIGHT_DIRT, DARK_DIRT, LIGHT_ROAD, DARK_ROAD, BIOMES


class GrassTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('grass') - 1)
        self.image = LIGHT_GRASS[num]
        self.image2 = DARK_GRASS[num]

    name = 'Grass'


class DirtTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('dirt') - 1)
        self.image = LIGHT_DIRT[num]
        self.image2 = DARK_DIRT[num]

    name = 'Dirt'


class RoadTileFloor(TileFloor):

    def __init__(self, mode):
        self.image = LIGHT_ROAD.get(mode)
        self.image2 = DARK_ROAD.get(mode)

    name = 'Road'


