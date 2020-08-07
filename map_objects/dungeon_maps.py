from dungeons.tile_mixins import InitRealTiles
from map_objects.majorroad import RoadTileFloor
from ECS.entity import Entity
from random import randint
from abstracts.abstract_maps import ProceduralTiles2D
from misc_functions.random_utils import random_choice_from_dict, from_dungeon_level
from enums.render_order import RenderOrder
from builders.mob_builder import MobDirector, MobBuilder
from map_objects.rect import Rect
from misc_functions.item_chances import get_item_chances
from misc_functions.mob_chances import MobChances
from builders.make_item import make_item
from config.constants import MAX_ROOMS, ROOM_MAX_SIZE, ROOM_MIN_SIZE


class DangerousMap(ProceduralTiles2D, InitRealTiles):
    """One of two "real" Maps, along with SafeMap. Time flows normally (1 hr/step) on a DangerousMap and every step
    has a chance for a combat encounter to trigger. """

    def __init__(self, width, height, variant):
        super().__init__(width, height, variant)
        self.entities = []
        self.structures = []
        self.noncombatants = []
        self.entrance = None
        self.exit = None

    def create_room(self, room, d_type, subtype):

        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False
                self.tiles[x][y].type = d_type
                self.tiles[x][y].subtype = subtype
                self.get_image(d_type, self.tiles[x][y])

    def create_h_tunnel(self, x1, x2, y, d_type, subtype=None):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].type = d_type
            self.tiles[x][y].subtype = subtype
            self.get_image(d_type, self.tiles[x][y])

    def create_v_tunnel(self, y1, y2, x, d_type, subtype=None):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].type = d_type
            self.tiles[x][y].subtype = subtype
            self.get_image(d_type, self.tiles[x][y])

    # Create everything except stairs
    def fill_tiles(self, dungeon_type, subtype, node_power):
        rooms = []
        num_rooms = 0
        center_of_last_room_x = None
        center_of_last_room_y = None

        for r in range(MAX_ROOMS):
            w = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            h = randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
            # random position without going out of boundaries of the map
            x = randint(0, self.width - w - 1)
            y = randint(0, self.height - h - 1)
            new_room = Rect(x, y, w, h)
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # No intersections, ergo valid room
                # "paint" to map's tiles
                self.create_room(new_room, dungeon_type, subtype)
                # center coordinates of new room, useful later
                (new_x, new_y) = new_room.center()
                center_of_last_room_x = new_x
                center_of_last_room_y = new_y

                if num_rooms == 0:
                    # First room, where player starts
                    self.entrance = (new_x, new_y)

                else:
                    # all rooms after first
                    # connect it to previous room with a tunnel
                    # center of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                    # flip a coin
                    if randint(0, 1) == 1:
                        # first horizontal, then vertical
                        self.create_h_tunnel(prev_x, new_x, prev_y, dungeon_type, subtype)
                        self.create_v_tunnel(prev_y, new_y, new_x, dungeon_type, subtype)
                    else:
                        # first vertical, then horizontal
                        self.create_v_tunnel(prev_y, new_y, prev_x, dungeon_type, subtype)
                        self.create_h_tunnel(prev_x, new_x, new_y, dungeon_type, subtype)
                # append room to list
                #self.place_entities(new_room, dungeon_type, subtype, node_power)

                rooms.append(new_room)
                self.exit = (center_of_last_room_x, center_of_last_room_y)
                num_rooms += 1

    def place_entities(self, room, dungeon_type, subtype, node_power):
        number_of_monsters = from_dungeon_level([[2, 1], [3, 4], [5, 6]], self.dungeon_level)

        number_of_items = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)
        mob_chances = MobChances(dungeon_type, subtype, node_power)
        mcs = mob_chances.get_mob_chances()
        item_chances = get_item_chances(self.dungeon_level)

        for i in range(number_of_monsters):
            # choose location in room
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in self.entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(mcs)

                mob_builder = MobBuilder(0, monster_choice)
                mob_director = MobDirector()
                mob_director.set_builder(mob_builder)
                combatant_component = mob_director.get_mob()
                monster = Entity(x, y, blocks=True, render_order=RenderOrder.ACTOR,
                                 combatant=combatant_component)

                self.entities.append(monster)

        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)
            if not any([entity for entity in self.entities if entity.x == x and entity.y == y]) and not \
                    any([transition for transition in self.transitions if transition.x == x and transition.y == y]):
                item_choice = random_choice_from_dict(item_chances)
                item = make_item(item_choice)
                self.entities.append(item)

    def add_boss(self, d_type, subtype, node_power):

        mob_chances = MobChances(d_type, subtype, node_power * 100)

        monster_choice = random_choice_from_dict(mob_chances.get_mob_chances())
        mob_builder = MobBuilder(0, monster_choice)
        mob_director = MobDirector()
        mob_director.set_builder(mob_builder)
        mob = mob_director.get_mob()
        mob.x, mob.y = self.exit[0], self.exit[1]

        self.entities.append(mob)


class SafeMap(InitRealTiles, ProceduralTiles2D):
    """One of two "real Maps, alongside DangerousMap. Movement does not trigger the passage of time or combat checks.
    Time/Combat can still occur through other events """

    def __init__(self, width, height, variant):
        super().__init__(width, height, variant)
        self.entities = []
        self.structures = []
        self.noncombatants = []
        self.entrance = None
        self.exit = None

    def add_road(self, road):
        self.set_floors(road)
        self.set_modes(road)

    def set_floors(self, proto):
        j, i = 0, 0
        for y in range(proto.rect.y1, proto.rect.y2):
            for x in range(proto.rect.x1, proto.rect.x2):
                self.tiles[y][x].floor = proto.tiles[j][i].floor
                i += 1
            j += 1
            i = 0

    def set_modes(self, proto):
        for y in range(proto.rect.y1, proto.rect.y2):
            for x in range(proto.rect.x1, proto.rect.x2):
                mode = ''
                try:
                    tf = [self.tiles[y - 1][x - 1], self.tiles[y - 1][x],
                          self.tiles[y - 1][x + 1], self.tiles[y][x - 1],
                          self.tiles[y][x + 1], self.tiles[y + 1][x - 1],
                          self.tiles[y + 1][x], self.tiles[y + 1][x + 1]]
                except IndexError:
                    tf = [self.tiles[y][x], self.tiles[y][x],
                          self.tiles[y][x], self.tiles[y][x],
                          self.tiles[y][x], self.tiles[y][x],
                          self.tiles[y][x], self.tiles[y][x]]

                for qq in tf:
                    if isinstance(qq.floor, RoadTileFloor):
                        mode += '1'
                    else:
                        mode += '0'
                self.tiles[y][x].floor.mode = mode
                self.tiles[y][x].floor.set_images()



    def fill_tiles(self):
        pass

    def add_structure(self):
        pass