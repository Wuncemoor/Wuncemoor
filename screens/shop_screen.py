from config.constants import WHITE
from config.image_objects import SHOP_MENU, INVENTORY_OPTIONS
from screens.gui_tools import get_surface, align_and_blit, get_text_surface, get_alpha_surface


def shop_screen(self):
    surf = get_surface(SHOP_MENU)
    if self.handler.sub is None:
        options_img = INVENTORY_OPTIONS[self.owner.options.current.choice]
        party_subinv, shop_subinv = self.handler.get_subs()
    else:
        ind = self.handler.menu.options.choice
        options_img = INVENTORY_OPTIONS[ind]
        surf.blit(INDICATOR_H, (410, 130 + (32 * self.owner.options.current.choice)))
        subinventory = self.handler.menu.get_sub()
    ps, ss = display_partysub(party_subinv), display_shopsub(shop_subinv)
    sk_name = get_text_surface(self.handler.shopkeeper.name.capitalize(), fontsize=18)
    sk_gold = get_text_surface(str(self.handler.shopkeeper.shopkeeper.inventory.gold), color=WHITE)
    party_gold = get_text_surface(str(self.owner.party.inventory.gold), color=WHITE)
    td_text = get_text_surface('Transaction Details', fontsize=14, color=WHITE)
    align_and_blit(surf, options_img, x_ratio=0.17, y_ratio=0.16)
    align_and_blit(surf, options_img, x_ratio=0.5, y_ratio=0.16)
    align_and_blit(surf, options_img, x_ratio=0.83, y_ratio=0.16)
    align_and_blit(surf, sk_name, x_ratio=0.1, y_ratio=0.05, x_adjust=6, y_adjust=2)
    align_and_blit(surf, td_text, x_ratio=0.5, y_ratio=0.11)
    align_and_blit(surf, sk_gold, x_ratio=0.06, y_ratio=0.11)
    align_and_blit(surf, party_gold, x_ratio=0.72, y_ratio=0.11)
    align_and_blit(surf, ps, x_ratio=0.83, y_ratio=0.27)
    align_and_blit(surf, ss, x_ratio=0.17, y_ratio=0.27)
    align_and_blit(self.screen, surf)


def display_partysub(subinventory):
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


def display_shopsub(subinventory):
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
