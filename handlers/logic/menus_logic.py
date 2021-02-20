
def menus_goto_submenu(mvc):
    if len(mvc.handler.menu_type.menu.pointer_data) > 0:
        return [{'subsubstate': 2}]
    return []


def menus_goto_selected_options():
    return [{'subsubstate': 3}]


def menus_goto_menus(obj):
    return [{'substate': obj}]


def menus_submenu_goto_life():
    return [{'subsubstate': 1}, {'state': 'life'}]


def menus_exit(mvc):
    if mvc.handler.menu_type.submenu is None:
        return [{'state': 'life'}, {'substate': 'root'}]
    elif mvc.handler.menu_type.submenu.locked:
        return menus_goto_submenu(mvc)
    else:
        return [{'subsubstate': 1}]


def menus_toggle(mvc, output):
    if mvc.handler.menu_type is output:
        return menus_submenu_goto_life()
    else:
        return menus_goto_menus(output)
