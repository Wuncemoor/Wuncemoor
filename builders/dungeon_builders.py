import tcod as libtcod
from ECS.entity import Entity
from abstracts.abstract_dungeon_builder import AbstractDungeonBuilder
from config.constants import OVERWORLD, DUNGEON_ALPHA, DUNGEON_DELTA, DUNGEON_GAMMA, DUNGEON_BETA
from dungeons.mixins import InitDangerousMap, InitSafeMap
from enums.render_order import RenderOrder
from map_objects.transition import Transition
from config.image_objects import STAIRS_DOWN, STAIRS_UP
from map_objects.rect import Rect
from map_objects.majorroad import MajorRoad
from dungeons.dungeon_alpha import DungeonAlphaMixin
from dungeons.overworld.biome_mixin import BiomeMixin
from dungeons.overworld.plot_mixin import PlotMixin


class CaveBuilder(AbstractDungeonBuilder, InitDangerousMap):
    """DungeonBuilder that makes procedural caves. Not currently implemented, but should work"""

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
    """DungeonBuilder that makes the overworld. BiomeMixin applies biomes and PlotMixin creates the core plot"""

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
    """Builds the first dungeon in the core plot, the starting town for the Player"""

    def __init__(self, node):
        self.basename = 'alpha'
        self.subtype = None
        self.floors = 1
        self.width, self.height = DUNGEON_ALPHA
        self.np = 0
        self.node = node

    def get_maps(self):
        alpha_map = self.initialize_map()
        outer_scenery_dim = 5

        walls = self.get_town_walls(outer_scenery_dim)
        major_road = self.get_major_road(outer_scenery_dim)

        alpha_map.integrate_protostructure(walls)
        alpha_map.integrate_protostructure(major_road, flag='major')

        alpha_map.set_modes(walls, 'blocker')

        structures = self.get_prefab_structures()

        alpha_map.integrate_protostructures(structures)

        alpha_map.set_modes(major_road, 'floor')
        for struct in structures:
            alpha_map.set_modes(struct, 'floor')

        samwise = self.get_samwise()

        alpha_map.noncombatants.append(samwise)

        return [alpha_map]
        # convert to add_structures as part of tile rework
        # add_house(floor, 10, int(height / 2) - 8)
        # add_hut(floor, 30, int(height / 2) - 19)

        # equippable_test = EquippableBuilder(499)
        # director = Director()
        #
        # random shopkeeper
        # director.set_builder(equippable_test)
        # equippable = director.get_equippable()
        # item_component = Item(equippable=equippable)
        # test_gear = Entity(20, 20, blocks=False, render_order=RenderOrder.ITEM, item=item_component)
        #
        # floor.entities.append(test_gear)
        #


class DungeonBetaBuilder(InitSafeMap, AbstractDungeonBuilder):
    """Builds the second dungeon in the core plot, another town similar to DungeonAlpha. Will have binary decision
    that affects DungeonGamma, defaults one way after x time. """

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
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.connect_to_overworld(road)
        return [map]


class DungeonGammaBuilder(InitSafeMap, AbstractDungeonBuilder):
    """Builds the third dungeon in the core plot, a castle city with multiple districts. May have altered
    strength/influence or opinion of Player based on DungeonBeta events. """

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
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.connect_to_overworld(road)
        return [map]


class DungeonDeltaBuilder(InitSafeMap, AbstractDungeonBuilder):
    """Builds the fourth dungeon in the core plot, a seaside port town where the Player can gain boat access."""

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
        road = MajorRoad(rect, self.node)
        road.set_transitions('vertical')
        # add_road also adds transitions to overworld
        map.connect_to_overworld(road)
        return [map]
