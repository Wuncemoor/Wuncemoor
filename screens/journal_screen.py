from screens.gui_tools import get_surface, get_alpha_surface, align_and_blit, get_button_surface, get_text_surface, get_wrapped_text
from config.image_objects import JOURNAL_OBJS
from config.constants import RED, DARK_RED, BLACK, YELLOW_SELECT, GREY, WHITE


def journal_screen(self):
    surf = get_surface(JOURNAL_OBJS.get('bg'))

    if self.handler.menu.sub is not None:
        ind = self.handler.menu.options.choice
        sj = self.handler.menu.sub

        j_display = journal_options_display(sj, self.game.options.current.choice)
        details = get_entry_details(sj[self.game.options.current.choice])
        surf.blit(j_display, (83, 278))
        surf.blit(details, (812, 270))
    else:
        ind = self.game.options.current.choice

    text = JOURNAL_OBJS.get('text' + str(ind))
    selected_icon = JOURNAL_OBJS.get('selected_icon')
    current = JOURNAL_OBJS.get('current')
    completed = JOURNAL_OBJS.get('completed')
    codex = JOURNAL_OBJS.get('codex')
    history = JOURNAL_OBJS.get('history')

    surf.blit(text, (71, 218))

    surf.blit(selected_icon, (825 + 75 * ind, 120))
    surf.blit(current, (825, 120))
    surf.blit(completed, (900, 120))
    surf.blit(codex, (975, 120))
    surf.blit(history, (1050, 120))

    align_and_blit(self.screen, surf)


def journal_options_display(subjournal, option):
    obj = JOURNAL_OBJS.get('selected_quest')

    surf = get_alpha_surface(obj.get_width(), obj.get_height() * len(subjournal))
    y = 0
    for i in subjournal:
        if y is option:
            color = YELLOW_SELECT
        else:
            color = GREY
        bg = get_surface(obj)
        text = get_text_surface(i.title, 30, color, 'source_sans_pro')
        bg.blit(text, (80, 5))
        surf.blit(bg, (0, 0 + (y * obj.get_height())))
    return surf


def get_entry_details(entry):
    surf = get_alpha_surface(946, 765)
    align_and_blit(surf, get_text_surface(entry.title, 36, BLACK), y_ratio=0.1)
    y_off = 130
    for i in entry.plot:
        sc = get_story_chunk(i)
        surf.blit(sc, (60, y_off))
        y_off += sc.get_height() + 30
    return surf


def get_story_chunk(chunk):
    width = 946
    titlesize = 28
    fontsize = 22
    lines = get_wrapped_text(chunk.info, width, fontsize, color=BLACK)

    surf = get_alpha_surface(width, titlesize + (fontsize * 1.2) * len(lines))
    surf.blit(get_text_surface(chunk.title, titlesize, WHITE), (0, 0))

    y = 40
    for line in lines:
        surf.blit(line, (0, y))
        y += fontsize
    return surf
