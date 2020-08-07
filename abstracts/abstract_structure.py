from abc import ABC
from abstracts.abstract_maps import ProceduralTiles2D
from dungeons.tile_mixins import InitFakeTiles


class AbstractStructure(InitFakeTiles, ProceduralTiles2D, ABC):
    """Abstract to make a Stucture in Hammerspace. rect defines the coordinates for integration with real Map"""

    def __init__(self, rect, variant):
        super().__init__(rect.x2 - rect.x1, rect.y2 - rect.y1, variant)
        self.rect = rect
        self.fill_tiles()
