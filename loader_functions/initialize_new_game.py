from loader_functions.new_game_functions import get_player, get_camera, equip_player, get_dungeons
from game_messages import MessageLog
from game_states import GameStates
from map_objects.game_map import GameMap


def get_game_variables(constants, images):

    ent = images.get('entities')
    player = get_player(ent.get('combatants').get('hero'))
    camera = get_camera(player, constants)
    equip_player(player, ent.get('items').get('equippables').get('weapons').get('stick'))
    
    entities = [player]
    structures = []
    transitions = []
    
    dungeons, world_map = get_dungeons(constants, images)
    game_map = GameMap(dungeons['town'].maps[0])
    
    entities.extend(game_map.current_map.map_entities)
    structures.extend(game_map.current_map.structures)
    transitions.extend(game_map.current_map.transitions)

    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    game_state = GameStates.PLAYERS_TURN
    
    return player, dungeons, entities, structures, transitions, game_map,  world_map, camera, message_log, game_state
    