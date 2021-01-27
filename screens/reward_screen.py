from data_structures.menu_tools import MenuSpecs
from data_structures.gui_tools import get_alpha_surface, get_text_surface
from enums.game_states import RewardStates
from config.image_objects import ENCOUNTER_BUTTON, POINTER_RIGHT, REWARD_BG
from config.constants import BLACK
from data_structures.menu_structures import FancyMenu
from handlers.logic.logic_chunks import reward_auto, reward_manual, reward_goto_life, reward_sifting, reward_depositing


def get_reward_menu_specs():
    specs = MenuSpecs(bg=REWARD_BG, pointer_image=None, )


def get_reward_menu():
    data = [get_reward_thinking_menu(), get_reward_sifting_menu(), get_reward_depositing_menu()]
    logic = []
    specs = get_reward_menu_specs()


def get_reward_thinking_specs():
    specs = MenuSpecs(bg=REWARD_BG, pointer_image=POINTER_RIGHT, pointer_x_offset=60, pointer_y_offset=38,
                      pointer_delta=40, button_bg=ENCOUNTER_BUTTON, button_x_offset=110, button_y_offset=110,
                      button_gap=10, font_size=24)
    return specs

def get_reward_thinking_menu():
    data = ['AUTO', 'MANUAL', 'LEAVE']
    logic = [reward_auto, reward_manual, reward_goto_life]
    specs = get_reward_thinking_specs()

    return FancyMenu(data, logic, specs)

def get_reward_sifting_menu_specs():
    specs = MenuSpecs(pointer_image=POINTER_RIGHT, )
    return specs

def get_reward_sifting_menu():
    data = []
    logic = reward_sifting
    specs = get_reward_sifting_menu_specs()

def get_reward_depositing_menu_specs():
    specs = MenuSpecs()
    return specs

def get_reward_depositing_menu():
    data = []
    logic = reward_depositing
    specs = get_reward_depositing_menu_specs()


def display_loot(reward):
    window = get_alpha_surface(1280, 300)

    y1 = 0
    for item in reward.loot.items:
        window.blit(item.images.sprite, (120, 40 + (100 * y1)))
        text = get_text_surface(item.name, fontsize=20, color=BLACK)
        window.blit(text, (210, 70 + (100 * y1)))
        y1 += 1
    y2 = 0
    bonus_y = 640
    for item in reward.loot.claimed:
        window.blit(item.images.sprite, (120 + bonus_y, 40 + (100 * y2)))
        text = get_text_surface(item.name, fontsize=20, color=BLACK)
        window.blit(text, (210 + bonus_y, 40 + (100 * y2)))
        y2 += 1
    choice = reward.owner.options.current.choice
    if reward.state == RewardStates.SIFTING:
        window.blit(POINTER_RIGHT, (80, 60 + (choice * 100)))
    elif reward.state == RewardStates.DEPOSITING:
        window.blit(POINTER_RIGHT, (80 + bonus_y, 60 + choice * 100))

    return window


def display_resources_gain(loot):

    surf = get_alpha_surface(100, 100)
    text = get_text_surface('XP: ' + str(loot.xp), 20, BLACK)
    surf.blit(text, (0, 0))
    return surf
