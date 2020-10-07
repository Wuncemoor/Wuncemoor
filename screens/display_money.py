from config.constants import BLACK
from screens.gui_tools import get_alpha_surface, get_text_surface
from config.image_objects import GOLD, SILVER, COPPER


def display_money(value: int, color: tuple = BLACK):
    val_str = str(value)

    if value >= 10000:
        surf = get_alpha_surface(90, 12)
        g_str = get_text_surface(val_str[0], color=color)
        s_str = get_text_surface(val_str[1:2], color=color)
        c_str = get_text_surface(val_str[3:4], color=color)
        surf.blit(GOLD, (0, 1))
        surf.blit(g_str, (15, 0))
        surf.blit(SILVER, (30, 1))
        surf.blit(s_str, (45, 0))
        surf.blit(COPPER, (60, 1))
        surf.blit(c_str, (75, 0))

    elif value >= 1000:
        surf = get_alpha_surface(60, 12)
        s_str = get_text_surface(val_str[0:1], color=color)
        c_str = get_text_surface(val_str[2:3], color=color)
        surf.blit(SILVER, (0, 1))
        surf.blit(s_str, (15, 0))
        surf.blit(COPPER, (30, 1))
        surf.blit(c_str, (45, 0))

    elif value >= 100:

        surf = get_alpha_surface(60, 12)
        s_str = get_text_surface(val_str[0], color=color)
        c_str = get_text_surface(val_str[1:2], color=color)
        surf.blit(SILVER, (0, 1))
        surf.blit(s_str, (15, 0))
        surf.blit(COPPER, (30, 1))
        surf.blit(c_str, (45, 0))

    else:
        surf = get_alpha_surface(30, 12)
        c_str = get_text_surface(val_str, color=color)
        surf.blit(COPPER, (0, 1))
        surf.blit(c_str, (15, 0))

    return surf
