from handlers.logic.logic_chunks import NewGame, LoadGame, QuitGame, FightTargeting, UseSatchel, RunAway, RewardAuto, \
    RewardManual, RewardToLife, MenuGoToSub, ShopBaseGoToSub, TitleSettings, TitleAcknowledgements


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
    text = ['New Game', 'Load Game', 'Settings', 'Acknowledgements', 'Quit']
    options = Options([NewGame, LoadGame, TitleSettings, TitleAcknowledgements, QuitGame], text)
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


def shop_base_categories():
    return OptionsFake(['weapons', 'armor', 'accessories', 'rations', 'satchel', 'materials', 'plot'], fake=ShopBaseGoToSub)





