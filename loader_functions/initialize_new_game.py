from loader_functions.new_game_functions import get_player, equip_player, get_dungeons, get_intro_quest
from game_messages import MessageLog
from map_objects.game_map import GameMap
from handlers.menus.journal import Journal
from handlers.menus.party import Party
from handlers.menus.inventory import Inventory
from camera import Camera


def get_game_variables():

    player = get_player()
    party = Party(player)
    party.inventory = Inventory()
    equip_player(party)

    camera = Camera()

    entities = [player]
    structures = []
    transitions = []
    noncombatants = []

    dungeons, world_map = get_dungeons()

    game_map = GameMap(dungeons['town'], dungeons['town'].maps[0])

    entities.extend(game_map.current_map.map_entities)
    structures.extend(game_map.current_map.structures)
    transitions.extend(game_map.current_map.transitions)
    noncombatants.extend(game_map.current_map.noncombatants)

    message_log = MessageLog(10)

    journal = Journal()
    journal.current_quests.append(get_intro_quest())

    return player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera,\
        message_log, party, journal
