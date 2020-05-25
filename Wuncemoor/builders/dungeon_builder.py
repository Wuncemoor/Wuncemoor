import tcod as libtcod
from entity import Entity
from render_functions import RenderOrder
from components.stairs import Stairs
from loader_functions.constants import get_constants
from map_objects.dungeon import Dungeon
from map_objects.map import Map


class DungeonDirector:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_dungeon(self):
        dungeon = Dungeon('NAME_UNDEFINED', 'FLOORS_UNDEFINED', 'MAPS_UNDEFINED', 'NODEPOWER_UNDEFINED')

        name = self.__builder.get_name()
        dungeon.set_name(name)

        floors = self.__builder.get_floors()
        dungeon.set_floors(floors)

        maps = self.__builder.get_maps()
        dungeon.set_maps(maps)

        np = self.__builder.get_np()
        dungeon.set_node_power(np)

        return dungeon


class DungeonBuilder:

    def __init__(self, basename, subtype, floors, width, height, np, boss_obj):
        self.basename = basename
        self.floors = floors
        self.width = width
        self.height = height
        self.subtype = subtype
        self.np = np
        self.boss_obj = boss_obj

    def initialize_maps(self):

        map = Map(self.width, self.height)
        map.initialize_tiles()

        return map

    @property
    def name(self):
        if self.subtype is None:
            return self.basename
        else:
            return self.subtype + '_' + self.basename

    def get_name(self):
        return self.name

    def get_floors(self):
        return self.floors

    def get_np(self):
        return self.np

    def get_maps(self):

        maps = []
        constants = get_constants()
        objs = constants.get('images').get('entities')

        # Make a blank map for each floor in the dungeon
        for i in range(self.floors):
            map = self.initialize_maps()
            map.dungeon_level = i + 1
            map.set_floor_image(self.basename)
            maps.append(map)

        # Fill in the maps except for stairs
        for map in maps:
            map.fill_map(self.basename, self.subtype, self.np, constants['max_rooms'], constants['room_min_size'],
                         constants['room_max_size'], constants['map_width'], constants['map_height'],
                         objs)

        current_floor = 0

        # Fill in stairs connecting floors except for dungeon connection to world
        while current_floor < self.floors:

            downstairsimg = objs.get('transitions').get('down')
            upstairsimg = objs.get('transitions').get('up')

            if current_floor == 0:

                # Don't know where you're coming from, leave entrance blank, gets filled in world map building
                exit_stairs_component = Stairs('Stairs going deeper', downstairsimg, self.name, current_floor + 1,
                                               maps[current_floor + 1].entrance)
                exit_stairs = Entity(maps[current_floor].exit[0], maps[current_floor].exit[1], libtcod.white,
                                     render_order=RenderOrder.STAIRS, stairs=exit_stairs_component)
                maps[current_floor].transitions.append(exit_stairs)
                current_floor += 1

            elif current_floor < (self.floors - 1):

                entrance_stairs_component = Stairs('Stairs going up', upstairsimg, self.name, current_floor - 1,
                                                   maps[current_floor - 1].exit)
                entrance_stairs = Entity(maps[current_floor].entrance[0], maps[current_floor].entrance[1],
                                         libtcod.white, render_order=RenderOrder.STAIRS,
                                         stairs=entrance_stairs_component)
                exit_stairs_component = Stairs('Stairs going deeper', downstairsimg, self.name, current_floor + 1,
                                               maps[current_floor + 1].entrance)
                exit_stairs = Entity(maps[current_floor].exit[0], maps[current_floor].exit[1], libtcod.white,
                                     render_order=RenderOrder.STAIRS, stairs=exit_stairs_component)
                maps[current_floor].transitions.append(entrance_stairs)
                maps[current_floor].transitions.append(exit_stairs)
                current_floor += 1

            elif current_floor == (self.floors - 1):

                # Deepest floor has no stairs to go deeper
                entrance_stairs_component = Stairs('Stairs going up', upstairsimg, self.name, current_floor - 1,
                                                   maps[current_floor - 1].exit)
                entrance_stairs = Entity(maps[current_floor].entrance[0], maps[current_floor].entrance[1],
                                         libtcod.white, render_order=RenderOrder.STAIRS,
                                         stairs=entrance_stairs_component)
                maps[current_floor].transitions.append(entrance_stairs)
                current_floor += 1

        maps[-1].add_boss(self.basename, self.subtype, self.np, self.boss_obj)
        return maps
