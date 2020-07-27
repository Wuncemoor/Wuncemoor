from abc import ABC, abstractmethod

from map_objects.tile import Tile


class Tiles2D(ABC):

    def __init__(self, width, height, variant):
        self.width = width
        self.height = height
        self.variant = variant
        self.tiles = self.initialize_tiles()

    @abstractmethod
    def fill_map(self):
        pass

    def initialize_tiles(self):
        tiles = [[Tile(self.variant) for y in range(self.height)] for x in range(self.width)]

        return tiles