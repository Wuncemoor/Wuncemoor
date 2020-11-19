from ECS.__entity.shopkeeper import Shopkeeper
from ECS.entity import Entity
from ECS.__entity.age import Age
from ECS.__entity.noncombatant import Noncombatant
from builders.make_item import make_item
from config.image_objects import BUNDLE_SAMWISE
from dialogue.get_dialogue import get_samwise_dialogue
from enums.render_order import RenderOrder
from handlers.menus.inventory import Inventory
from map_objects.majorroad import MajorRoad
from map_objects.rect import Rect
from map_objects.town_walls import TownWalls
from prefabs.alpha_prefabs import TownAlphaInn, TownAlphaMageHouse


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
        samwise = Entity(6, 34, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age, shopkeeper=shopkeeper)
        return samwise

    def get_major_road(self, outer_scenery_dim):
        rect = Rect(outer_scenery_dim, int(self.height / 2) - 2, self.width - outer_scenery_dim*2, 4)
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        return road

    @staticmethod
    def get_prefab_structures():
        structures = [TownAlphaInn(), TownAlphaMageHouse()]
        return structures

    def get_town_walls(self, outer_scenery_dim):
        rect = Rect(outer_scenery_dim, outer_scenery_dim, self.width - outer_scenery_dim*2, self.height - outer_scenery_dim*2)
        walls = TownWalls(rect, 'stone')
        return walls




