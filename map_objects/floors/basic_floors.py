
from abstracts.abstract_tile_component import AbstractTileFloor
from config.image_objects import GRASS_TILE_FLOOR, DIRT_TILE_FLOOR


class GrassTileFloor(AbstractTileFloor):

    name = 'Grass'

    def __init__(self):
        super().__init__()
        self.image = GRASS_TILE_FLOOR


class DirtTileFloor(AbstractTileFloor):

    name = 'Dirt'

    def __init__(self):
        super().__init__()
        self.image = DIRT_TILE_FLOOR

    def __repr__(self):
        return 'DirtTileFloor'

