from entities.prefabs.dungeon_alpha import get_samwise, get_mage, get_guard_captain, get_priest, get_rogue, get_homer, \
    get_mayor, get_innkeeper, get_tavernkeeper
from world_objects.majorroad import MajorRoad
from world_objects.rect import Rect
from world_objects.town_walls import TownWalls
from structures.prefabs.dungeon_alpha import TownAlphaInn, TownAlphaMageHouse, TownAlphaMageHousePathway, \
    TownAlphaMayorHousePathway, TownAlphaMayorHouse, TownAlphaGuardHut, TownAlphaGuardHutPathway1, \
    TownAlphaGuardHutPathway2, TownAlphaTavern, TownAlphaTavernPathway1, TownAlphaChurch, TownAlphaChurchPathway, \
    TownAlphaMarketSquare, TownAlphaOrphanage, TownAlphaOrphanagePathway, TownAlphaInnTavernPathway, \
    TownAlphaInnPathway, TownAlphaTavernPathway2, TownAlphaMageGarden, TownAlphaGuardTrainingGrounds, \
    TownAlphaChurchGraveyard


class DungeonAlphaMixin:
    """Mixin for DungeonAlphaBuilder, adds functionality unique to starting town"""

    @staticmethod
    def get_noncombatants():
        noncombatants = [get_samwise(), get_mage(), get_guard_captain(), get_priest(), get_rogue(), get_homer(), get_mayor(), get_innkeeper(), get_tavernkeeper()]
        return noncombatants

    def get_major_road(self, outer_scenery_dim):
        rect = Rect(outer_scenery_dim, int(self.height / 2) - 2, self.width - outer_scenery_dim*2, 4)
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        return road

    @staticmethod
    def get_prefab_structures():
        structures = [TownAlphaInn(), TownAlphaInnPathway(), TownAlphaMageHouse(), TownAlphaMageGarden(), TownAlphaMageHousePathway(), TownAlphaMayorHouse(),
                      TownAlphaMayorHousePathway(), TownAlphaGuardHut(), TownAlphaGuardTrainingGrounds(), TownAlphaGuardHutPathway1(), TownAlphaTavern(),
                      TownAlphaGuardHutPathway2(), TownAlphaChurch(), TownAlphaChurchGraveyard(), TownAlphaChurchPathway(), TownAlphaMarketSquare(), TownAlphaOrphanage(), TownAlphaOrphanagePathway(), TownAlphaInnTavernPathway(), TownAlphaTavernPathway1(), TownAlphaTavernPathway2()]
        return structures

    def get_town_walls(self, outer_scenery_dim):
        rect = Rect(outer_scenery_dim, outer_scenery_dim, self.width - outer_scenery_dim*2, self.height - outer_scenery_dim*2)
        walls = TownWalls(rect, 'stone')
        return walls




