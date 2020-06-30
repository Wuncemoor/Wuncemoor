import math

from config.constants import WHITE, LIGHT_GREY
from config.image_objects import DIALOGUE_MENU
from dialogue.deja_vu_check import deja_vu_check
from screens.gui_tools import get_surface, get_text_surface


def dialogue_screen(screen, player, dialogue_handler):
    gap = 5
    portrait_off_x = 20
    name_off_y = 40
    noncom_off_x = 1030
    interactor_width = 250
    fontsize = 12
    actor_name_fontsize = 20

    window = get_surface(DIALOGUE_MENU)

    player_name = get_text_surface(player.name, actor_name_fontsize, WHITE)
    (pnw, pnh) = player_name.get_size()

    pn_off_x = (interactor_width / 2) - (pnw / 2)
    window.blit(player.images.portrait, (portrait_off_x, name_off_y + pnh + gap))
    window.blit(player_name, (pn_off_x, name_off_y))

    noncom_name = get_text_surface(dialogue_handler.partner.name.capitalize(), actor_name_fontsize, WHITE)
    nnw, nnh = noncom_name.get_width(), noncom_name.get_height()
    nn_off_x = (interactor_width / 2) - (nnw / 2)
    window.blit(dialogue_handler.partner.images.portrait, (noncom_off_x + portrait_off_x, name_off_y + nnh + gap))
    window.blit(noncom_name, (noncom_off_x + nn_off_x, name_off_y))

    dialogue = dialogue_handler.partner.noncombatant.dialogue
    current_node = dialogue.graph_dict.get(dialogue.current_convo)

    words_off_x = 285
    words_off_y = 25
    options_off_y = 296

    words = get_text_surface(current_node.words, fontsize, WHITE)

    window.blit(words, (words_off_x, words_off_y))

    text_gap = math.ceil(fontsize * 0.2)
    letter_index = ord('a')
    q = 0
    for option in dialogue_handler.real_talk:

        deja_vu = deja_vu_check(dialogue_handler, q + 1)
        if deja_vu:
            color = LIGHT_GREY
        else:
            color = WHITE
        text = get_text_surface(str(q + 1) + ' ) ' + option.text, fontsize, color)
        window.blit(text, (words_off_x, words_off_y + options_off_y + ((q * fontsize) + (q + 1) * text_gap)))
        q += 1
        letter_index += 1

    screen.blit(window, (0, 0))