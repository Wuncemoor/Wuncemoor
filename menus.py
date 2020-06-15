import pygame as py
import math
from dialogue.deja_vu_check import deja_vu_check
from screens.resources_HUD import player_resource_display
from screens.encounter_menu import get_encounter_menus
from screens.display_actors import display_actors
from screens.message_box import get_message_box


def menu(screen, header, gui_img, fontsize, options, width, height, camera_width, camera_height, off_x, off_y):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')




    # create an off-screen console that represents the menu's window
    menu = py.Surface((width, height))

    menu.blit(gui_img, (0, 0))

    # print the header, with auto-wrap

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
    x = int((camera_width / 2) - (width / 2))
    y = int((camera_height / 2) - (height / 2))
    screen.blit(menu, (x, y))


def inventory_menu(screen, header, gui_img, player, camera_width, camera_height):
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

    menu(screen, header, gui_img, fontsize, options, inventory_width, inventory_height, camera_width, camera_height,
         off_x, off_y)


def main_menu(screen, screen_width, screen_height, bg_img, gui_img, fontsize):
    screen.blit(bg_img, (0, 0))
    font = py.font.SysFont("comicsansms", fontsize)
    titletext = font.render('WUNCEMOOR: THE ETERNAL DREAM', True, (255, 255, 255))


    menu_width = 650
    menu_height = 170
    off_x = 35
    off_y = -3

    screen.blit(titletext, (int(screen_width / 4), int(screen_height / 10)))

    menu(screen, '', gui_img, fontsize, ['Start A New Game', 'Continue Previous Game', 'Quit'], menu_width, menu_height,
         screen_width, screen_height, off_x, off_y)


def level_up_menu(screen, header, gui_img, player, camera_width, camera_height):
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
    menu(screen, header, gui_img, fontsize, options, menu_width, menu_height, camera_width, camera_height, off_x, off_y)


def map_menu(screen, world_map, images, mm_width, mm_height, camera_width, camera_height):
    window = py.Surface((mm_width, mm_height))
    offset_x = 50
    offset_y = 50
    i, j = 0, 0

    for row in world_map:
        for tile in row:
            img = images.get(tile.type)
            window.blit(img, (offset_x + i, offset_y + j))
            j += 1
        i += 1
        j = 0


    x = camera_width // 2 - mm_width // 2
    y = camera_height // 2 - mm_height // 2
    screen.blit(window, (x, y))


def dialogue_menu(screen, gui_img, player, dialogue_handler, camera_width, camera_height):

    gap = 5
    portrait_off_x = 20
    name_off_y = 40
    noncom_off_x = 1030
    interactor_width = 250

    actor_name_fontsize = 20
    actor_font = py.font.SysFont("comicsansms", actor_name_fontsize)

    fontsize = 12
    font = py.font.SysFont("comicsansms", fontsize)

    window = py.Surface((camera_width, camera_height))
    window.blit(gui_img, (0, 0))

    player_name = actor_font.render(player.name, True, (255, 255, 255))
    pnw, pnh = player_name.get_width(), player_name.get_height()
    pn_off_x = (interactor_width / 2) - (pnw / 2)
    window.blit(player.images.portrait, (portrait_off_x, name_off_y + pnh + gap))
    window.blit(player_name, (pn_off_x, name_off_y))


    noncom_name = actor_font.render(dialogue_handler.partner.name.capitalize(), True, (255, 255, 255))
    nnw, nnh = noncom_name.get_width(), noncom_name.get_height()
    nn_off_x = (interactor_width / 2) - (nnw / 2)
    window.blit(dialogue_handler.partner.images.portrait, (noncom_off_x + portrait_off_x, name_off_y + nnh + gap))
    window.blit(noncom_name, (noncom_off_x + nn_off_x, name_off_y))

    dialogue = dialogue_handler.partner.noncombatant.dialogue
    current_node = dialogue.graph_dict.get(dialogue.current_convo)

    words_off_x = 285
    words_off_y = 25
    options_off_y = 296

    words = font.render(current_node.words, True, (255, 255, 255))

    window.blit(words, (words_off_x, words_off_y))

    text_gap = math.ceil(fontsize * 0.2)
    letter_index = ord('a')
    q = 0
    for option in dialogue_handler.real_talk:

        deja_vu = deja_vu_check(dialogue_handler, q + 1)
        if deja_vu:
            text = font.render(str(q + 1) + ' ) ' + option.text, True, (190, 190, 190))
        else:
            text = font.render(str(q + 1) + ' ) ' + option.text, True, (255, 255, 255))
        window.blit(text, (words_off_x, words_off_y + options_off_y + ((q * fontsize) + (q + 1) * text_gap)))
        q += 1
        letter_index += 1

    screen.blit(window, (0, 0))


def encounter_screen(screen, images, player, encounter, message_log):

    screen.blit(encounter.background, (0, 0))


    resource_hud = player_resource_display(player, images.get('gui').get('resource_hud_objs'))
    screen.blit(resource_hud, (0, 0))

    options_menu = get_encounter_menus(images.get('gui').get('encounter'), encounter)
    screen.blit(options_menu, (0, 480))

    message_box = get_message_box(images.get('gui').get('encounter_message_bg'), message_log, off_x=15, off_y=5)
    screen.blit(message_box, (940, 490))


    actor_display = display_actors(player, encounter, images.get('gui').get('encounter').get('indicator_v'))
    screen.blit(actor_display, (0, 180))




def message_box(screen, width, screen_width, screen_height):
    fontsize = 12

    menu(screen, '', fontsize, ['No save game to load :('], width, screen_width, screen_height)



class MenuHandler:
    def __init__(self):
        self.state = None
        self.display = None
        self.options = None
        self.current_option = 0
        self.menu = None

    def handle_menu(self, menu_obj):
        self.menu = menu_obj
        self.state = menu_obj.superstate
        self.options = menu_obj.options
        self.current_option = 0




