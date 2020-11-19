from abstracts.abstract_structure import PrefabStructure
from map_objects.blockers.inn_blockers import inn_blocker_array
from map_objects.blockers.mage_house_blockers import mage_house_blocker_array
from map_objects.floors.outside_floors import DirtTileFloor
from map_objects.rect import Rect


class TownAlphaInn(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = inn_blocker_array()
    rect = Rect(25, 25, 9, 7)

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
    rect = Rect(7, 7, 8, 6)

    def __init__(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        print(self.width)
        print(self.height)
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
