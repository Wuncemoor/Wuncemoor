from random import randint

from abstracts.abstract_tile_component import AbstractTileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import LIGHT_GRASS, DARK_GRASS, LIGHT_DIRT, DARK_DIRT, LIGHT_ROAD, DARK_ROAD


class PrefabTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.name = None

    name = 'Prefab'


class GrassTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('grass') - 1)
        self.image = LIGHT_GRASS[num]
        self.image2 = DARK_GRASS[num]

    name = 'Grass'


class DirtTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('dirt') - 1)
        self.image = LIGHT_DIRT[num]
        self.image2 = DARK_DIRT[num]

    name = 'Dirt'


class RoadTileFloor(AbstractTileFloor):

    def __init__(self, mode):
        super().__init__()
        self.image = LIGHT_ROAD.get(mode)
        self.image2 = DARK_ROAD.get(mode)

    name = 'Road'


