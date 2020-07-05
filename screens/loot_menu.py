from screens.gui_tools import get_alpha_surface, get_text_surface, blit_options
from enums.game_states import RewardStates
from config.image_objects import ENCOUNTER_BUTTON, INDICATOR_H
from config.constants import BLACK


def get_reward_menu(reward):

    menu = get_alpha_surface(400, 240)

    off_x = 110
    off_y = 110
    dy = 40
    fontsize = 24

    blit_options(menu, ENCOUNTER_BUTTON, off_x, off_y, dy, reward.options, fontsize)
    if reward.state == RewardStates.THINKING:
        menu.blit(INDICATOR_H, (off_x - 50, off_y - 11 + (dy * reward.current_option)))

    return menu


def display_loot(reward):
    window = get_alpha_surface(1280, 300)

    y1 = 0
    for item in reward.loot.items:
        window.blit(item.images.port_mini, (120, 40 + (100 * y1)))
        text = get_text_surface(item.name, fontsize=20, color=BLACK)
        window.blit(text, (210, 70 + (100 * y1)))
        y1 += 1
    y2 = 0
    bonus_y = 640
    for item in reward.loot.claimed:
        window.blit(item.images.port_mini, (120 + bonus_y, 40 + (100 * y2)))
        text = get_text_surface(item.name, fontsize=20, color=BLACK)
        window.blit(text, (210 + bonus_y, 40 + (100 * y2)))
        y2 += 1

    if reward.state == RewardStates.SIFTING:
        window.blit(INDICATOR_H, (80, 60 + (reward.current_option * 100)))
    elif reward.state == RewardStates.DEPOSITING:
        window.blit(INDICATOR_H, (80 + bonus_y, 60 + reward.current_option * 100))

    return window


def display_resources_gain(loot):

    surf = get_alpha_surface(100, 100)
    text = get_text_surface('XP: ' + str(loot.xp), 20, BLACK)
    surf.blit(text, (0, 0))
    return surf
