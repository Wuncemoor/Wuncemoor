from abstracts.abstract_maps import InitTiles
from map_objects.tile import Tile, FakeTile


class InitFakeTiles(InitTiles):

    def initialize_tiles(self):
        tiles = [[FakeTile(self.variant) for x in range(self.width)] for y in range(self.height)]

        return tiles


class InitRealTiles(InitTiles):

    def initialize_tiles(self):
        tiles = [[Tile(self.variant) for x in range(self.width)] for y in range(self.height)]

        return tiles
