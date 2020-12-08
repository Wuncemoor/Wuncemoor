from screens.gui_tools import get_alpha_surface, get_text_surface
from config.image_objects import RESOURCE_HUD
from config.constants import WHITE, YELLOW, ORANGE, DARK_RED, GREY


def player_resource_display(player):
    res_display = get_alpha_surface(320, 180)

    blit_portrait(res_display, player)

    blit_resource_bars(res_display, player)

    blit_letters(res_display)

    return res_display


def blit_portrait(res_display, player):
    frame_off_x = 20
    frame_off_y = 40
    port_off_x = frame_off_x + 3
    port_off_y = frame_off_y + 3

    res_display.blit(player.images.port_mini, (port_off_x, port_off_y))
    res_display.blit(RESOURCE_HUD.get('frame'), (frame_off_x, frame_off_y))


def blit_resource_bars(res_display, player):
    blit_resource_frames(res_display)

    for i in ['HP', 'MP', 'TP', 'VP']:
        blit_resource_bar(res_display, player, i)


def blit_resource_frames(res_display):
    bar_off_x = 94
    bar_off_y = 40

    for i in range(4):
        res_display.blit(RESOURCE_HUD.get('resource_bar'), (bar_off_x, bar_off_y))
        bar_off_y += 25


def blit_resource_bar(res_display, player, stat):
    percent, now_val, max_val, font_color = get_resource_vals(player, stat)

    if stat == 'HP':
        text = get_text_surface(str(now_val) + ' / ' + str(max_val), 25, font_color)

        hp_values_off_x = 157
        hp_values_off_y = get_res_val_off_y(stat)
        res_display.blit(text, (hp_values_off_x, hp_values_off_y))

    else:
        text = get_text_surface(str(now_val) + ' / ' + str(max_val), 12, font_color)

        values_off_x = 225
        values_off_y = get_res_val_off_y(stat)
        res_display.blit(text, (values_off_x, values_off_y))

    blit_resource_real(res_display, stat, percent)


def get_resource_vals(player, stat):
    hp_dict = {'current': player.combatant.attributes.current_hp, 'max': player.combatant.max_hp}
    mp_dict = {'current': player.combatant.attributes.current_mp, 'max': player.combatant.max_mp}
    tp_dict = {'current': player.combatant.attributes.current_tp, 'max': player.combatant.max_tp}
    vp_dict = {'current': player.combatant.attributes.current_vp, 'max': player.combatant.max_vp}

    stat_dict = {'HP': hp_dict, 'MP': mp_dict, 'TP': tp_dict, 'VP': vp_dict}

    now_val = stat_dict.get(stat).get('current')
    max_val = stat_dict.get(stat).get('max')
    percent = float(now_val / max_val) * 100

    font_color = get_resource_font_color(percent)

    return percent, now_val, max_val, font_color


def blit_resource_real(res_display, stat, percent):
    chunk_x_off = 8
    x_off = 94
    y_off = get_real_offset_y(stat)
    for i in range(100):
        img = get_resource_real_img(i, stat)
        if percent >= i:
            res_display.blit(img, (x_off + chunk_x_off, y_off))
        chunk_x_off += 2


def get_real_offset_y(stat):
    if stat == 'HP':
        y = 40
    elif stat == 'MP':
        y = 65
    elif stat == 'TP':
        y = 90
    elif stat == 'VP':
        y = 115

    return y

def blit_letters(res_display):
    letters_off_x = 109

    hp_letters = RESOURCE_HUD.get('HP')
    hp_off_x = letters_off_x - 18
    hp_off_y = 15
    res_display.blit(hp_letters, (hp_off_x, hp_off_y))

    mp_letters = RESOURCE_HUD.get('MP')
    mp_off_y = 60
    res_display.blit(mp_letters, (letters_off_x, mp_off_y))

    tp_letters = RESOURCE_HUD.get('TP')
    tp_off_y = 85
    res_display.blit(tp_letters, (letters_off_x, tp_off_y))

    vp_letters = RESOURCE_HUD.get('VP')
    vp_off_y = 110
    res_display.blit(vp_letters, (letters_off_x, vp_off_y))


def get_resource_real_img(i, stat):
    if i == 0:
        img = RESOURCE_HUD.get(stat + 'left0')
    elif i == 1:
        img = RESOURCE_HUD.get(stat + 'left1')
    elif i == 98:
        img = RESOURCE_HUD.get(stat + 'right0')
    elif i == 99:
        img = RESOURCE_HUD.get(stat + 'right1')
    else:
        img = RESOURCE_HUD.get(stat + 'mid')
    return img


def get_res_val_off_y(stat):
    val = {
        'HP': 12,
        'MP': 52,
        'TP': 77,
        'VP': 102,
    }
    return val.get(stat)


def get_resource_font_color(percent):
    color_list = [(50, WHITE), (35, YELLOW), (15, ORANGE), (0, DARK_RED)]

    for threshold in color_list:
        if percent > threshold[0]:
            return threshold[1]
    return GREY
