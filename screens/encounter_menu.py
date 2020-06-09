from screens.gui_tools import get_alpha_surface, blit_options
from enums.game_states import EncounterStates


def get_encounter_menus(images, encounter):

    menu = get_alpha_surface(400, 240)

    menu_off_x = 60
    menu_off_y = 0
    menu.blit(images.get('encounter_menu'), (menu_off_x, menu_off_y))

    buttons_off_x = 130
    buttons_off_y = 30

    dy = 40
    blit_options(menu, images.get('button'), buttons_off_x, buttons_off_y, dy, encounter.options, fontsize=24)

    if encounter.state == EncounterStates.THINKING:
        menu.blit(images.get('indicator_h'), (buttons_off_x - 50, buttons_off_y - 11 + (dy * encounter.current_option)))

    return menu



