
from entity import Entity
from render_functions import RenderOrder
from builders.dungeon_builder import DungeonDirector, DungeonBuilder
from builders.random_item_maker import EquippableBuilder, Director
from map_objects.rectangle import Rect
from map_objects.map import Map
from map_objects.dungeon import Dungeon
from map_objects.object_files.get_structures import get_house_obj, get_town_obj, get_hut_obj
from map_objects.structure import Structure
from map_objects.road import Road
from components.item import Item


def get_town(width, height):

    map = get_map(width, height)
    rect = Rect(0, 0, width - 1, height - 1)
    map.create_room(rect)

    road = Road(Rect(0, int(height/2) -2, width, 4), 'goblin_cave', 0, (30,30))
    road.set_transitions('vertical')
    map.floor_image = 'grass'
    map.add_road(road)
    house = Structure(Rect(10, int(height/2)-8, 5, 6), get_house_obj())
    town = Structure(Rect(70, int(height/2)-6, 8, 4), get_town_obj())
    hut = Structure(Rect(30, int(height/2)- 19, 17, 17), get_hut_obj())
    map.structures.append(hut)
    map.structures.append(house)
    map.structures.append(town)

    equippable_test = EquippableBuilder(499)
    director = Director()

    director.set_builder(equippable_test)
    equippable_component = director.get_equippable()
    item_component = Item(equippable_component=equippable_component)
    test_gear = Entity(20, 20, blocks=False, render_order=RenderOrder.ITEM, item=item_component)

    map.map_entities.append(test_gear)



    town = Dungeon('town', 1, [map], np=0)

    return town

    
def get_cave(constants, subtype):

    dungeon_builder = DungeonBuilder('cave', subtype, 5, constants['map_width'], constants['map_height'], 75)
    dungeon_director = DungeonDirector()
    dungeon_director.set_builder(dungeon_builder)
    cave = dungeon_director.get_dungeon()
    
    return cave
    
def get_map(width, height):
    

    map = Map(width, height)
    map.initialize_tiles()
    
    return map

#def get_world_map(width, height):
