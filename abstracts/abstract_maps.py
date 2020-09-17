from abc import ABC, abstractmethod


class AbstractInitTiles(ABC):
    """Abstract fpr creating an array of Tile objects. You likely want to inherit from InitRealTiles or InitFakeTiles"""

    def __init__(self):
        self.tiles = self.initialize_tiles()

    @abstractmethod
    def initialize_tiles(self):
        pass


class AbstractFillTiles(ABC):
    """Abstract for filling an array of Tile objects"""

    @abstractmethod
    def fill_tiles(self):
        pass


class PrefabTiles2D(AbstractInitTiles, AbstractFillTiles, ABC):
    """Abstract for tiles that are always linked together in the same configuration"""
    def __init__(self):
        self.width = len(self._images[0][0])
        self.height = len(self._images[0])
        super().__init__()


class ProceduralTiles2D(AbstractInitTiles, AbstractFillTiles, ABC):
    """Abstract for procedurally creating Tile arrays based on parameters"""

    def __init__(self, width, height, variant):
        self.width = width
        self.height = height
        self.variant = variant
        super().__init__()
