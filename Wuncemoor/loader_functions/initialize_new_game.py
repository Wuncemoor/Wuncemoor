import tcod as libtcod
from PIL import Image
from components.combatant import Combatant
from components.item import Item
from components.inventory import Inventory
from components.level import Level
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.equipment import Equipment
from components.equippable import Equippable, get_equippable
from components.attributes import Attributes
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap
from map_objects.alpha import NodeAlphaMap
from render_functions import RenderOrder


def get_constants():
    window_title = 'Wuncemoor: The Eternal Dream'
    
    screen_width = 80
    screen_height = 50
    fps = 60
    
    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height
    
    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height -1
    
    map_width = 80
    map_height = 43
    
    room_max_size = 10
    room_min_size = 6
    max_rooms = 3
    
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10
    
    max_monsters_per_room = 3
    max_items_per_room = 2
    
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50),
        'white' : libtcod.Color(255,255,255)
        }
    
    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors
        }
    return constants
    
def get_game_variables(constants):
    attribute_component = Attributes(10,10,10,10,10,10,10,10,10,10)
    inventory_component = Inventory(26)
    level_component = Level()
    competence_component = Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(), Finesse(), Charisma(), Devotion())
    equipment_component = Equipment()
    combatant_component = Combatant('Player', '@', attributes=attribute_component, level=level_component, competence=competence_component, equipment=equipment_component, inventory=inventory_component)

    
    player = Entity(0, 0, libtcod.white, blocks=True, render_order = RenderOrder.ACTOR, combatant=combatant_component)
    
    entities = [player]
    
    item_component = Item(Equippable('Stick', '-', EquipmentSlots.MAIN_HAND, EquippableCore('staff'), EquippableMaterial('wood'), EquippableQuality('average')))
    stick = Entity(0, 0, libtcod.sky, item=item_component)
    player.combatant.inventory.add_item(stick)
    player.combatant.equipment.toggle_equip(stick)
    
    
    game_map = NodeAlphaMap(constants['map_width'], constants['map_height'])
    game_map.make_alpha_map(constants['map_width'], constants['map_height'], player, entities)
    
    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    game_state = GameStates.PLAYERS_TURN
    
    return player, entities, game_map, message_log, game_state
    