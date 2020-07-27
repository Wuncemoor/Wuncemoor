from ECS.__entity.age import Age
from ECS.__entity.item import Item
from ECS.__entity.noncombatant import Noncombatant
from ECS.entity import Entity
from builders.dungeon_builders import OverworldBuilder
from builders.random_item_maker import EquippableBuilder, Director
from config.constants import OVERWORLD, START_TOWN, CAVE
from config.image_objects import BUNDLE_ALPHA, BUNDLE_SAMWISE
from dialogue.get_dialogue import get_samwise_dialogue
from enums.render_order import RenderOrder
from map_objects.dungeon import Dungeon
from map_objects.rectangle import Rect
from map_objects.road import Road


class DungeonDirector:
    def __init__(self):
        self.builder = None

    def overworld(self):
        (width, height) = OVERWORLD
        self.builder = OverworldBuilder('overworld', None, 1, width, height, 0)
        overworld = self.get_dungeon()

        return overworld

    def get_dungeon(self):
        dungeon = Dungeon('NAME_UNDEFINED', 'FLOORS_UNDEFINED', 'MAPS_UNDEFINED', 'NODEPOWER_UNDEFINED')

        name = self.__builder.get_name()
        dungeon.name = name

        floors = self.__builder.get_floors()
        dungeon.floors = floors

        maps = self.__builder.get_maps()
        dungeon.maps = maps

        np = self.__builder.get_np()
        dungeon.np = np

        return dungeon


def get_town(node):
    (width, height) = START_TOWN
    name, node_x, node_y = node.name, node.x, node.y

    floor = get_floor(width, height, variant=name)

    road = Road(Rect(0, int(height / 2) - 2, width, 4), 'world', 0, (node_x, node_y), BUNDLE_ALPHA)
    road.set_transitions('vertical')
    floor.floor_image = 'grass'
    # add_road also adds transitions
    floor.add_road(road)
    # convert to add_structures later
    add_house(floor, 10, int(height / 2) - 8)
    add_hut(floor, 30, int(height / 2) - 19)
    add_town(floor, 70, int(height / 2) - 6)

    equippable_test = EquippableBuilder(499)
    director = Director()

    director.set_builder(equippable_test)
    equippable = director.get_equippable()
    item_component = Item(equippable=equippable)
    test_gear = Entity(20, 20, blocks=False, render_order=RenderOrder.ITEM, item=item_component)

    floor.entities.append(test_gear)

    # Get samwise but only in first town
    if name == 'town':

        dialogue = get_samwise_dialogue()
        noncom = Noncombatant('samwise', BUNDLE_SAMWISE, dialogue)
        age = Age(13, 12, 28, 0, (1, 4))
        samwise = Entity(18, 16, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom, age=age)

        floor.noncombatants.append(samwise)

    town = Dungeon(name, 1, [floor], np=0)

    return town


def get_cave(subtype):
    (width, height) = CAVE
    dungeon_builder = DungeonBuilder('cave', subtype, 5, width, height, 75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    cave = dungeon_director.get_dungeon()

    return cave

