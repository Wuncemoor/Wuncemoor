
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
from opensimplex import OpenSimplex
import random

def get_town(width, height):

    map = get_map(width, height)
    rect = Rect(0, 0, width - 1, height - 1)
    map.create_room(rect)

    road = Road(Rect(0, int(height/2) -2, width, 4), 'world', 0, (30,30))
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


def get_world_map(constants):

    map = get_map(constants['width'], constants['height'])
    for row in map.tiles:
        for tile in row:
            tile.blocked = False
            tile.block_sight = False
    equator = constants['height'] / 2

    heightmesh = OpenSimplex(seed=random.randint(1, 1000000))
    heightmesh2 = OpenSimplex(seed=random.randint(1, 1000000))
    heightmesh3 = OpenSimplex(seed=random.randint(1, 1000000))
    moistmesh = OpenSimplex(seed=random.randint(1, 1000000))
    moistmesh2 = OpenSimplex(seed=random.randint(1, 1000000))
    moistmesh3 = OpenSimplex(seed=random.randint(1, 1000000))

    for j in range(constants['height']):

        tempdiff = abs(equator - j) / equator

        for i in range(constants['width']):

            amp = 1
            freq = 1
            height = 0
            moist = 0
            temp = 1 - tempdiff

            for k in range(constants['octaves']):
                octavex = j * constants['scale'] * freq
                octavey = i * constants['scale'] * freq

                hvalue = heightmesh.noise2d(x=octavex, y=octavey)
                hvalue2 = heightmesh2.noise2d(x=octavex, y=octavey)
                hvalue3 = heightmesh3.noise2d(x=octavex, y=octavey)
                mvalue = moistmesh.noise2d(x=octavex, y=octavey)
                mvalue2 = moistmesh2.noise2d(x=octavex, y=octavey)
                mvalue3 = moistmesh3.noise2d(x=octavex, y=octavey)
                height += avg([hvalue, hvalue2, hvalue3]) * amp
                moist += avg([mvalue, mvalue2, mvalue3]) * amp

                amp *= constants['persist']
                freq *= constants['lacuna']
            heightmod = (abs(height)) * .7
            temp -= heightmod
            moist -= heightmod
            moist += constants['moist_mod']
            temp += constants['temp_mod']
            templist = [('very_hot', 5 / 6), ('hot', 4 / 6), ('warm', 3 / 6), ('cool', 2 / 6), ('cold', 1 / 6),
                        ('very_cold', 0), ('polar', -10)]

            if height <= constants['water_level']:
                if height > 0:
                    map.tiles[i][j].type = 'shallow'
                else:
                    map.tiles[i][j].type = 'deep'

            else:

                temp = temperature(templist, temp)
                moistlist = get_moistlist(temp)
                biome = moisture(moistlist, moist)
                map.tiles[i][j].type = biome

    world = Dungeon('world', 1, [map], np=0)
    return world


def moisture(table, moist_level):
    for (value, level) in table:
        if moist_level >= level:
            return value
    return -1


def get_moistlist(temp):
    dict = {
        'very_hot': [('tropicrain', .6), ('jungle', .2), ('savannah', 0), ('desert', -10)],
        'hot': [('temprain', .5), ('forest', .3), ('savannah', 0), ('desert', -10)],
        'warm': [('temprain', .65), ('forest', .3), ('savannah', 0), ('plains', -.25), ('desert', -10)],
        'cool': [('temprain', .7), ('forest', .2), ('savannah', -.2), ('plains', -.5), ('desert', -10)],
        'cold': [('taiga', 0), ('plains', -10)],
        'very_cold': [('tundra', 0), ('snow', -10)],
        'polar': [('snow', -10)],
    }

    return dict[temp]


def temperature(table, temp_level):
    for (value, level) in table:
        if temp_level >= level:
            return value
    return -1


def avg(list):
    x = 0
    for i in list:
        x += i
    return x / len(list)

