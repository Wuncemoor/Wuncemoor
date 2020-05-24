
from entity import Entity
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
from components.item import Item
from components.stairs import Stairs
from random import randint



def get_town(width, height, node):

    name, node_x, node_y = node.name, node.x, node.y


    map = get_map(width, height, name)

    road = Road(Rect(0, int(height/2) -2, width, 4), 'world', 0, (node_x, node_y))
    road.set_transitions('vertical')
    map.floor_image = 'grass'
    map.add_road(road)
    add_house(map, 10, int(height / 2) - 8)
    add_hut(map, 30, int(height/2) - 19)
    add_town(map, 70, int(height/2) - 6)


    equippable_test = EquippableBuilder(499)
    director = Director()

    director.set_builder(equippable_test)
    equippable_component = director.get_equippable()
    item_component = Item(equippable_component=equippable_component)
    test_gear = Entity(20, 20, blocks=False, render_order=RenderOrder.ITEM, item=item_component)

    map.map_entities.append(test_gear)

    town = Dungeon(name, 1, [map], np=0)

    return town

    
def get_cave(constants, subtype):

    dungeon_builder = DungeonBuilder('cave', subtype, 5, constants['map_width'], constants['map_height'], 75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    cave = dungeon_director.get_dungeon()
    
    return cave


def get_map(width, height, type=None):
    

    map = Map(width, height)
    map.initialize_tiles()
    if type == 'town' or 'second_town':
        map.create_room(Rect(0, 0, width - 1, height - 1))
    elif type == 'world':
        for row in map.tiles:
            for tile in row:
                tile.blocked = False
                tile.block_sight = False
    
    return map


def get_world_map(constants):

    map = get_map(constants['width'], constants['height'], type='world')
    apply_simplex_biomes(map, constants)
    apply_mode(map)
    nodes = get_core_plot_nodes(constants['width'], constants['height'])
    for node in nodes:
        add_town(map, node.x, node.y)
        stairs = Stairs('Stairs', 'images\\alpha.png', node.name, 0, node.entrance)
        ent = Entity(node.x, node.y, stairs=stairs)
        map.transitions.append(ent)

    world = Dungeon('world', 1, [map], np=0)
    return world, nodes


def apply_mode(map):
    for row in map.tiles:
        for tile in row:
            tile.mode = str(randint(0, 8))


