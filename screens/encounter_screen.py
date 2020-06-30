from screens.display_actors import display_actors
from screens.gui_tools import get_alpha_surface, blit_options, align_and_blit
from enums.game_states import EncounterStates
from config.image_objects import ENCOUNTER_MENU, ENCOUNTER_BUTTON, INDICATOR_H, ENCOUNTER_MESSAGE_BG
from screens.message_box import get_message_box
from screens.resources_HUD import player_resource_display


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


def encounter_screen(screen, player, encounter, message_log):

    screen.blit(encounter.background, (0, 0))

    resource_hud = player_resource_display(player)
    screen.blit(resource_hud, (0, 0))

    options_menu = get_encounter_menus(encounter)
    screen.blit(options_menu, (0, 480))

    message_box = get_message_box(ENCOUNTER_MESSAGE_BG, message_log, off_x=15, off_y=5)
    screen.blit(message_box, (940, 490))

    actor_display = display_actors(player, encounter)
    screen.blit(actor_display, (0, 180))
