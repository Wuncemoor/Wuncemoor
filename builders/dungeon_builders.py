import tcod as libtcod
from ECS.entity import Entity
from abstracts.abstract_dungeon_builder import AbstractDungeonBuilder
from config.constants import OVERWORLD, DUNGEON_ALPHA, DUNGEON_DELTA, DUNGEON_GAMMA, DUNGEON_BETA
from dungeons.mixins import InitDangerousMap, InitSafeMap
from enums.render_order import RenderOrder
from ECS.__entity.transition import Transition
from config.image_objects import STAIRS_DOWN, STAIRS_UP, BUNDLE_ALPHA
from map_objects.rectangle import Rect
from map_objects.road import Road
from dungeons.dungeon_alpha import DungeonAlphaMixin
from dungeons.overworld.biome_mixin import BiomeMixin
from dungeons.overworld.plot_mixin import PlotMixin


class CaveBuilder(AbstractDungeonBuilder, InitDangerousMap):

    def get_maps(self):

        maps = []

        # Make a blank map for each floor in the dungeon
        for i in range(self.floors):
            map = self.initialize_map()
            map.dungeon_level = i + 1
            maps.append(map)

        # Fill in the maps except for stairs
        for map in maps:
            map.fill_tiles(self.basename, self.subtype, self.np)

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


class OverworldBuilder(InitDangerousMap, AbstractDungeonBuilder, BiomeMixin, PlotMixin):

    def __init__(self):
        self.basename = 'overworld'
        self.subtype = None
        self.floors = 1
        self.width, self.height = OVERWORLD
        self.np = 1

    def get_maps(self):
        map = self.initialize_map()
        self.apply_simplex_biomes(map)
        return [map]


class DungeonAlphaBuilder(InitSafeMap, AbstractDungeonBuilder, DungeonAlphaMixin):

    def __init__(self, node):
        self.basename = 'alpha'
        self.subtype = None
        self.floors = 1
        self.width, self.height = DUNGEON_ALPHA
        self.np = 0
        self.node = node

    def get_maps(self):
        map = self.initialize_map()

        rect = Rect(0, int(self.height / 2) - 2, self.width, 4)
        road = Road(rect, 'overworld', 0, (self.node.x, self.node.y), BUNDLE_ALPHA)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.add_road(road)
        samwise = self.get_samwise()

        map.noncombatants.append(samwise)

        return [map]
        # convert to add_structures later
        # add_house(floor, 10, int(height / 2) - 8)
        # add_hut(floor, 30, int(height / 2) - 19)

        # equippable_test = EquippableBuilder(499)
        # director = Director()
        #
        # director.set_builder(equippable_test)
        # equippable = director.get_equippable()
        # item_component = Item(equippable=equippable)
        # test_gear = Entity(20, 20, blocks=False, render_order=RenderOrder.ITEM, item=item_component)
        #
        # floor.entities.append(test_gear)
        #
        # Get samwise but only in first town


class DungeonBetaBuilder(InitSafeMap, AbstractDungeonBuilder):

    def __init__(self, node):
        self.basename = 'beta'
        self.subtype = None
        self.floors = 1
        self.width, self.height = DUNGEON_BETA
        self.np = 0
        self.node = node

    def get_maps(self):
        map = self.initialize_map()

        rect = Rect(0, int(self.height / 2) - 2, self.width, 4)
        road = Road(rect, 'overworld', 0, (self.node.x, self.node.y), BUNDLE_ALPHA)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.add_road(road)
        return [map]


class DungeonGammaBuilder(InitSafeMap, AbstractDungeonBuilder):

    def __init__(self, node):
        self.basename = 'gamma'
        self.subtype = None
        self.floors = 1
        self.width, self.height = DUNGEON_GAMMA
        self.np = 0
        self.node = node

    def get_maps(self):
        map = self.initialize_map()

        rect = Rect(0, int(self.height / 2) - 2, self.width, 4)
        road = Road(rect, 'overworld', 0, (self.node.x, self.node.y), BUNDLE_ALPHA)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.add_road(road)
        return [map]


class DungeonDeltaBuilder(InitSafeMap, AbstractDungeonBuilder):

    def __init__(self, node):
        self.basename = 'delta'
        self.subtype = None
        self.floors = 1
        self.width, self.height = DUNGEON_DELTA
        self.np = 0
        self.node = node

    def get_maps(self):
        map = self.initialize_map()

        rect = Rect(0, int(self.height / 2) - 2, self.width, 4)
        road = Road(rect, 'overworld', 0, (self.node.x, self.node.y), BUNDLE_ALPHA)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.add_road(road)
        return [map]
