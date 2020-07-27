
import tcod as libtcod

from ECS.entity import Entity
from abstracts.abstract_builder import DangerousDungeonBuilder
from enums.render_order import RenderOrder
from ECS.__entity.transition import Transition
from config.image_objects import STAIRS_DOWN, STAIRS_UP
from maps.overworld.biome_functions import BiomeMixin
from maps.overworld.core_nodes import PlotMixin


class CaveBuilder(DangerousDungeonBuilder):

    def get_maps(self):

        maps = []

        # Make a blank map for each floor in the dungeon
        for i in range(self.floors):
            map = self.initialize_map()
            map.dungeon_level = i + 1
            maps.append(map)

        # Fill in the maps except for stairs
        for map in maps:
            map.fill_map(self.basename, self.subtype, self.np)

        current_map = 0

        # Fill in transitions connecting maps except for dungeon connection to world
        while current_map < self.floors:

            downstairsimg = STAIRS_DOWN
            upstairsimg = STAIRS_UP

            if current_map == 0:

                # Don't know where you're coming from, leave entrance blank, gets filled in overworld map building
                exit_stairs_component = Transition('Stairs going deeper', downstairsimg, self.name, current_map + 1,
                                               maps[current_map + 1].entrance)
                exit_stairs = Entity(maps[current_map].exit[0], maps[current_map].exit[1], libtcod.white,
                                     render_order=RenderOrder.STAIRS, transition=exit_stairs_component)
                maps[current_map].transitions.append(exit_stairs)
                current_map += 1

            elif current_map < (self.floors - 1):

                entrance_stairs_component = Transition('Stairs going up', upstairsimg, self.name, current_map - 1,
                                                   maps[current_map - 1].exit)
                entrance_stairs = Entity(maps[current_map].entrance[0], maps[current_map].entrance[1],
                                         libtcod.white, render_order=RenderOrder.STAIRS,
                                         transition=entrance_stairs_component)
                exit_stairs_component = Transition('Stairs going deeper', downstairsimg, self.name, current_map + 1,
                                               maps[current_map + 1].entrance)
                exit_stairs = Entity(maps[current_map].exit[0], maps[current_map].exit[1], libtcod.white,
                                     render_order=RenderOrder.STAIRS, transition=exit_stairs_component)
                maps[current_map].transitions.append(entrance_stairs)
                maps[current_map].transitions.append(exit_stairs)
                current_map += 1

            elif current_map == (self.floors - 1):

                # Deepest floor has no stairs to go deeper
                entrance_stairs_component = Transition('Stairs going up', upstairsimg, self.name, current_map - 1,
                                                   maps[current_map - 1].exit)
                entrance_stairs = Entity(maps[current_map].entrance[0], maps[current_map].entrance[1],
                                         libtcod.white, render_order=RenderOrder.STAIRS,
                                         transition=entrance_stairs_component)
                maps[current_map].transitions.append(entrance_stairs)
                current_map += 1

        maps[-1].add_boss(self.basename, self.subtype, self.np)
        return maps


class OverworldBuilder(DangerousDungeonBuilder, BiomeMixin, PlotMixin):

    def get_maps(self):
        map = self.initialize_map()
        self.apply_simplex_biomes(map)
        self.apply_core_plot_nodes(map)
        return map

