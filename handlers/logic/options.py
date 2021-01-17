from handlers.logic.logic_chunks import ShopBaseGoToSub, encounter_goto_targeting, encounter_goto_life, \
    encounter_goto_satchel, reward_goto_life, reward_manual, reward_auto


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
    logic = [encounter_goto_targeting, encounter_goto_satchel, encounter_goto_life]
    text = ['FIGHT', 'ITEM', 'RUN']
    options = Options(logic, text)
    return options


def reward_options():
    logic = [reward_auto, reward_manual, reward_goto_life]
    text = ['AUTO', 'MANUAL', 'LEAVE']
    options = Options(logic, text)
    return options


def settings_options():
    pass


def shop_base_categories():
    return OptionsFake(['weapons', 'armor', 'accessories', 'rations', 'satchel', 'materials', 'plot'], fake=ShopBaseGoToSub)





