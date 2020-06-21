import pygame as py
import math
from dialogue.deja_vu_check import deja_vu_check
from screens.resources_HUD import player_resource_display
from screens.encounter_menu import get_encounter_menus
from screens.display_actors import display_actors
from screens.message_box import get_message_box
from config.constants import CSCREEN, MINI_MAP, WHITE, LIGHT_GREY
from config.image_objects import INVENTORY_MENU, LEVELUP_MENU, DIALOGUE_MENU, ENCOUNTER_MESSAGE_BG, MINIMAP
from screens.gui_tools import get_surface, get_text_surface


def menu(screen, gui_img, constants, options):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')

    (width, height, off_x, off_y, fontsize) = constants

    menu = py.Surface((width, height))

    menu.blit(gui_img, (0, 0))

    font = py.font.SysFont("comicsansms", fontsize)

    # print all the options
    gap = math.ceil(fontsize * 0.2)
    q = 0
    letter_index = ord('a')
    for option_text in options:
        text = font.render('(' + chr(letter_index) + ') ' + option_text, True, (255, 255, 255))
        menu.blit(text, (off_x, off_y + ((q * fontsize) + (q + 1) * gap)))
        q += 1
        letter_index += 1

    # blit the contents of "window" to the root console
    x = int((screen.get_width() / 2) - (width / 2))
    y = int((screen.get_height() / 2) - (height / 2))
    screen.blit(menu, (x, y))


def inventory_menu(screen, header, player):
    fontsize = 12
    # show a menu with each item of the inventory as an option
    if len(player.combatant.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.combatant.inventory.items:
            if player.combatant.equipment.main_hand == item:
                options.append('{0} (Main Hand)'.format(item.name))
            elif player.combatant.equipment.off_hand == item:
                options.append('{0} (Off Hand)'.format(item.name))
            elif player.combatant.equipment.head == item:
                options.append('{0} (Head)'.format(item.name))
            elif player.combatant.equipment.body == item:
                options.append('{0} (Body)'.format(item.name))
            elif player.combatant.equipment.feet == item:
                options.append('{0} (Feet)'.format(item.name))
            elif player.combatant.equipment.belt == item:
                options.append('{0} (Belt)'.format(item.name))
            elif player.combatant.equipment.hands == item:
                options.append('{0} (Hands)'.format(item.name))
            elif player.combatant.equipment.finger == item:
                options.append('{0} (Finger)'.format(item.name))
            elif player.combatant.equipment.neck == item:
                options.append('{0} (Neck)'.format(item.name))
            elif player.combatant.equipment.back == item:
                options.append('{0} (Back)'.format(item.name))
            elif player.combatant.equipment.accessory == item:
                options.append('{0} (Accessory)'.format(item.name))
            else:
                options.append(item.name)

    inventory_width = 200
    inventory_height = 400
    off_x = 16
    off_y = 21

    (width, height) = CSCREEN
    menu(screen, header, INVENTORY_MENU, fontsize, options, inventory_width, inventory_height, width, height,
         off_x, off_y)


def level_up_menu(screen, player):
    att = player.combatant.attributes
    options = ['Strength ({0} -> {1})'.format(att.strength, att.strength + 1),
               'Instinct ({0} -> {1})'.format(att.instinct, att.instinct + 1),
               'Coordination ({0} -> {1})'.format(att.coordination, att.coordination + 1),
               'Vitality ({0} -> {1})'.format(att.vitality, att.vitality + 1),
               'Arcana ({0} -> {1})'.format(att.arcana, att.arcana + 1),
               'Improvisation ({0} -> {1})'.format(att.improvisation, att.improvisation + 1),
               'Wisdom ({0} -> {1})'.format(att.wisdom, att.wisdom + 1),
               'Finesse ({0} -> {1})'.format(att.finesse, att.finesse + 1),
               'Charisma ({0} -> {1})'.format(att.charisma, att.charisma + 1),
               'Devotion ({0} -> {1})'.format(att.devotion, att.devotion + 1)]
    fontsize = 14
    menu_width = 200
    menu_height = 200
    off_x = 16
    off_y = 21
    (width, height) = CSCREEN
    gui_img = LEVELUP_MENU
    menu(screen, gui_img, fontsize, options, menu_width, menu_height, width, height, off_x, off_y)


def minimp_menu(screen, world_map):
    (width, height) = MINI_MAP
    (cwidth, cheight) = CSCREEN

    window = py.Surface((width, height))
    offset_x = 50
    offset_y = 50
    i, j = 0, 0

    for row in world_map:
        for tile in row:
            img = MINIMAP.get(tile.type)
            window.blit(img, (offset_x + i, offset_y + j))
            j += 1
        i += 1
        j = 0

    x = cwidth // 2 - width // 2
    y = cheight // 2 - height // 2
    screen.blit(window, (x, y))


def dialogue_menu(screen, player, dialogue_handler):
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
