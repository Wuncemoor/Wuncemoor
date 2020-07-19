from enums.game_states import GameStates
from handlers.views.messages import Message
from loader_functions.data_loaders import save_game
from config.constants import START
from handlers.game_handler import GameHandler
from handlers.artist_handler import ArtistHandler
import pygame as py


# Main menu
def main():

    (screen_size, caption) = START
    py.init()
    py.display.set_caption(caption)
    screen = py.display.set_mode(screen_size)

    artist = ArtistHandler(screen)
    game = GameHandler(artist)
    game.state_handler = game.title
    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                game.quit()
            if event.type == py.KEYDOWN:

                output = game.input.transduce(event.key)
                game.logic.translate(output)

        game.artist.render()
        py.display.flip()


# code that still needs to be converted to new MVC system

def play_game(player, message_log, party, game):

    targeting_item = None

    while True:
        for event in py.event.get():
            player_turn_results = []
            encounter_results = []
            loot_results = []
            if event.type == py.QUIT:
                game.quit()
            if event.type == py.KEYDOWN:

                action = game.input.output(event.key)


                exit = action.get('exit')

                if exit:


                    if game.state == GameStates.TARGETING:
                        player_turn_results.append({'targeting_cancelled': True})
                    else:
                        save_game(player, game.dungeons, entities, game.world, message_log, game.state_handler)
                        game.quit()

                for player_turn_result in player_turn_results:

                    equip = player_turn_result.get('equip')
                    targeting = player_turn_result.get('targeting')
                    targeting_cancelled = player_turn_result.get('targeting_cancelled')
                    xp = player_turn_result.get('xp')

                    if equip:
                        equip_results = player.combatant.equipment.toggle_equip(equip)

                        for equip_result in equip_results:
                            equipped = equip_result.get('equipped')
                            dequipped = equip_result.get('dequipped')

                            if equipped:
                                message_log.add_message(Message('You equip the {0}!'.format(equipped.name)))
                            if dequipped:
                                message_log.add_message(Message('You dequipped the {0}!'.format(dequipped.name)))

                    if targeting:
                        game.state = GameStates.TARGETING

                        targeting_item = targeting

                        message_log.add_message(targeting_item.item.useable.targeting_message)

                    if targeting_cancelled:

                        message_log.add_message(Message('Targeting cancelled.'))


                for loot_result in loot_results:

                    take_all = loot_result.get('AUTO')
                    take_some = loot_result.get('MANUAL')
                    leave = loot_result.get('LEAVE')
                    toggle = loot_result.get('toggle')
                    loot = game.reward.loot


                    if leave:
                        player.combatant.level.add_xp(loot.xp)
                        party.inventory.take_loot(loot.claimed)
                        game.reward.current_option = 0

                        game.state_handler = game.life





if __name__ == '__main__':
    main()
