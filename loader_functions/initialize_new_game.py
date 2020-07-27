from loader_functions.new_game_functions import get_party, get_starting_items, get_intro_quest
from handlers.world_handler import WorldHandler
from handlers.menus.journal import Journal


def get_game_variables():

    party = get_party()

    get_starting_items(party)

    world = WorldHandler()
    world.new()

    journal = Journal()
    journal.current_quests.append(get_intro_quest())
    party.journal = journal

    return world, party
