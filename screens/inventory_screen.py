from config.image_objects import INVENTORY_BG, INVENTORY_OPTIONS, EQUIPMENT_BG, INDICATOR_H
from screens.display_money import display_money
from screens.gui_tools import get_surface, align_and_blit, get_alpha_surface, get_text_surface


def inventory_screen(self):

    surf = get_surface(INVENTORY_BG)
    if self.handler.menu.sub is None:
        options = INVENTORY_OPTIONS[self.owner.options.current.choice]
        subinventory = self.handler.menu.get_sub()
    else:
        ind = self.handler.menu.options.choice
        options = INVENTORY_OPTIONS[ind]
        surf.blit(INDICATOR_H, (410, 130 + (32 * self.owner.options.current.choice)))
        subinventory = self.handler.menu.get_sub()
    sg = display_subinventory(subinventory)
    party_money = display_money(self.owner.party.inventory.money)

    align_and_blit(surf, party_money, x_ratio=0.6, y_ratio=0.19)
    align_and_blit(surf, options, x_ratio=0.75, y_ratio=0.19)
    align_and_blit(surf, EQUIPMENT_BG, x_ratio=0.1, y_ratio=0.58)
    surf.blit(sg, (470, 135))

    align_and_blit(self.screen, surf)

    return surf


def display_subinventory(subinventory):
    option_height = 32

    surf = get_alpha_surface(200, len(subinventory) * option_height)
    y = 0
    for entity in subinventory:
        mini = entity.images.port_mini
        text = get_text_surface(entity.name, fontsize=16)
        value = display_money(entity.item.value)
        window = get_alpha_surface(200, option_height)
        window.blit(mini, (0, 0))
        window.blit(text, (35, 12))
        window.blit(value, (200-value.get_width(), 12))
        surf.blit(window, (0, y * option_height))
        y += 1
    return surf

