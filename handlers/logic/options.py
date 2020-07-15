from handlers.logic.logic_chunks import NewGame, LoadGame, QuitGame, GoToSubJournal, GoToSubInventory, \
    FightTargeting, UseSatchel, RunAway


class Options:
    def __init__(self, options):
        self.options = options
        self.choice = 0


def title_options():
    options = Options([NewGame, LoadGame, QuitGame])
    return options


def party_options():
    options = Options([])
    return options


def inventory_options():
    options = Options([GoToSubInventory, GoToSubInventory, GoToSubInventory, GoToSubInventory,
                       GoToSubInventory, GoToSubInventory, GoToSubInventory])
    return options


def journal_options():
    options = Options([GoToSubJournal, GoToSubJournal, GoToSubJournal, GoToSubJournal])
    return options


def encounter_options():
    options = Options([FightTargeting, UseSatchel, RunAway])
    return options


