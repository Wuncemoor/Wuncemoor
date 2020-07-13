from ECS.entity import Entity
from enums.render_order import RenderOrder
from builders.dungeon_builder import DungeonDirector, DungeonBuilder
from builders.random_item_maker import EquippableBuilder, Director
from map_objects.rectangle import Rect
from map_objects.floor import Floor
from map_objects.dungeon import Dungeon
from map_objects.road import Road
from maps.world_map.biome_functions import apply_simplex_biomes
from maps.world_map.core_nodes import get_core_plot_nodes
from maps.town.add_structure import add_house, add_hut, add_town
from ECS.__entity.item import Item
from ECS.__entity.transition import Transition
from ECS.__entity.noncombatant import Noncombatant
from ECS.__entity.age import Age
from random import randint
from dialogue.get_dialogue import get_samwise_dialogue
from config.constants import OVERWORLD, START_TOWN, CAVE
from config.image_objects import ALPHA, BUNDLE_SAMWISE


def get_town(node):
    (width, height) = START_TOWN
    name, node_x, node_y = node.name, node.x, node.y

    floor = get_floor(width, height, variant=name)

    road = Road(Rect(0, int(height / 2) - 2, width, 4), 'world', 0, (node_x, node_y), ALPHA)
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


def get_floor(width, height, variant=None, subtype=None, dangerous=False):

    floor = Floor(width, height, variant=variant, dangerous=dangerous)

    if variant in ('town', 'second_town', 'third_town', 'fourth_town'):

        floor.create_room(Rect(0, 0, width - 1, height - 1), 'town', subtype)
    elif variant == 'overworld':
        for row in floor.tiles:
            for tile in row:
                tile.blocked = False
                tile.block_sight = False

    return floor


def overworld():
    (width, height) = OVERWORLD

    floor = get_floor(width, height, variant='overworld', dangerous=True)
    apply_simplex_biomes(floor)
    apply_mode(floor)
    nodes = get_core_plot_nodes(width, height)
    for node in nodes:
        add_town(floor, node.x, node.y)
        stairs = Transition('Stairs', ALPHA, node.name, 0, node.entrance)
        ent = Entity(node.x, node.y, transition=stairs)
        floor.transitions.append(ent)

    world = Dungeon('world', 1, [floor], np=0)
    return world, nodes


def apply_mode(floor):
    for row in floor.tiles:
        for tile in row:
            tile.mode = str(randint(0, 8))
