from ECS.__entity.shopkeeper import Shopkeeper
from ECS.entity import Entity
from ECS.__entity.age import Age
from ECS.__entity.noncombatant import Noncombatant
from builders.make_item import make_item
from config.image_objects import BUNDLE_SAMWISE
from dialogue.get_dialogue import get_samwise_dialogue
from enums.render_order import RenderOrder
from handlers.menus.inventory import Inventory
from world_objects.majorroad import MajorRoad
from world_objects.rect import Rect
from world_objects.town_walls import TownWalls
from prefabs.alpha_prefabs import TownAlphaInn, TownAlphaMageHouse, TownAlphaMageHousePathway, \
    TownAlphaMayorHousePathway, TownAlphaMayorHouse, TownAlphaGuardHut, TownAlphaGuardHutPathway1, \
    TownAlphaGuardHutPathway2, TownAlphaTavern, TownAlphaTavernPathway1, TownAlphaChurch, TownAlphaChurchPathway, \
    TownAlphaMarketSquare, TownAlphaOrphanage, TownAlphaOrphanagePathway, TownAlphaInnTavernPathway, \
    TownAlphaInnPathway, TownAlphaTavernPathway2, TownAlphaMageGarden, TownAlphaGuardTrainingGrounds, \
    TownAlphaChurchGraveyard


class DungeonAlphaMixin:
    """Mixin for DungeonAlphaBuilder, adds functionality unique to starting town"""

    @staticmethod
    def get_samwise():

        dialogue = get_samwise_dialogue()
        noncom = Noncombatant('samwise', BUNDLE_SAMWISE, dialogue)
        age = Age(13, 12, 28, 0, (1, 4))
        inven = Inventory()
        potion = make_item('healing_potion')
        inven.add_item(potion)
        shopkeeper = Shopkeeper(inven)
        samwise = Entity(73, 24, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age, shopkeeper=shopkeeper)
        return samwise

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




