from abc import ABC, abstractmethod


class InitTiles(ABC):

    def __init__(self):
        self.tiles = self.initialize_tiles()

    @abstractmethod
    def initialize_tiles(self):
        pass


class FillTiles(ABC):

    @abstractmethod
    def fill_tiles(self):
        pass


class PrefabTiles2D(InitTiles, FillTiles, ABC):
    pass


class ProceduralTiles2D(InitTiles, FillTiles, ABC):

    def __init__(self, width, height, variant):
        self.width = width
        self.height = height
        self.variant = variant
        super().__init__()
