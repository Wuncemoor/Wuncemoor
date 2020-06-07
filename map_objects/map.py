import tcod as libtcod

from ECS.entity import Entity
from enums.equipment_slots import EquipmentSlots
from game_messages import Message
from item_functions import heal, cast_lightning, cast_fireball, cast_confuse
from random import randint
from random_utils import random_choice_from_dict, from_dungeon_level
from render_functions import RenderOrder
from builders.mob_builder import MobDirector, MobBuilder
from ECS.__entity.__item.equippable import Equippable
from ECS.__entity.__item.__equippable.equippable_core import EquippableCore
from ECS.__entity.__item.__equippable.equippable_material import EquippableMaterial
from ECS.__entity.__item.__equippable.equippable_quality import EquippableQuality
from ECS.__entity.item import Item
from ECS.__entity.__item.useable import Useable
from map_objects.rectangle import Rect
from map_objects.tile import Tile
from map_objects.chances.item_chances import get_item_chances
from map_objects.chances.mob_chances import MobChances
from map_objects.encounter import Encounter
from ECS.image_bundle import ImageBundle
from loader_functions.image_objects import get_image_bundle



class Map:

    def __init__(self, width, height, variant=None, dungeon_level=0, dangerous=False):

        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        self.dungeon_level = dungeon_level
        self.map_entities = self.initialize_entities()
        self.transitions = []
        self.structures = []
        self.noncombatants = []
        self.entrance = None
        self.exit = None
        self.floor_image = None
        self.variant = variant
        self.dangerous = dangerous

    def add_road(self, road):
        for x in range(road.rect.x1, road.rect.x2):
            for y in range(road.rect.y1, road.rect.y2):
                self.tiles[x][y].type = 'road'
                self.tiles[x][y].blocked = False
        for x in range(road.rect.x1, road.rect.x2):
            for y in range(road.rect.y1, road.rect.y2):
                mode = ''
                try:
                    tf = [self.tiles[x - 1][y - 1].type == 'road', self.tiles[x][y - 1].type == 'road',
                          self.tiles[x + 1][y - 1].type == 'road', self.tiles[x - 1][y].type == 'road',
                          self.tiles[x + 1][y].type == 'road', self.tiles[x - 1][y + 1].type == 'road',
                          self.tiles[x][y + 1].type == 'road', self.tiles[x + 1][y + 1].type == 'road']
                except IndexError:
                    tf = [True, True, True, True, True, True, True, True]

                for qq in tf:
                    if qq:
                        mode += '1'
                    else:
                        mode += '0'

                self.tiles[x][y].mode = mode
        self.transitions.extend(road.transitions)

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        for row in tiles:
            for tile in row:
                tile.type = 'wall'
        return tiles

    def initialize_entities(self):
        entities = []
        return entities

    def set_dungeon_level(self, level):
        self.dungeon_level = level

    def create_room(self, room, d_type, subtype):
        # go through the tiles in the rectangle and make them not blocked

        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False
                self.tiles[x][y].type = d_type
                self.tiles[x][y].subtype = subtype



    def create_h_tunnel(self, x1, x2, y, d_type, subtype=None):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].type = d_type
            self.tiles[x][y].subtype = subtype


    def create_v_tunnel(self, y1, y2, x, d_type, subtype=None):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
            self.tiles[x][y].type = d_type
            self.tiles[x][y].subtype = subtype


    # Create everything except stairs
    def fill_map(self, dungeon_type, subtype, node_power, max_rooms, room_min_size, room_max_size, map_width,
                 map_height, objs):
        rooms = []
        num_rooms = 0
        center_of_last_room_x = None
        center_of_last_room_y = None

        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random posiition without going out of boundaries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)
            # Rect class makes rectangless easier to work  with
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
                self.place_entities(new_room, dungeon_type, subtype, node_power, objs)
                rooms.append(new_room)
                self.exit = (center_of_last_room_x, center_of_last_room_y)
                num_rooms += 1

    def place_entities(self, room, dungeon_type, subtype, node_power, objs):
        # Get random number of monsters
        number_of_monsters = from_dungeon_level([[2, 1], [3, 4], [5, 6]], self.dungeon_level)

        number_of_items = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)

        mob_chances = MobChances(dungeon_type, subtype, node_power)
        mcs = mob_chances.get_mob_chances()
        item_chances = get_item_chances(self.dungeon_level)
        items = objs.get('entities').get('items')


        for i in range(number_of_monsters):
            # choose location in room
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in self.map_entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(mcs)
                mob_img_bundle = get_image_bundle(objs, monster_choice)

                mob_builder = MobBuilder(0, monster_choice, mob_img_bundle)
                mob_director = MobDirector()
                mob_director.set_builder(mob_builder)
                combatant_component = mob_director.get_combatant()
                monster = Entity(x, y, blocks=True, render_order=RenderOrder.ACTOR,
                                 combatant=combatant_component)

                self.map_entities.append(monster)

        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)
            equippables = items.get('equippables')
            weapons = equippables.get('weapons')
            useables = items.get('useables')

            if not any([entity for entity in self.map_entities if entity.x == x and entity.y == y]) and not \
                    any([transition for transition in self.transitions if transition.x == x and transition.y == y]):
                item_choice = random_choice_from_dict(item_chances)

                if item_choice == 'healing_potion':
                    image = ImageBundle(useables.get('potion'))
                    item_component = Item(
                        useable_component=Useable('Healing Potion', image, use_function=heal, amount=400))
                    item = Entity(x, y, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'sword':
                    image = ImageBundle(weapons.get('longsword'))
                    equippable_core = EquippableCore('longsword', image)
                    equippable_material = EquippableMaterial('wood')
                    equippable_quality = EquippableQuality('average')

                    equippable_component = Equippable('Sword', image, EquipmentSlots.MAIN_HAND, equippable_core,
                                                      equippable_material, equippable_quality)
                    item_component = Item(equippable_component)
                    item = Entity(x, y, item=item_component)
                elif item_choice == 'shield':
                    image = ImageBundle(weapons.get('shield'))
                    equippable_core = EquippableCore('shield', image)
                    equippable_material = EquippableMaterial('iron')
                    equippable_quality = EquippableQuality('average')

                    equippable_component = Equippable('Shield', image, EquipmentSlots.OFF_HAND, equippable_core,
                                                      equippable_material, equippable_quality)
                    item_component = Item(equippable_component)
                    item = Entity(x, y, item=item_component)
                elif item_choice == 'fireball_scroll':
                    image = ImageBundle(items.get('useables').get('scroll'))
                    item_component = Item(
                        useable_component=Useable('Fireball Scroll', image, use_function=cast_fireball, targeting=True,
                                                  targeting_message=Message(
                                                      'Left-click a target tile for the fireball, or right-click to rethink your life decisions.',
                                                      libtcod.light_cyan), damage=250, radius=3))
                    item = Entity(x, y, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'confusion_scroll':
                    image = ImageBundle(items.get('useables').get('scroll'))
                    item_component = Item(
                        useable_component=Useable('Confusion Scroll', image, use_function=cast_confuse, targeting=True,
                                                  targeting_message=Message(
                                                      'Left-click an enemy to confuse it, or right-click to cancel.',
                                                      libtcod.light_cyan)))
                    item = Entity(x, y, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'lightning_scroll':
                    image = ImageBundle(items.get('useables').get('scroll'))
                    item_component = Item(
                        useable_component=Useable('Lightning Scroll', image, use_function=cast_lightning, damage=400,
                                                  maximum_range=5))
                    item = Entity(x, y, render_order=RenderOrder.ITEM, item=item_component)

                self.map_entities.append(item)

    def add_boss(self, d_type, subtype, node_power, obj):

        mob_chances = MobChances(d_type, subtype, node_power * 100)

        monster_choice = random_choice_from_dict(mob_chances.get_mob_chances())
        mob_builder = MobBuilder(0, monster_choice, obj)
        mob_director = MobDirector()
        mob_director.set_builder(mob_builder)
        combatant_component = mob_director.get_combatant()
        monster = Entity(self.exit[0], self.exit[1], blocks=True,
                         render_order=RenderOrder.ACTOR, combatant=combatant_component)

        self.map_entities.append(monster)

    def set_floor_image(self, string):

        dict = {
            'cave': 'dirt',
            'directed_dungeon': 'dirt',
        }

        self.floor_image = dict.get(string)


    def get_encounter(self, images, tile, options):

        bg = images.get('backgrounds').get(tile.type + '_bg')

        event = self.get_encounter_event(images, tile)

        return Encounter(bg, event, options)


    def get_encounter_event(self, images, tile):

        mob_chances = MobChances(tile.type, tile.subtype, tile.np)
        mcs = mob_chances.get_mob_chances()
        monster_choice = random_choice_from_dict(mcs)
        print(monster_choice)
        print(images)
        mob_img_bundle = get_image_bundle(images, monster_choice)
        print(mob_img_bundle)
        print(mob_img_bundle.actor)

        mob_builder = MobBuilder(0, monster_choice, mob_img_bundle)
        mob_director = MobDirector()
        mob_director.set_builder(mob_builder)
        combatant_component = mob_director.get_combatant()
        event = Entity(0, 0, blocks=True, render_order=RenderOrder.ACTOR,
                         combatant=combatant_component)


        return event