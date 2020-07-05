from screens.message_box import get_message_box
from screens.loot_menu import display_loot, get_reward_menu, display_resources_gain
from config.image_objects import LOOT_BG, LOOT_BANNER, ENCOUNTER_MESSAGE_BG


def reward_screen(screen, reward, message_log):

    screen.blit(LOOT_BG, (0, 0))
    screen.blit(LOOT_BANNER, (320, 0))

    message_box = get_message_box(ENCOUNTER_MESSAGE_BG, message_log, off_x=15, off_y=5)
    screen.blit(message_box, (940, 490))
    loot_visual = display_loot(reward)
    screen.blit(loot_visual, (0, 300))

    resources = display_resources_gain(reward.loot)
    screen.blit(resources, (1000, 180))

    loot_menu = get_reward_menu(reward)
    screen.blit(loot_menu, (0, 0))
