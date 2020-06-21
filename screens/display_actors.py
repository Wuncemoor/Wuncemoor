from screens.gui_tools import get_alpha_surface
from enums.game_states import EncounterStates
from config.image_objects import INDICATOR_V


def display_actors(player, encounter):
    w, h = 1280, 300
    window = get_alpha_surface(w, h)
    dim = 160
    off_x = (w / 4) - (dim / 2)
    off_y = (h / 2) - (dim / 2)

    window.blit(player.combatant.images.actor, (off_x, off_y))
    if encounter.event.combatant:
        window.blit(encounter.event.combatant.images.actor, (off_x + (w / 2), off_y))

    if encounter.state == EncounterStates.FIGHT_TARGETING:
        window.blit(INDICATOR_V, ((3 * w / 4) - (INDICATOR_V.get_width() / 2), off_y - 40))

    return window
