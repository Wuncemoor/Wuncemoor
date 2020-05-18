import tcod as libtcod

from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import Message
from item_functions import heal, cast_lightning, cast_fireball, cast_confuse
from random import randint
from random_utils import random_choice_from_dict, from_dungeon_level
from render_functions import RenderOrder
from builders.mob_builder import MobDirector, MobBuilder
from components.equippable import Equippable
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from components.item import Item
from components.useable import Useable
from map_objects.rectangle import Rect
from map_objects.tile import Tile
from map_objects.chances.item_chances import get_item_chances
from map_objects.chances.mob_chances import MobChances



class Map:
    
    def __init__(self, width, height, tiles, map_entities, dungeon_level=0):
        
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        self.dungeon_level = dungeon_level
        self.map_entities = self.initialize_entities()
        self.structures = []
        self.entrance = None
        self.exit = None

    def add_road(self, road):
        i = 0
        j = 0
        for y in self.tiles:
            for x in y:
                if road.x1 <= i < road.x2 and road.y1 <= j < road.y2:
                    self.tiles[x][y].type = 'road'
                i += 1
            j += 1
        
    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles
        
    def initialize_entities(self):
        entities = []
        return entities
    
    def set_dungeon_level(self, level):
        self.dungeon_level = level
        
    def create_room(self, room):
        #go through the tiles in the rectangle and make them not blocked
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def add_road(self, road):
        for x in range(road.x1, road.x2):
            for y in range(road.y1, road.y2):
                self.tiles[x][y].type = 'road'
                self.tiles[x][y].blocked = False
                
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
        
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    #Create everything except stairs
    def fill_map(self, dungeon_type, subtype, node_power, max_rooms, room_min_size, room_max_size, map_width, map_height):
        rooms = []
        num_rooms = 0
        center_of_last_room_x = None
        center_of_last_room_y = None
        
        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            #random posiition without going out of boundaries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)
            #Rect class makes rectangless easier to work  with
            new_room = Rect(x, y, w, h)
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                #No intersections, ergo valid room
                #"paint" to map's tiles
                self.create_room(new_room)
                #center coordinates of new room, useful later
                (new_x, new_y) = new_room.center()
                center_of_last_room_x = new_x
                center_of_last_room_y = new_y
                     
                if num_rooms == 0:
                #First room, where player starts
                    self.entrance = (new_x, new_y)

                else:
                #all rooms after first
                #connect it to previous room with a tunnel
                #center of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                #flip a coin
                    if randint(0,1) == 1:
                    #first horizontal, then vertical
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                    #first vertical, then horizontal
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                #append room to list
                self.place_entities(new_room, dungeon_type, subtype, node_power)
                rooms.append(new_room)
                self.exit = (center_of_last_room_x, center_of_last_room_y)
                num_rooms += 1
        


    def place_entities(self, room, dungeon_type, subtype, node_power):
        #Get random number of monsters
        number_of_monsters = from_dungeon_level([[2,1], [3,4], [5,6]], self.dungeon_level)
        
        number_of_items = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)

        mob_chances = MobChances(dungeon_type, subtype, node_power)
        mcs = mob_chances.get_mob_chances()
        item_chances = get_item_chances(dungeon_type, self.dungeon_level)
            
        for i in range(number_of_monsters):
            #choose location in room
            x = randint(room.x1 +1, room.x2 -1)
            y = randint(room.y1 +1, room.y2 -1)
            
            if not any([entity for entity in self.map_entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(mcs)
                mob_builder = MobBuilder(0,monster_choice)
                mob_director = MobDirector()
                mob_director.set_builder(mob_builder)
                combatant_component = mob_director.get_combatant()
                monster = Entity(x, y, libtcod.desaturated_green, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant_component)
                    
                self.map_entities.append(monster)
                     
        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 -1)
            y = randint(room.y1 + 1, room.y2 -1)
            
            if not any([entity for entity in self.map_entities if entity.x == x and entity.y == y]):
                item_choice = random_choice_from_dict(item_chances)
                
                
                if item_choice == 'healing_potion':
                    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\\potion.png'
                    item_component = Item(useable_component=Useable('Healing Potion', image, use_function=heal, amount=400))
                    item = Entity(x, y, libtcod.violet, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'sword':
                    equippable_core = EquippableCore('longsword')
                    equippable_material = EquippableMaterial('wood')
                    equippable_quality = EquippableQuality('average')
                    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\\longsword.png'
                    equippable_component = Equippable('Sword', image, EquipmentSlots.MAIN_HAND, equippable_core, equippable_material, equippable_quality)
                    item_component = Item(equippable_component)
                    item = Entity(x, y, libtcod.sky, item=item_component)
                elif item_choice == 'shield':
                    equippable_core = EquippableCore('shield')
                    equippable_material = EquippableMaterial('iron')
                    equippable_quality = EquippableQuality('average')
                    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\\shield.png'
                    equippable_component = Equippable('Shield', image, EquipmentSlots.OFF_HAND, equippable_core, equippable_material, equippable_quality)
                    item_component = Item(equippable_component)
                    item = Entity(x, y, libtcod.darker_orange, item=item_component)
                elif item_choice == 'fireball_scroll':
                    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\\scroll.png'
                    item_component = Item(useable_component=Useable('Fireball Scroll', image, use_function=cast_fireball, targeting = True, targeting_message=Message('Left-click a target tile for the fireball, or right-click to rethink your life decisions.', libtcod.light_cyan), damage=250, radius=3))
                    item = Entity(x, y, libtcod.red, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'confusion_scroll':
                    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\\scroll.png'
                    item_component = Item(useable_component=Useable('Confusion Scroll', image, use_function=cast_confuse, targeting=True, targeting_message=Message('Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan)))
                    item = Entity(x, y, libtcod.light_pink, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'lightning_scroll':
                    image = r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\images\\scroll.png'
                    item_component = Item(useable_component=Useable('Lightning Scroll', image, use_function = cast_lightning, damage=400, maximum_range=5))
                    item = Entity(x, y, libtcod.yellow, render_order=RenderOrder.ITEM, item=item_component)
                    
                self.map_entities.append(item)
                    
    def add_boss(self, d_type, subtype, node_power):
    
        mob_chances = MobChances(d_type, subtype, node_power*100)

    
        monster_choice = random_choice_from_dict(mob_chances.get_mob_chances())
        mob_builder = MobBuilder(0,monster_choice)
        mob_director = MobDirector()
        mob_director.set_builder(mob_builder)
        combatant_component = mob_director.get_combatant()
        monster = Entity(self.exit[0], self.exit[1], libtcod.desaturated_green, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant_component)
            
        self.map_entities.append(monster)
        