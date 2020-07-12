import math
import pygame as py
from config.image_objects import INVENTORY_BG, INVENTORY_OPTIONS, EQUIPMENT_BG, INDICATOR_H
from screens.gui_tools import get_surface, align_and_blit, get_alpha_surface, get_text_surface


def inventory_screen(self):

    surf = get_surface(INVENTORY_BG)
    if self.handler.display is None:
        options = INVENTORY_OPTIONS[self.handler.current_option]
        subgroup = self.handler.menu.subgroups[self.handler.current_option]
    else:
        ind = self.handler.options.index(self.handler.display)
        options = INVENTORY_OPTIONS[ind]
        surf.blit(INDICATOR_H, (410, 130 + (32 * self.handler.current_option)))
        subgroup = self.handler.menu.subgroups[ind]
    sg = display_subgroup(subgroup)

    align_and_blit(surf, options, x_ratio=0.75, y_ratio=0.19)
    align_and_blit(surf, EQUIPMENT_BG, x_ratio=0.1, y_ratio=0.58)
    surf.blit(sg, (470, 135))

    align_and_blit(self.screen, surf)

    return surf


def display_subgroup(subgroup):
    option_height = 32

    surf = get_alpha_surface(200, len(subgroup) * option_height)
    y = 0
    for unit in subgroup:
        mini = unit.images.port_mini
        text = get_text_surface(unit.name, fontsize=16)
        window = get_alpha_surface(200, option_height)
        window.blit(mini, (0, 0))
        window.blit(text, (35, 12))
        surf.blit(window, (0, y * option_height))
        y += 1
    return surf


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
            else:
                options.append(item.name)

    inventory_width = 200
    inventory_height = 400
    off_x = 16
    off_y = 21

    menu(screen, header, fontsize, options, inventory_width, inventory_height, off_x, off_y)


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