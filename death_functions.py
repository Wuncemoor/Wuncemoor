from game_messages import Message
from enums.game_states import GameStates
from enums.render_order import RenderOrder
from config.image_objects import CORPSE
from config.constants import RED, DARK_RED


def kill_player(player):
    make_corpse(player)

    return Message('You died!', RED), GameStates.PLAYER_DEAD


def kill_monster(monster):

    death_message = Message('{0} is dead!'.format(monster.name), DARK_RED)

    make_corpse(monster)
    monster.blocks = False
    monster.combatant = None
    monster.ai = None
    monster.render_order = RenderOrder.CORPSE

    return death_message


def make_corpse(entity):
    entity.images.sprite = CORPSE
