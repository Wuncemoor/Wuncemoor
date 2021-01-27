from handlers.logic.logic_chunks import ShopBaseGoToSub, reward_goto_life, reward_manual, reward_auto



def settings_options():
    pass


def shop_base_categories():
    return OptionsFake(['weapons', 'armor', 'accessories', 'rations', 'satchel', 'materials', 'plot'], fake=ShopBaseGoToSub)





