from config.image_objects import INVENTORY_BG, INVENTORY_OPTIONS, EQUIPMENT_BG, INDICATOR_H
from screens.gui_tools import get_surface, align_and_blit, get_alpha_surface, get_text_surface


def inventory_screen(self):

    surf = get_surface(INVENTORY_BG)
    if self.handler.display is None:
        options = INVENTORY_OPTIONS[self.owner.options.current.choice]
        subinventory = self.handler.menu.get_subinventory()
    else:
        ind = self.handler.menu.options.choice
        options = INVENTORY_OPTIONS[ind]
        surf.blit(INDICATOR_H, (410, 130 + (32 * self.owner.options.current.choice)))
        subinventory = self.handler.menu.get_subinventory()
    sg = display_subinventory(subinventory)

    align_and_blit(surf, options, x_ratio=0.75, y_ratio=0.19)
    align_and_blit(surf, EQUIPMENT_BG, x_ratio=0.1, y_ratio=0.58)
    surf.blit(sg, (470, 135))

    align_and_blit(self.screen, surf)

    return surf


def display_subinventory(subinventory):
    option_height = 32

    surf = get_alpha_surface(200, len(subinventory) * option_height)
    y = 0
    for unit in subinventory:
        mini = unit.images.port_mini
        text = get_text_surface(unit.name, fontsize=16)
        window = get_alpha_surface(200, option_height)
        window.blit(mini, (0, 0))
        window.blit(text, (35, 12))
        surf.blit(window, (0, y * option_height))
        y += 1
    return surf

