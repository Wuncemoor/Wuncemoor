def handle_targeting_keys(key):
    if key == py.K_ESCAPE:
        return {'exit': True}

    return {}


def handle_player_dead_keys(key):
    if key == py.K_i:
        return {'show_inventory': True}


    elif key == py.K_ESCAPE:
        # Exit the menu
        return {'exit': True}

    return {}


def handle_mouse(mouse):
    try:
        (x, y) = (mouse[0][0], mouse[0][1])

        if mouse[1] == 1:
            return {'left_click': (x, y)}
        elif mouse[1] == 3:
            return {'right_click': (x, y)}
    except:
        return {}

    return {}


def handle_level_up_menu(key):
    if key:

        if key == py.K_a:
            return {'level_up': 'Strength'}
        elif key == py.K_b:
            return {'level_up': 'Instinct'}
        elif key == py.K_c:
            return {'level_up': 'Coordination'}
        elif key == py.K_d:
            return {'level_up': 'Vitality'}
        elif key == py.K_e:
            return {'level_up': 'Arcana'}
        elif key == py.K_f:
            return {'level_up': 'Improvisation'}
        elif key == py.K_g:
            return {'level_up': 'Wisdom'}
        elif key == py.K_h:
            return {'level_up': 'Finesse'}
        elif key == py.K_i:
            return {'level_up': 'Charisma'}
        elif key == py.K_j:
            return {'level_up': 'Devotion'}

    return {}