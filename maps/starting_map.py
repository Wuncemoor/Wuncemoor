from ECS.entity import Entity
from render_functions import RenderOrder
from builders.dungeon_builder import DungeonDirector, DungeonBuilder
from builders.random_item_maker import EquippableBuilder, Director
from map_objects.rectangle import Rect
from map_objects.map import Map
from map_objects.dungeon import Dungeon
from map_objects.road import Road
from maps.world_map.biome_functions import apply_simplex_biomes
from maps.world_map.core_nodes import get_core_plot_nodes
from maps.town.add_structure import add_house, add_hut, add_town
from ECS.__entity.item import Item
from ECS.__entity.transition import Transition
from ECS.__entity.noncombatant import Noncombatant
from random import randint
from dialogue.get_dialogue import get_samwise_dialogue


def get_town(width, height, node, img_objs):
    name, node_x, node_y = node.name, node.x, node.y

    map = get_map(width, height, name)

    ents = img_objs.get('entities')

    alpha = ents.get('transitions').get('alpha')
    road = Road(Rect(0, int(height / 2) - 2, width, 4), 'world', 0, (node_x, node_y), alpha)
    road.set_transitions('vertical')
    map.floor_image = 'grass'
    # add_road also adds transitions
    map.add_road(road)
    # convert to add_structures later
    add_house(map, 10, int(height / 2) - 8)
    add_hut(map, 30, int(height / 2) - 19)
    add_town(map, 70, int(height / 2) - 6)

    equippable_test = EquippableBuilder(499, ents.get('items').get('equippables').get('weapons'))
    director = Director()

    director.set_builder(equippable_test)
    equippable_component = director.get_equippable()
    item_component = Item(equippable_component=equippable_component)
    test_gear = Entity(20, 20, blocks=False, render_order=RenderOrder.ITEM, item=item_component)

    map.map_entities.append(test_gear)

    # Get samwise but only in first town
    if name == 'town':

        samwise_obj = ents.get('noncombatants').get('samwise')
        samwise_portrait = img_objs.get('portraits').get('samwise')
        dialogue = get_samwise_dialogue()
        noncom = Noncombatant('samwise', samwise_obj, dialogue, samwise_portrait)
        samwise = Entity(38, 16, blocks=False, render_order=RenderOrder.ACTOR, noncombatant=noncom)

        map.noncombatants.append(samwise)

    town = Dungeon(name, 1, [map], np=0)

    return town


def get_cave(constants, images, subtype):
    dungeon_builder = DungeonBuilder('cave', subtype, 5, constants['map_width'], constants['map_height'], 75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    cave = dungeon_director.get_dungeon(constants, images)

    return cave


def get_map(width, height, variant=None):

    map = Map(width, height, variant=variant)

    if variant in ('town', 'second_town', 'third_town', 'fourth_town'):

        map.create_room(Rect(0, 0, width - 1, height - 1))
    elif variant == 'world_map':
        for row in map.tiles:
            for tile in row:
                tile.blocked = False
                tile.block_sight = False

    return map


def get_world_map(constants, alpha_img):
    map = get_map(constants['width'], constants['height'], variant='world_map')
    apply_simplex_biomes(map, constants)
    apply_mode(map)
    nodes = get_core_plot_nodes(constants['width'], constants['height'])
    for node in nodes:
        add_town(map, node.x, node.y)
        stairs = Transition('Stairs', alpha_img, node.name, 0, node.entrance)
        ent = Entity(node.x, node.y, transition=stairs)
        map.transitions.append(ent)

    world = Dungeon('world', 1, [map], np=0)
    return world, nodes


def apply_mode(map):
    for row in map.tiles:
        for tile in row:
            tile.mode = str(randint(0, 8))
