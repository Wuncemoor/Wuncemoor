from abstracts.abstract_maps import InitTiles
from map_objects.tile import Tile, PrefabTile


class InitPrefabTiles(InitTiles):

    def initialize_tiles(self):
        tiles = [[PrefabTile() for y in range(self.height)] for x in range(self.width)]

        return tiles


class InitRealTiles(InitTiles):

    def initialize_tiles(self):
        tiles = [[Tile(self.variant) for y in range(self.height)] for x in range(self.width)]

        return tiles
