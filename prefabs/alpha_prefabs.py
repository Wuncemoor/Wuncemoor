from abstracts.abstract_structure import PrefabStructure
from map_objects.blockers.inn_blockers import inn_blocker_array, inn_overhead_array
from map_objects.blockers.mage_house_blockers import mage_house_blocker_array, mage_house_overhead_array, \
    mage_house2_blocker_array, mage_house2_overhead_array
from map_objects.floors.outside_floors import DirtTileFloor
from map_objects.rect import Rect


class TownAlphaInn(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = inn_blocker_array()
    _overhead = inn_overhead_array()
    rect = Rect(25, 25, 9, 7)
    is_interior = True

    def __init__(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaMageHouse(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = mage_house_blocker_array()
    _overhead = mage_house_overhead_array()
    rect = Rect(7, 7, 11, 9)
    is_interior = True

    def __init__(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaMageHousePathway(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(11, 16, 3, 19)
    is_interior = False

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = DirtTileFloor()
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass

