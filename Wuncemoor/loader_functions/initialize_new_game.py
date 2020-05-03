import tcod as libtcod
from PIL import Image
from components.combatant import Combatant
from components.item import Item
from components.inventory import Inventory
from components.level import Level
from components.stairs import Stairs
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.equipment import Equipment
from components.equippable import Equippable, get_equippable
from components.attributes import Attributes
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from components.phylo import Phylo
from loader_functions.new_game_functions import get_player, get_camera, equip_player, get_dungeons
from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap
from map_objects.dungeon import Dungeon
from render_functions import RenderOrder

    
def get_game_variables(constants):

    player = get_player()
    camera = get_camera(player, constants)
    equip_player(player)
    
    entities = [player]
    
    dungeons = get_dungeons(constants)
    game_map = GameMap(dungeons['start'].maps[0])
    
    entities.extend(game_map.current_map.map_entities)
    
    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    game_state = GameStates.PLAYERS_TURN
    
    return player, dungeons, entities, game_map,  camera, message_log, game_state
    