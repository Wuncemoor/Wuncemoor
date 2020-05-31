import tcod as libtcod


from game_messages import Message
from enums.game_states import GameStates
from render_functions import RenderOrder


def kill_player(player, corpse):
    make_corpse(player, corpse)

    return Message('You died!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster, corpse):
    death_message = Message('{0} is dead!'.format(monster.name.capitalize()), libtcod.orange)

    make_corpse(monster, corpse)
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.combatant = None
    monster.ai = None
    monster.name = 'The remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message


def make_corpse(entity, corpse):

    entity.image = corpse
