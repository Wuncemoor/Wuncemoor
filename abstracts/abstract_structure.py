from abc import ABC, abstractmethod
from abstracts.abstract_maps import ProceduralTiles2D, PrefabTiles2D
from dungeons.tile_mixins import InitFakeTiles


class ProceduralStructure(InitFakeTiles, ProceduralTiles2D, ABC):
    """Abstract to make a Stucture in Hammerspace. rect defines the coordinates for integration with real Map"""

    def __init__(self, rect, variant):
        super().__init__(rect.x2 - rect.x1, rect.y2 - rect.y1, variant)
        self.rect = rect
        self.fill_tiles()

    @abstractmethod
    def set_transitions(self):
        pass


class PrefabStructure(InitFakeTiles, PrefabTiles2D, ABC):
    """Abstract to make a Structure in Hammerspace. images stored in 2D array for integration with real Map"""

    def __init__(self, variant):
        super().__init__(variant)
        self.fill_tiles()

    @abstractmethod
    def set_transitions(self):
        pass
