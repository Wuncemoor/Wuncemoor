from abstracts.abstract_structure import ProceduralStructure
from abstracts.abstract_tile_component import ModalTileBlocker
from config.image_objects import STONE_WALL
from map_objects.floors.basic_floors import GrassTileFloor


class TownWalls(ProceduralStructure):
    """A structure that surrounds a town, separating it from the nearby scenery. Variant is the type of material the
    wall is built out of."""

    def __init__(self, rect, variant):
        super().__init__(rect, variant)

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                print(str(i) + ' ' + str(j))
                if (i in (0, self.width - 1)) or (j in (0, self.height - 1)):
                    tile.floor = self.set_floor()
                    tile.blocker = self.set_blocker()
                else:
                    tile.floor = None
                    tile.blocker = None
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


    @staticmethod
    def set_floor():
        return GrassTileFloor()

    def set_blocker(self):
        if self.variant == 'stone':
            return StoneWallTileBlocker()


class StoneWallTileBlocker(ModalTileBlocker):

    light_dict = STONE_WALL
    dark_dict = STONE_WALL
    name = 'Stone Wall'
    opaque = True
    overshadow = None

