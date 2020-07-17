from handlers.views.messages import Message
from enums.game_states import GameStates
from enums.render_order import RenderOrder
from config.image_objects import CORPSE
from config.constants import RED, DARK_RED


def kill_player(player):
    make_corpse(player)

    return Message('You died!', RED), GameStates.PLAYER_DEAD


def kill_monster(mob):


    make_corpse(mob)
    mob.blocks = False
    mob.combatant = None
    mob.ai = None
    mob.render_order = RenderOrder.CORPSE



def make_corpse(entity):
    entity.images.sprite = CORPSE
