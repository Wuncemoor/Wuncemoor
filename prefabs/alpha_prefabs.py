from abstracts.abstract_structure import PrefabStructure
from map_objects.blockers.inn_blockers import inn_blocker_array
from map_objects.floors.structure_floors import WoodTileFloor


class TownAlphaInn(PrefabStructure):

    _floor = WoodTileFloor()
    _blockers = inn_blocker_array()

    def __init__(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floor
                tile.blocker = self._blockers[i][j]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass