import tcod as libtcod
from entity import Entity
from render_functions import RenderOrder
from builders.dungeon_builder import DungeonDirector, DungeonBuilder
from builders.random_item_maker import EquippableBuilder, Director
from map_objects.rectangle import Rect
from map_objects.map import Map
from map_objects.dungeon import Dungeon
from map_objects.object_files.get_house import get_house_obj
from components.item import Item



def get_town(width, height):

    map = get_map(width, height)
    rect = Rect(0, 0, width - 1, height - 1)
    map.create_room(rect)

    road = Rect(0, int(height/2) -2, width, 4)
    map.add_road(road)
    house_obj = get_house_obj()
    house = ['house', Rect(10, int(height/2)-8, 5, 6), house_obj]
    map.structures.extend(house)

    town = Dungeon('town', 1, [map], np=0)

    return town


def get_starting_town(constants):
    
    starting_map = get_map(constants['alpha_width'], constants['alpha_height'])

    
    town = Rect(0,0,constants['alpha_width']-1,constants['alpha_height']-1)
    starting_map.create_room(town)
    
    equippable_test = EquippableBuilder(499)
    director = Director()
    
    director.set_builder(equippable_test)
    equippable_component = director.get_equippable()
    item_component = Item(equippable_component=equippable_component)
    test_gear = Entity(20, 20, libtcod.white, blocks=False, render_order = RenderOrder.ITEM, item=item_component)
    
    starting_map.map_entities.append(test_gear)
    
    town_alpha = Dungeon('start', 1, [starting_map], np=0)

    return town_alpha
    

def get_directed_dungeon(constants):

    dungeon_builder = DungeonBuilder('directed_dungeon', None, 5, constants['map_width'], constants['map_height'], 0)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    directed_dungeon = dungeon_director.get_dungeon()
    
    return directed_dungeon
    
def get_cave(constants, subtype):

    dungeon_builder = DungeonBuilder('cave', subtype, 5, constants['map_width'], constants['map_height'], 75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    cave = dungeon_director.get_dungeon()
    
    return cave

def get_goblin_cave(constants):
    
    dungeon_builder = DungeonBuilder('goblin_cave', None, 5, constants['map_width'], constants['map_height'],75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    goblin_cave = dungeon_director.get_dungeon()
    
    return goblin_cave
    
def get_kobold_cave(constants):

    dungeon_builder = DungeonBuilder('kobold_cave', None, 5, constants['map_width'], constants['map_height'], 500)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    kobold_cave = dungeon_director.get_dungeon()
    
    return kobold_cave
    
def get_map(width, height):
    
    tiles = []
    map_entities = []
    map = Map(width, height, tiles, map_entities)
    map.initialize_tiles()
    
    return map
    
# def get_world_map(width, height, num_cells):
#
#     tiles = []
#     map_entities = []
#     world_map = Map(width, height, tiles, map_entities)
#     tiles = world_map.initialize_tiles()
#
#
#     vor = voronoi_generate(width, height, num_cells)
#     cont = continents_generate(vor[0],vor[1], vor[2], vor[3], vor[4], vor[5], vor[6])
#     bslist = []
#     for i in cont[1]:
#         if i in cont[2]:
#             bslist.append(i)
#     print(cont[2])
#     print(bslist)
#
#     #for each tile in finalarray
#     for i in cont[0]:
#
#         #if its a continent tile
#         if i[0] in cont[2]:
#
#             world_map.tiles[i[1]][i[2]].blocked = False
#             world_map.tiles[i[1]][i[2]].block_sight = False
#
#     world_dungeon = Dungeon('world', 1, [world_map])
#
#     return world_dungeon

