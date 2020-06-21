from screens.gui_tools import get_alpha_surface, blit_options, align_and_blit
from enums.game_states import EncounterStates
from config.image_objects import ENCOUNTER_MENU, ENCOUNTER_BUTTON, INDICATOR_H


def get_encounter_menus(encounter):

    menu = get_alpha_surface(400, 240)

    align_and_blit(menu, ENCOUNTER_MENU)

    buttons_off_x = 130
    buttons_off_y = 60

    dy = 40
    blit_options(menu, ENCOUNTER_BUTTON, buttons_off_x, buttons_off_y, dy, encounter.options, fontsize=24)

    if encounter.state == EncounterStates.THINKING:
        menu.blit(INDICATOR_H, (buttons_off_x - 50, buttons_off_y - 11 + (dy * encounter.current_option)))

    return menu
