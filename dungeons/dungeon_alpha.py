from entities.prefabs.dungeon_alpha import get_samwise, get_mage, get_guard_captain, get_priest, get_rogue, get_homer, \
    get_mayor, get_innkeeper, get_tavernkeeper
from structures.procedurals.roads import MajorRoad, Road
from world_objects.rect import Rect
from world_objects.town_walls import TownWalls
from structures.prefabs.dungeon_alpha import TownAlphaInn, TownAlphaMageHouse, TownAlphaMayorHouse, TownAlphaGuardHut, \
    TownAlphaTavern, TownAlphaChurch, TownAlphaOrphanage


class DungeonAlphaMixin:
    """Mixin for DungeonAlphaBuilder, adds functionality unique to starting town"""

    @staticmethod
    def get_noncombatants():
        noncombatants = [get_samwise(), get_mage(), get_guard_captain(), get_priest(), get_rogue(), get_homer(),
                         get_mayor(), get_innkeeper(), get_tavernkeeper()]
        return noncombatants

    def get_major_road(self, outer_scenery_dim):
        rect = Rect(outer_scenery_dim, int(self.height / 2) - 2, self.width - outer_scenery_dim*2, 4)
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        return road

    @staticmethod
    def get_structures():
        inn_road = Road(Rect(87, 45, 3, 3))
        mage_garden = Road(Rect(20, 7, 10, 8))
        mage_road = Road(Rect(11, 16, 3, 19))
        mayor_road = Road(Rect(49, 19, 3, 16))
        guard_grounds = Road(Rect(8, 59, 13, 7))
        guard_road1 = Road(Rect(8, 39, 3, 12))
        guard_road2 = Road(Rect(11, 48, 3, 3))
        church_graveyard = Road(Rect(83, 8, 9, 8))
        church_road = Road(Rect(86, 31, 3, 4))
        market = Road(Rect(36, 30, 28, 14))
        orphan_road = Road(Rect(74, 24, 3, 11))
        inntavern_road = Road(Rect(90, 39, 3, 28))
        tavern_road1 = Road(Rect(79, 64, 11, 3))
        tavern_road2 = Road(Rect(79, 62, 3, 2))

        structures = [TownAlphaInn(), inn_road, TownAlphaMageHouse(), mage_garden, mage_road, TownAlphaMayorHouse(),
                      mayor_road, TownAlphaGuardHut(), guard_grounds, guard_road1, guard_road2, TownAlphaTavern(),
                      TownAlphaChurch(), church_graveyard, church_road, market, TownAlphaOrphanage(), orphan_road, inntavern_road, tavern_road1, tavern_road2]
        return structures

    def get_town_walls(self, outer_scenery_dim):
        rect = Rect(outer_scenery_dim, outer_scenery_dim, self.width - outer_scenery_dim*2, self.height - outer_scenery_dim*2)
        walls = TownWalls(rect, 'stone')
        return walls
