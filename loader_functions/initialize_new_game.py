from loader_functions.new_game_functions import get_party, get_starting_items, get_dungeons, get_intro_quest
from handlers.world_handler import WorldHandler
from handlers.menus.journal import Journal


def get_game_variables():

    party = get_party()

    get_starting_items(party)

    dungeons, overworld_tiles = get_dungeons()

    world = WorldHandler(dungeons, dungeons['town'], dungeons['town'].maps[0])

    journal = Journal()
    journal.current_quests.append(get_intro_quest())
    party.journal = journal

    return world, overworld_tiles, party
