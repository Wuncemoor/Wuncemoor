from abstracts.abstract_tile_component import AbstractTileFloor
from config.image_objects import DEEP_TILE_FLOOR, DESERT_TILE_FLOOR, FOREST_TILE_FLOOR, PLAINS_TILE_FLOOR, \
    SAVANNAH_TILE_FLOOR, SHALLOW_TILE_FLOOR, SNOW_TILE_FLOOR, TAIGA_TILE_FLOOR, TEMPRAIN_TILE_FLOOR, \
    TROPICRAIN_TILE_FLOOR, TUNDRA_TILE_FLOOR


class DeepTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = DEEP_TILE_FLOOR

    name = 'Deep Water'


class DesertTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = DESERT_TILE_FLOOR

    name = 'Desert'


class ForestTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = FOREST_TILE_FLOOR

    name = 'Forest'


class PlainsTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = PLAINS_TILE_FLOOR

    name = 'Plains'


class SavannahTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = SAVANNAH_TILE_FLOOR

    name = 'Savannah'


class ShallowTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = SHALLOW_TILE_FLOOR

    name = 'Shallow Water'


class SnowTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = SNOW_TILE_FLOOR

    name = 'Snow'


class TaigaTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = TAIGA_TILE_FLOOR

    name = 'Taiga'


class TemprainTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = TEMPRAIN_TILE_FLOOR

    name = 'Temperate Rainforest'


class TropicrainTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = TROPICRAIN_TILE_FLOOR

    name = 'Tropical Rainforest'


class TundraTileFloor(AbstractTileFloor):

    def __init__(self):
        super().__init__()
        self.image = TUNDRA_TILE_FLOOR

    name = 'Tundra'

