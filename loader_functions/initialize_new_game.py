from loader_functions.new_game_functions import get_player, get_camera, equip_player, get_dungeons, get_intro_quest
from game_messages import MessageLog
from enums.game_states import GameStates
from map_objects.game_map import GameMap
from loader_functions.image_objects import get_image_bundle
from journal import Journal, Quest
from party import Party


def get_game_variables(constants, images):

    hero_bundle = get_image_bundle(images, 'hero')

    ent = images.get('entities')

    player = get_player(hero_bundle)
    camera = get_camera(player, constants)
    equip_player(player, ent.get('items').get('equippables').get('weapons').get('stick'))
    
    entities = [player]
    structures = []
    transitions = []
    noncombatants = []
    
    dungeons, world_map = get_dungeons(constants, images)
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
    