import tcod as libtcod
from entity import Entity
from render_functions import RenderOrder
from builders.random_item_maker import EquippableBuilder, Director
from map_objects.rectangle import Rect
from map_objects.map import Map
from map_objects.tile import Tile
from map_objects.dungeon import Dungeon
from components.stairs import Stairs
from components.item import Item



def get_starting_town(width, height):
    
    tiles = []
    map_entities = []
    starting_map = Map(width, height, tiles,  map_entities)
    tiles = starting_map.initialize_tiles()

    
    town = Rect(0,0,width-1,height-1)
    starting_map.create_room(town)
    
    equippable_test = EquippableBuilder(499)
    director = Director()
    
    director.set_builder(equippable_test)
    equippable_component = director.get_equippable()
    item_component = Item(equippable_component=equippable_component)
    test_gear = Entity(20, 20, libtcod.white, blocks=False, render_order = RenderOrder.ITEM, item=item_component)
    
    starting_map.map_entities.append(test_gear)
    
    town_alpha = Dungeon('start', 1, [starting_map])

    return town_alpha
    
def get_dungeon(width, height):
    
    tiles = []
    map_entities = []
    dungeon = Map(width, height, tiles, map_entities)
    tiles = dungeon.initialize_tiles()
    dungeon.set_dungeon_level(1)
    
    return dungeon
