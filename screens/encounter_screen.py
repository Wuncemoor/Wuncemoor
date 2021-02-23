from config.image_objects import ENCOUNTER_MENU, POINTER_RIGHT, ENCOUNTER_BUTTON
from data_structures.menu_structures import DescendingFancyMenu
from data_structures.menu_tools import MenuSpecs
from handlers.logic.logic_chunks import encounter_goto_targeting, encounter_goto_satchel, encounter_goto_life


def get_encounter_thinking_menu_specs():
    bg = ENCOUNTER_MENU
    specs = MenuSpecs(bg=bg, pointer_image=POINTER_RIGHT, pointer_x_offset=80, pointer_y_offset=49, pointer_delta=40,
                      button_bg=ENCOUNTER_BUTTON, button_x_offset=130, button_y_offset=60, button_gap=10, font_size=24)
    return specs


def get_encounter_thinking_menu():
    data = ['FIGHT', 'ITEM', 'RUN']
    logic = [encounter_goto_targeting, encounter_goto_satchel, encounter_goto_life]
    specs = get_encounter_thinking_menu_specs()
    menu = DescendingFancyMenu(data, logic, specs)

    return menu


