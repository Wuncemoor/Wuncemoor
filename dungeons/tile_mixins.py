from abstracts.abstract_maps import AbstractInitTiles
from map_objects.tile import Tile, FakeTile


class InitFakeTiles(AbstractInitTiles):
    """Used to make Structures in Hammerspace before integration into a real Map"""

    def initialize_tiles(self):
        tiles = [[FakeTile() for x in range(self.width)] for y in range(self.height)]

        return tiles


class InitRealTiles(AbstractInitTiles):
    """Used by real Maps in the real game"""

    def initialize_tiles(self):
        tiles = [[Tile(self.variant) for x in range(self.width)] for y in range(self.height)]

        return tiles
