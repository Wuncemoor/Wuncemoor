from loader_functions.new_game_functions import get_player, equip_player, get_dungeons, get_intro_quest
from game_messages import MessageLog
from handlers.world_handler import WorldHandler
from handlers.menus.journal import Journal
from handlers.menus.party import Party
from handlers.state_handlers import MenusHandler


def get_game_variables():

    player = get_player()
    party = Party(player)
    party.focus = party.p1

    equip_player(party)

    dungeons, overworld_tiles = get_dungeons()

    world = WorldHandler(dungeons['town'], dungeons['town'].maps[0])

    message_log = MessageLog(10)

    journal = Journal()
    journal.current_quests.append(get_intro_quest())
    party.journal = journal

    return player, dungeons, world, overworld_tiles, message_log, party
