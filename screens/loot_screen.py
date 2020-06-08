from game_messages import Message
from screens.message_box import get_message_box
import tcod as libtcod


def loot_screen(screen, images, player, encounter, message_log):

    screen.blit(images.get('gui').get('loot_bg'), (0, 0))

    message_box = get_message_box(images.get('gui').get('encounter_message_bg'), message_log, off_x=15, off_y=5)
    screen.blit(message_box, (940, 490))

