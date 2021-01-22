from pygame import draw
from pygame.transform import scale
from config.constants import WHITE, BLACK, DARK_GREY, SUBINVENTORY_OPTION_WIDTH, SUBINVENTORY_OPTION_HEIGHT
from config.image_objects import INVENTORY_BG, INVENTORY_ICONS, EQUIPMENT_EMPTY_DICT, EQUIPMENT_SLOT_BORDER, \
    POINTER_RIGHT
from enums.game_states import MenuSubStates
from misc_functions.split_money_value import split_money
from data_structures.gui_tools import get_surface, align_and_blit, get_alpha_surface, get_text_surface


def inventory_screen(self):
    surf = get_surface(INVENTORY_BG)

    display_name_and_portrait(self.game.party.p1, surf)
    display_equipment_icons(self.game.party.p1, surf)
    display_selected_icon(self, surf)
    display_subinventory(self, surf)
    if self.handler.menu_type.state is MenuSubStates.SELECTED_OPTIONS:
        display_entity_options(self, surf)
    display_mass_capacities(self.game.party, surf)
    display_wealth(self.game.party.inventory.money, surf)

    align_and_blit(self.screen, surf)


def display_name_and_portrait(player, surf):
    p_name = get_text_surface(player.name, fontsize=25, color=WHITE, style='source_sans_pro')
    align_and_blit(surf, p_name, x_ratio=0.23, y_ratio=0.25)
    align_and_blit(surf, player.images.portrait, x_ratio=0.23)


def display_equipment_icons(player, surf):

    window = get_alpha_surface(300, 450)

    slots = ['head', 'shoulders', 'chest', 'arms', 'wrists', 'hands', 'legs', 'feet', 'face', 'neck', 'back',
             'waist', 'finger1', 'finger2', 'satchel', 'weapon1', 'weapon2', 'quiver', 'food', 'drink']
    for slot in slots:
        if slot == 'quiver':
            display_equipment_icon(window, player.combatant.equipment, slot, mini=True)
        else:
            display_equipment_icon(window, player.combatant.equipment, slot)

    align_and_blit(surf, window, x_ratio=0.23, y_ratio=0.595)


def display_equipment_icon(window, eq, slot, mini=False):

    string_to_slot_dict = {'head': eq.head, 'shoulders': eq.shoulders, 'chest': eq.chest, 'arms': eq.arms,
                           'wrists': eq.wrists, 'hands': eq.hands, 'legs': eq.legs, 'feet': eq.feet,
                           'face': eq.face, 'neck': eq.neck, 'back': eq.back, 'waist': eq.waist,
                           'finger1': eq.finger1, 'finger2': eq.finger2, 'satchel': eq.satchel, 'weapon1': eq.main_hand,
                           'weapon2': eq.off_hand, 'quiver': eq.quiver, 'food': eq.food, 'drink': eq.drink}
    icon_ratio_dicts = {'head': (25, 24), 'shoulders': (25, 70), 'chest': (25, 116), 'arms': (25, 162),
                        'wrists': (25, 208), 'hands': (25, 254), 'legs': (25, 300), 'feet': (25, 346),
                        'face': (267, 24), 'neck': (267, 70), 'back': (267, 116), 'waist': (267, 162),
                        'finger1': (267, 208), 'finger2': (267, 254), 'satchel': (267, 346), 'weapon1': (112, 340),
                        'weapon2': (158, 340), 'quiver': (198, 345), 'food': (120, 410), 'drink': (170, 410)}

    if string_to_slot_dict.get(slot) is None:
        img = EQUIPMENT_EMPTY_DICT.get(slot)
    else:
        img = get_alpha_surface(48, 48)
        img.fill(BLACK)
        align_and_blit(img, scale(string_to_slot_dict.get(slot).item.equippable.images.sprite,
                                  (int(img.get_width()*7/8), int(img.get_height()*7/8))))

    x_ratio, y_ratio = icon_ratio_dicts.get(slot)

    if mini:
        shrink = (int(img.get_width()*11/10), int(img.get_height()*11/10))
        align_and_blit(window, img, x_ratio=x_ratio / window.get_width(), y_ratio=y_ratio / window.get_height())
        align_and_blit(window, scale(EQUIPMENT_SLOT_BORDER, shrink), x_ratio=x_ratio / window.get_width(),
                       y_ratio=y_ratio / window.get_height())
    else:
        align_and_blit(window, img, x_ratio=x_ratio/window.get_width(), y_ratio=y_ratio/window.get_height())
        align_and_blit(window, EQUIPMENT_SLOT_BORDER, x_ratio=x_ratio/window.get_width(),
                       y_ratio=y_ratio/window.get_height())

    return None


def display_selected_icon(self, surf):
    index = self.handler.menu_type.menu.pointer
    selected_icon = INVENTORY_ICONS[index]
    align_and_blit(surf, selected_icon, x_ratio=0.493+(0.0669*index), y_ratio=0.242)


def display_subinventory(self, surf):
    entities = self.handler.menu_type.menu.pointer_data

    subinv = get_alpha_surface(SUBINVENTORY_OPTION_WIDTH, len(entities) * SUBINVENTORY_OPTION_HEIGHT)
    display_entity_list(entities, subinv)
    display_subinv_pointer(self, subinv)
    surf.blit(subinv, (340, 170))


def display_entity_list(entities, subinv):
    y = 0
    for entity in entities:
        sprite = entity.images.sprite
        text = get_text_surface(entity.name, fontsize=24, color=WHITE)
        item = get_alpha_surface(SUBINVENTORY_OPTION_WIDTH, SUBINVENTORY_OPTION_HEIGHT)
        align_and_blit(item, sprite, x_ratio=0.15)
        item.blit(text, (int(item.get_width() * 0.35), int(0.5 * (item.get_height() - text.get_height()))))
        draw.line(item, DARK_GREY, (0, SUBINVENTORY_OPTION_HEIGHT - 1),
                  (int(SUBINVENTORY_OPTION_WIDTH), SUBINVENTORY_OPTION_HEIGHT - 1))
        subinv.blit(item, (0, y * SUBINVENTORY_OPTION_HEIGHT))
        y += 1


def display_subinv_pointer(self, subinv):
    if self.handler.menu_type.state is MenuSubStates.BASE:
        pass
    elif self.handler.menu_type.state in (MenuSubStates.SUBMENU, MenuSubStates.SELECTED_OPTIONS):
        subinv.blit(POINTER_RIGHT, (0, 2 + (SUBINVENTORY_OPTION_HEIGHT * self.handler.menu_type.submenu.pointer)))


def display_entity_options(self, surf):
    menu = self.game.options.current
    window = menu.get_window_image()

    surf.blit(window, (surf.get_width()*0.55, surf.get_height()*0.3 +
                       SUBINVENTORY_OPTION_HEIGHT*self.handler.menu_type.submenu.pointer))


def display_mass_capacities(party, surf):

    total_used = party.inventory.mass
    player_capa = get_text_surface(str(round(party.p1.used_carry_capacity, 2)) + '  /  ' +
                                   str(round(party.p1.max_carry_capacity, 2)) + ' kg.', color=WHITE)
    surf.blit(player_capa, (140, 400))
    mass_capa = get_text_surface(str(round(total_used, 2)) + '  /  ' + str(round(party.inventory.max_carry_capacity, 2))
                                 + ' kg.', color=WHITE)
    surf.blit(mass_capa, (358, surf.get_height()-50))


def display_wealth(money, surf):
    gold, silver, copper = split_money(money, fontsize=16)

    w = 508
    for money in [gold, silver, copper]:
        if money is not None:
            surf.blit(money, (w-money.get_width(), surf.get_height()-52))
        w += 75
