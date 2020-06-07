from screens.gui_tools import get_alpha_surface


def display_actors(player, enemy):
    w, h = 1280, 300
    window = get_alpha_surface(w, h)
    dim = 160
    off_x = (w / 4) - (dim / 2)
    off_y = (h / 2) - (dim / 2)

    window.blit(player.combatant.images.actor, (off_x, off_y))
    window.blit(enemy.combatant.images.actor, (off_x + (w / 2), off_y))

    return window
