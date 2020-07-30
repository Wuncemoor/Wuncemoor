from random import randint
from abstracts.abstract_tile_component import TileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import BIOMES


class DeepTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_deep')[num]
        self.image2 = BIOMES.get('dark_deep')[num]

    name = 'Deep Water'


class DesertTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_desert')[num]
        self.image2 = BIOMES.get('dark_desert')[num]

    name = 'Desert'


class ForestTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_forest')[num]
        self.image2 = BIOMES.get('dark_forest')[num]

    name = 'Forest'


class PlainsTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_plains')[num]
        self.image2 = BIOMES.get('dark_plains')[num]

    name = 'Plains'


class SavannahTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_savannah')[num]
        self.image2 = BIOMES.get('dark_savannah')[num]

    name = 'Savannah'


class ShallowTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_shallow')[num]
        self.image2 = BIOMES.get('dark_shallow')[num]

    name = 'Shallow Water'


class SnowTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_snow')[num]
        self.image2 = BIOMES.get('dark_snow')[num]

    name = 'Snow'


class TaigaTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_taiga')[num]
        self.image2 = BIOMES.get('dark_taiga')[num]

    name = 'Taiga'


class TemprainTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_temprain')[num]
        self.image2 = BIOMES.get('dark_temprain')[num]

    name = 'Temperate Rainforest'


class TropicrainTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_tropicrain')[num]
        self.image2 = BIOMES.get('dark_tropicrain')[num]

    name = 'Tropical Rainforest'


class TundraTileFloor(TileFloor):

    def __init__(self):
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.image = BIOMES.get('light_tundra')[num]
        self.image2 = BIOMES.get('dark_tundra')[num]

    name = 'Tundra'

