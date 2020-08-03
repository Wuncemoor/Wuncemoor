from abc import ABC

from abstracts.abstract_maps import ProceduralTiles2D
from dungeons.tile_mixins import InitFakeTiles


class AbstractStructure(InitFakeTiles, ProceduralTiles2D, ABC):
    """rect defines the map coordinates for placement"""

    def __init__(self, rect, variant):
        super().__init__(rect.x2 - rect.x1, rect.y2 - rect.y1, variant)
        self.rect = rect
        self.fill_tiles()
