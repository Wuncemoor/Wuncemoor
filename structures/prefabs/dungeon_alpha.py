from abstracts.abstract_structure import PrefabStructure
from structures.prefabs.arrays.town_alpha import mage_house_blocker_array, mage_house_overhead_array, \
    mayor_house_blocker_array, \
    mayor_house_overhead_array, guard_hut_blocker_array, guard_hut_overhead_array, church_blocker_array, \
    church_overhead_array, orphanage_blocker_array, orphanage_overhead_array, inn_blocker_array, inn_overhead_array, \
    tavern_blocker_array, tavern_overhead_array, mage_house_floor_array
from world_objects.floors.outside_floors import DirtTileFloor
from world_objects.floors.wood_floors import WoodPlankTileFloor
from world_objects.rect import Rect


class TownAlphaMageHouse(PrefabStructure):

    floor_component = WoodPlankTileFloor
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


class TownAlphaMageGarden(PrefabStructure):
    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(20, 7, 10, 8)
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


class TownAlphaMayorHouse(PrefabStructure):

    floor_component = DirtTileFloor
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
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaMayorHousePathway(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(49, 19, 3, 16)
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


class TownAlphaGuardHut(PrefabStructure):
    floor_component = DirtTileFloor
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
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaGuardTrainingGrounds(PrefabStructure):
    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(8, 59, 13, 7)
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


class TownAlphaGuardHutPathway1(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(8, 39, 3, 12)
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


class TownAlphaGuardHutPathway2(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(11, 48, 3, 3)
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


class TownAlphaChurch(PrefabStructure):
    floor_component = DirtTileFloor
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
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaChurchGraveyard(PrefabStructure):
    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(83, 8, 9, 8)
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

class TownAlphaChurchPathway(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(86, 31, 3, 4)
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


class TownAlphaMarketSquare(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(36, 30, 28, 14)
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


class TownAlphaOrphanage(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = orphanage_blocker_array()
    _overhead = orphanage_overhead_array()
    rect = Rect(69, 14, 13, 10)
    is_interior = True

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


class TownAlphaOrphanagePathway(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(74, 24, 3, 11)
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



class TownAlphaInn(PrefabStructure):

    floor_component = DirtTileFloor
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
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaTavern(PrefabStructure):
    floor_component = DirtTileFloor
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
                tile.floor = DirtTileFloor()
                tile.blocker = self._blockers[j][i]
                i += 1
            j += 1
            i = 0

    def set_transitions(self):
        pass


class TownAlphaTavernPathway1(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(79, 64, 11, 3)
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


class TownAlphaTavernPathway2(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(79, 62, 3, 2)
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

class TownAlphaInnTavernPathway(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(90, 39, 3, 28)
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

class TownAlphaInnPathway(PrefabStructure):

    floor_component = DirtTileFloor
    _blockers = None
    _overhead = None
    rect = Rect(87, 45, 3, 3)
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