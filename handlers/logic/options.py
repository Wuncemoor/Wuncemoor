from handlers.logic.logic_chunks import NewGame, LoadGame, QuitGame

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
    options = Options([InvMisc, InvWeapons, InvArmor, InvAccessories, InvSatchel, InvMaterials, InvPlot])

def journal_options():
    options = Options([JournalCurrent, JournalCompleted, JournalCodex, JournalConvo])
    return options


