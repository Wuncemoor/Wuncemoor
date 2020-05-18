from loader_functions.new_game_functions import get_player, get_camera, equip_player, get_dungeons
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap


    
def get_game_variables(constants):

    player = get_player()
    camera = get_camera(player, constants)
    equip_player(player)
    
    entities = [player]
    structures = []
    
    dungeons = get_dungeons(constants)
    game_map = GameMap(dungeons['start'].maps[0])
    
    entities.extend(game_map.current_map.map_entities)
    structures.append(game_map.current_map.structures)
    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    game_state = GameStates.PLAYERS_TURN
    
    return player, dungeons, entities, structures, game_map,  camera, message_log, game_state
    