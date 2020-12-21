from handlers.logic.logic_chunks import FightTargeting, UseSatchel, RunAway, RewardAuto, \
    RewardManual, RewardToLife, ShopBaseGoToSub


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


def encounter_window_options():
    logic = [FightTargeting, UseSatchel, RunAway]
    text = ['FIGHT', 'ITEM', 'RUN']
    options = Options(logic, text)
    return options


def reward_options():
    logic = [RewardAuto, RewardManual, RewardToLife]
    text = ['AUTO', 'MANUAL', 'LEAVE']
    options = Options(logic, text)
    return options


def settings_options():
    pass


def shop_base_categories():
    return OptionsFake(['weapons', 'armor', 'accessories', 'rations', 'satchel', 'materials', 'plot'], fake=ShopBaseGoToSub)





