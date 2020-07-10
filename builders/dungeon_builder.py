import tcod as libtcod
from ECS.entity import Entity
from enums.render_order import RenderOrder
from ECS.__entity.transition import Transition
from map_objects.dungeon import Dungeon
from map_objects.floor import Floor
from config.image_objects import STAIRS_DOWN, STAIRS_UP



class DungeonDirector:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

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


class DungeonBuilder:

    def __init__(self, basename, subtype, floors, width, height, np):
        self.basename = basename
        self.floors = floors
        self.width = width
        self.height = height
        self.subtype = subtype
        self.np = np


    def initialize_maps(self):

        map = Floor(self.width, self.height, variant=self.basename, dangerous=True)
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

        # Make a blank map for each floor in the dungeon
        for i in range(self.floors):
            map = self.initialize_maps()
            map.dungeon_level = i + 1
            maps.append(map)

        # Fill in the maps except for stairs
        for map in maps:
            map.fill_floor(self.basename, self.subtype, self.np)


        current_floor = 0

        # Fill in stairs connecting floors except for dungeon connection to world
        while current_floor < self.floors:

            downstairsimg = STAIRS_DOWN
            upstairsimg = STAIRS_UP

            if current_floor == 0:

                # Don't know where you're coming from, leave entrance blank, gets filled in world map building
                exit_stairs_component = Transition('Stairs going deeper', downstairsimg, self.name, current_floor + 1,
                                               maps[current_floor + 1].entrance)
                exit_stairs = Entity(maps[current_floor].exit[0], maps[current_floor].exit[1], libtcod.white,
                                     render_order=RenderOrder.STAIRS, transition=exit_stairs_component)
                maps[current_floor].transitions.append(exit_stairs)
                current_floor += 1

            elif current_floor < (self.floors - 1):

                entrance_stairs_component = Transition('Stairs going up', upstairsimg, self.name, current_floor - 1,
                                                   maps[current_floor - 1].exit)
                entrance_stairs = Entity(maps[current_floor].entrance[0], maps[current_floor].entrance[1],
                                         libtcod.white, render_order=RenderOrder.STAIRS,
                                         transition=entrance_stairs_component)
                exit_stairs_component = Transition('Stairs going deeper', downstairsimg, self.name, current_floor + 1,
                                               maps[current_floor + 1].entrance)
                exit_stairs = Entity(maps[current_floor].exit[0], maps[current_floor].exit[1], libtcod.white,
                                     render_order=RenderOrder.STAIRS, transition=exit_stairs_component)
                maps[current_floor].transitions.append(entrance_stairs)
                maps[current_floor].transitions.append(exit_stairs)
                current_floor += 1

            elif current_floor == (self.floors - 1):

                # Deepest floor has no stairs to go deeper
                entrance_stairs_component = Transition('Stairs going up', upstairsimg, self.name, current_floor - 1,
                                                   maps[current_floor - 1].exit)
                entrance_stairs = Entity(maps[current_floor].entrance[0], maps[current_floor].entrance[1],
                                         libtcod.white, render_order=RenderOrder.STAIRS,
                                         transition=entrance_stairs_component)
                maps[current_floor].transitions.append(entrance_stairs)
                current_floor += 1

        maps[-1].add_boss(self.basename, self.subtype, self.np)
        return maps
