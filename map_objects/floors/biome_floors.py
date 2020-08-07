from random import randint
from abstracts.abstract_tile_component import AbstractTileFloor
from config.constants import IMAGE_OPTIONS
from config.image_objects import BIOMES


class DeepTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_deep')[num]
        self.dark_image = BIOMES.get('dark_deep')[num]

    name = 'Deep Water'


class DesertTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_desert')[num]
        self.dark_image = BIOMES.get('dark_desert')[num]

    name = 'Desert'


class ForestTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_forest')[num]
        self.dark_image = BIOMES.get('dark_forest')[num]

    name = 'Forest'


class PlainsTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_plains')[num]
        self.dark_image = BIOMES.get('dark_plains')[num]

    name = 'Plains'


class SavannahTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_savannah')[num]
        self.dark_image = BIOMES.get('dark_savannah')[num]

    name = 'Savannah'


class ShallowTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_shallow')[num]
        self.dark_image = BIOMES.get('dark_shallow')[num]

    name = 'Shallow Water'


class SnowTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_snow')[num]
        self.dark_image = BIOMES.get('dark_snow')[num]

    name = 'Snow'


class TaigaTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_taiga')[num]
        self.dark_image = BIOMES.get('dark_taiga')[num]

    name = 'Taiga'


class TemprainTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_temprain')[num]
        self.dark_image = BIOMES.get('dark_temprain')[num]

    name = 'Temperate Rainforest'


class TropicrainTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_tropicrain')[num]
        self.dark_image = BIOMES.get('dark_tropicrain')[num]

    name = 'Tropical Rainforest'


class TundraTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        num = randint(0, IMAGE_OPTIONS.get('biome') - 1)
        self.light_image = BIOMES.get('light_tundra')[num]
        self.dark_image = BIOMES.get('dark_tundra')[num]

    name = 'Tundra'

