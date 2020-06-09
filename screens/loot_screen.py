from screens.message_box import get_message_box
from screens.loot_menu import display_loot, get_loot_menu, display_resources_gain


def loot_screen(screen, images, player, loot, message_log):

    screen.blit(images.get('gui').get('loot_bg'), (0, 0))
    screen.blit(images.get('gui').get('loot_banner'), (320, 0))

    message_box = get_message_box(images.get('gui').get('encounter_message_bg'), message_log, off_x=15, off_y=5)
    screen.blit(message_box, (940, 490))
    loot_visual = display_loot(images, loot)
    screen.blit(loot_visual, (0, 300))

    resources = display_resources_gain(loot)
    screen.blit(resources, (1000, 180))

    loot_menu = get_loot_menu(images, loot)
    screen.blit(loot_menu, (0, 0))
