from data_structures.gui_tools import get_surface, get_alpha_surface, align_and_blit, get_text_surface, get_wrapped_text
from config.image_objects import JOURNAL_OBJS
from config.constants import BLACK, YELLOW_SELECT, GREY, WHITE, SUBINVENTORY_OPTION_HEIGHT
from enums.game_states import MenuSubStates


def journal_screen(self):
    surf = get_surface(JOURNAL_OBJS.get('bg'))

    text = JOURNAL_OBJS.get('text' + str(self.handler.menu_type.menu.pointer))
    selected_icon = JOURNAL_OBJS.get('selected_icon')
    current = JOURNAL_OBJS.get('current')
    completed = JOURNAL_OBJS.get('completed')
    codex = JOURNAL_OBJS.get('codex')
    history = JOURNAL_OBJS.get('history')

    align_and_blit(surf, text, x_ratio=0.227, y_ratio=0.227)
    align_and_blit(surf, selected_icon, x_ratio=0.426+(0.05*self.handler.menu_type.menu.pointer), y_ratio=0.131)
    align_and_blit(surf, current, x_ratio=0.426, y_ratio=0.131)
    align_and_blit(surf, completed, x_ratio=0.476, y_ratio=0.131)
    align_and_blit(surf, codex, x_ratio=0.526, y_ratio=0.131)
    align_and_blit(surf, history, x_ratio=0.576, y_ratio=0.131)

    sj = self.handler.menu_type.menu.pointer_data
    if len(sj) > 0:

        j_display = journal_options_display(sj, self.handler.menu_type.menu.pointer)
        details = get_entry_details(sj.pointer_data)
        surf.blit(j_display, (int(surf.get_width()*0.05), int(surf.get_height()*0.27)))
        surf.blit(details, (int(surf.get_width()*0.43), int(surf.get_height()*0.255)))

    if self.handler.menu_type.state is MenuSubStates.SELECTED_OPTIONS:
        display_quest_options(self, surf)

    align_and_blit(self.screen, surf)


def journal_options_display(subjournal, option):
    obj = JOURNAL_OBJS.get('selected_quest')

    surf = get_alpha_surface(obj.get_width(), obj.get_height() * len(subjournal))
    y = 0
    for i in subjournal:
        if y is option:
            color = YELLOW_SELECT
            bg = get_surface(obj)
        else:
            color = GREY
            bg = get_alpha_surface(obj.get_width(), obj.get_height())
        text = get_text_surface(i.title, 18, color, 'source_sans_pro')
        align_and_blit(bg, text)
        surf.blit(bg, (0, 0 + (y * obj.get_height())))
    return surf


def get_entry_details(entry):
    surf = get_alpha_surface(367, 400)
    align_and_blit(surf, get_text_surface(entry.title, 22, BLACK), y_ratio=0.1)
    y_off = 80
    for i in entry.plot:
        sc = get_story_chunk(i)
        surf.blit(sc, (30, y_off))
        y_off += sc.get_height() + 30
    return surf


def get_story_chunk(chunk):
    width = 300
    titlesize = 18
    fontsize = 14
    lines = get_wrapped_text(chunk.info, width, fontsize, color=BLACK)

    surf = get_alpha_surface(width, titlesize + (fontsize * 1.2) * len(lines))
    surf.blit(get_text_surface(chunk.title, titlesize, WHITE), (0, 0))

    y = 20
    for line in lines:
        surf.blit(line, (0, y))
        y += fontsize
    return surf


def display_quest_options(self, surf):
    menu = self.game.options.current
    window = menu.get_window_image()

    surf.blit(window, (surf.get_width()*0.25, surf.get_height()*0.3 + SUBINVENTORY_OPTION_HEIGHT*self.handler.menu_type.submenu.pointer))

