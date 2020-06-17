from loader_functions.new_game_functions import get_player, get_camera, equip_player, get_dungeons, get_intro_quest
from game_messages import MessageLog
from enums.game_states import GameStates
from map_objects.game_map import GameMap
from journal import Journal
from party import Party
import config.image_objects as imgs
import config.constants as const


def get_game_variables():

    constants = const.get_constants()

    hero_bundle = imgs.get_image_bundle('hero')



    player = get_player(hero_bundle)

    camera = get_camera(player)

    equip_player(player)
    
    entities = [player]
    structures = []
    transitions = []
    noncombatants = []
    
    dungeons, world_map = get_dungeons()

    game_map = GameMap(dungeons['town'].maps[0])
    
    entities.extend(game_map.current_map.map_entities)
    structures.extend(game_map.current_map.structures)
    transitions.extend(game_map.current_map.transitions)
    noncombatants.extend(game_map.current_map.noncombatants)

    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    game_state = GameStates.PLAYERS_TURN

    party = Party(player)

    journal = Journal()
    journal.current_quests.append(get_intro_quest())

    return player, dungeons, entities, structures, transitions, noncombatants, game_map,  world_map, camera, message_log, game_state, party, journal
    