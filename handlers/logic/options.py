from handlers.logic.logic_chunks import NewGame, LoadGame, QuitGame, GoToSubJournal, GoToSubInventory, \
    FightTargeting, UseSatchel, RunAway


class Options:
    def __init__(self, options, text=None):
        self.options = options
        self.text = text
        self.choice = 0


def title_options():
    text = ['Start A New Game', 'Continue A Previous Game', 'Quit']
    options = Options([NewGame, LoadGame, QuitGame], text)
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
    text = ['FIGHT', 'ITEM', 'RUN']
    options = Options([FightTargeting, UseSatchel, RunAway], text)
    return options




