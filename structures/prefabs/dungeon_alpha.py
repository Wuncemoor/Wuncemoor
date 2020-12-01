from abstracts.abstract_structure import PrefabStructure
from structures.prefabs.arrays.town_alpha import mage_house_blocker_array, mage_house_overhead_array, \
    mayor_house_blocker_array, \
    mayor_house_overhead_array, guard_hut_blocker_array, guard_hut_overhead_array, church_blocker_array, \
    church_floor_array, \
    church_overhead_array, orphanage_blocker_array, orphanage_overhead_array, inn_blocker_array, inn_overhead_array, \
    tavern_blocker_array, tavern_overhead_array, mage_house_floor_array, guard_hut_floor_array, orphanage_floor_array, \
    tavern_floor_array, inn_floor_array, mayor_house_floor_array
from world_objects.rect import Rect


class TownAlphaMageHouse(PrefabStructure):
    _floors = mage_house_floor_array()
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
                tile.floor = self._floors[j][i]
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaMayorHouse(PrefabStructure):
    _floors = mayor_house_floor_array()
    _blockers = mayor_house_blocker_array()
    _overhead = mayor_house_overhead_array()
    rect = Rect(43, 7, 14, 12)
    is_interior = True

    def __init(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floors[j][i]
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaGuardHut(PrefabStructure):
    _floors = guard_hut_floor_array()
    _blockers = guard_hut_blocker_array()
    _overhead = guard_hut_overhead_array()
    rect = Rect(14, 42, 7, 15)
    is_interior = True

    def __init(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floors[j][i]
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaChurch(PrefabStructure):
    _floors = church_floor_array()
    _blockers = church_blocker_array()
    _overhead = church_overhead_array()
    rect = Rect(84, 18, 7, 13)
    is_interior = True

    def __init(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floors[j][i]
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaOrphanage(PrefabStructure):
    _floors = orphanage_floor_array()
    _blockers = orphanage_blocker_array()
    _overhead = orphanage_overhead_array()
    rect = Rect(69, 14, 13, 10)
    is_interior = True

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floors[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaInn(PrefabStructure):
    _floors = inn_floor_array()
    _blockers = inn_blocker_array()
    _overhead = inn_overhead_array()
    rect = Rect(76, 42, 11, 10)
    is_interior = True

    def __init__(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floors[j][i]
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaTavern(PrefabStructure):
    _floors = tavern_floor_array()
    _blockers = tavern_blocker_array()
    _overhead = tavern_overhead_array()
    rect = Rect(72, 53, 17, 9)
    is_interior = True

    def __init(self):
        super().__init__()
        self.fill_tiles()
        self.set_transitions()

    def fill_tiles(self):
        i, j = 0, 0
        for row in self.tiles:
            for tile in row:
                tile.floor = self._floors[j][i]
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


