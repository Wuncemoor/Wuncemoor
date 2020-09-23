from handlers.logic.logic_chunks import NewGame, LoadGame, QuitGame, FightTargeting, UseSatchel, RunAway, RewardAuto, \
    RewardManual, RewardToLife, MenuGoToSub, ShopGoToSub


class Options:
    def __init__(self, options, text=None):
        self.options = options
        self.text = text
        self.choice = 0


class OptionsFake:

    def __init__(self, options, fake, text=None):
        self.options = options
        self.fake = fake
        self.text = text
        self.choice = 0

def title_options():
    text = ['Start A New Game', 'Continue A Previous Game', 'Quit']
    options = Options([NewGame, LoadGame, QuitGame], text)
    return options


def initialize_menu_options(subgroups):
    return OptionsFake(subgroups, MenuGoToSub)


def encounter_window_options():
    text = ['FIGHT', 'ITEM', 'RUN']
    options = Options([FightTargeting, UseSatchel, RunAway], text)
    return options


def reward_options():
    text = ['AUTO', 'MANUAL', 'LEAVE']
    options = Options([RewardAuto, RewardManual, RewardToLife], text)
    return options


def settings_options():
    pass


def shop_options():
    return OptionsFake(['misc', 'weapons', 'armor', 'accessories', 'satchel', 'materials', 'plot'], fake=ShopGoToSub)





