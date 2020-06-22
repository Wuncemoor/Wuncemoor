from screens.gui_tools import get_alpha_surface, align_and_blit, get_button_surface, get_text_surface, get_wrapped_text
from config.image_objects import JOURNAL_OBJS
from config.constants import RED, DARK_RED, BLACK

def journal_screen(screen, menu_handler):
    surf = get_alpha_surface(550, 530)

    surf.blit(JOURNAL_OBJS.get('bg'), (0, 0))

    if menu_handler.display is not None:
        ind = menu_handler.options.index(menu_handler.display)
        sj = menu_handler.menu.get_subjournal(menu_handler.display)

        j_display = journal_options_display(sj, menu_handler.current_option)
        details = get_entry_details(sj[menu_handler.current_option])
        surf.blit(j_display, (30, 112))
        surf.blit(details, (275, 0))
    else:
        ind = menu_handler.current_option

    text = JOURNAL_OBJS.get('text' + str(ind))
    icon = JOURNAL_OBJS.get('icon' + str(ind))
    surf.blit(text, (78, 43))
    surf.blit(icon, (92 + 25 * ind, 72))

    align_and_blit(screen, surf)


def journal_options_display(subjournal, option):
    obj = JOURNAL_OBJS.get('quest_holder')

    surf = get_alpha_surface(obj.get_width(), obj.get_height() * len(subjournal))
    y = 0
    for i in subjournal:
        if y is option:
            color = RED
        else:
            color = BLACK
        surf.blit(get_button_surface(obj, i.title, 16, color), (0, 0 + (y * obj.get_height())))
    return surf

def get_entry_details(entry):
    surf = get_alpha_surface(275, 530)
    surf.blit(get_text_surface(entry.title, 14, DARK_RED), (25, 55))
    y_off = 90
    for i in entry.plot:
        sc = get_story_chunk(i)
        surf.blit(sc, (30, y_off))
        y_off += sc.get_height() + 5
    return surf

def get_story_chunk(chunk):
    width = 200
    titlesize = 12
    fontsize = 10
    lines = get_wrapped_text(chunk.info, width, fontsize, color=RED)

    surf = get_alpha_surface(width, titlesize + (fontsize * 1.2) * len(lines))
    surf.blit(get_text_surface(chunk.title, titlesize, DARK_RED), (0, 0))

    y = 15
    for line in lines:
        surf.blit(line, (0, y))
        y += fontsize
    return surf
