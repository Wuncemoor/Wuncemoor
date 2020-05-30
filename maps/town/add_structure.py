from map_objects.structure import Structure
from map_objects.rectangle import Rect
from map_objects.object_files.get_structures import get_house_obj, get_town_obj, get_hut_obj

def add_house(map, x, y):
    house = Structure(Rect(x, y, 5, 6), get_house_obj())
    map.structures.append(house)

def add_town(map, x, y):
    town = Structure(Rect(x, y, 8, 4), get_town_obj())
    map.structures.append(town)

def add_hut(map, x, y):
    hut = Structure(Rect(x, y, 17, 17), get_hut_obj())
    map.structures.append(hut)
