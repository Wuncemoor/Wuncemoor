from config.constants import WHITE, GREY
from config.image_objects import DIALOGUE_BG
from data_structures.gui_tools import get_surface, get_text_surface, align_and_blit, get_alpha_surface, get_wrapped_text, \
    get_wrapped_text_surface


def dialogue_screen(self):
    display = get_surface(DIALOGUE_BG)
    surf = get_alpha_surface(display.get_width(), int(display.get_height()*1.5))
    partner = self.handler.partner

    partner_name = get_text_surface(partner.name.capitalize(), fontsize=24, color=WHITE)

    display.blit(partner_name, (int(display.get_width()*0.1), int(display.get_height()*0.05)))
    align_and_blit(surf, partner.images.portrait, y_ratio=0.12)

    dialogue = self.handler.partner.noncombatant.dialogue
    current_node = dialogue.graph_dict.get(dialogue.conversation)
    words = get_wrapped_text_surface(current_node.words, width=int(display.get_width()*0.95), fontsize=18, color=WHITE)
    display.blit(words, (int(display.get_width()*0.025), int(display.get_height()*0.05 + partner_name.get_height())))

    options = get_dialogue_options(self)
    display.blit(options, (int(display.get_width()*0.025), int(display.get_height()*0.505)))

    surf.blit(display, (surf.get_width()-display.get_width(), surf.get_height()-display.get_height()))
    align_and_blit(self.screen, surf, y_ratio=0.65)


def get_dialogue_options(self):
    window_height_total = 0
    line_blit_height = 0
    option_list = []
    q = 1
    for option in self.handler.real_talk:

        deja_vu = self.handler.deja_vu_check(q)
        if deja_vu:
            color = GREY
        else:
            color = WHITE
        lines = get_wrapped_text(str(q) + ' ) ' + option.text, width=950, fontsize=18, color=color)
        option_list.extend(lines)
        for line in lines:
            window_height_total += line.get_height()
        q += 1
    window = get_alpha_surface(width=950, height=window_height_total)
    for option in option_list:
        window.blit(option, (0, line_blit_height))
        line_blit_height += option.get_height()

    return window
