from enums.game_states import GameStates, EncounterStates, RewardStates
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
                traverse_menu = action.get('traverse_menu')
                choose_menu_option = action.get('choose_menu_option')
                toggle = action.get('toggle')

                if traverse_menu:

                    if game.state == GameStates.REWARD:

                        if game.reward.state == RewardStates.SIFTING:
                            if (traverse_menu < 0 and game.reward.current_option == 0) or (
                                    traverse_menu > 0 and game.reward.current_option == (len(game.reward.items) - 1)):
                                pass
                            else:
                                game.reward.current_option += traverse_menu
                        elif game.reward.state == RewardStates.DEPOSITING:
                            if (traverse_menu < 0 and game.reward.current_option == 0) or (
                                    traverse_menu > 0 and game.reward.current_option == (len(game.reward.loot.claimed) - 1)):
                                pass
                            else:
                                game.reward.current_option += traverse_menu

                if toggle:
                    if game.state == GameStates.REWARD:
                        if game.reward.state == RewardStates.SIFTING and toggle == 'right' and len(game.reward.claimed) > 0:
                            loot_results.append({'toggle': 'right'})
                        elif game.reward.state == RewardStates.DEPOSITING and toggle == 'left' and len(game.reward.items) > 0:
                            loot_results.append({'toggle': 'left'})

                if choose_menu_option:

                    if game.state == GameStates.REWARD:
                        if game.reward.state == RewardStates.THINKING:
                            loot_results.append({game.reward.options[game.reward.current_option]: True})
                        elif game.reward.state == RewardStates.SIFTING:
                            game.reward.loot.claimed.append(game.reward.loot.items[game.reward.current_option])
                            del game.reward.loot.items[game.reward.current_option]
                            if len(game.reward.loot.items) == 0:
                                game.reward.current_option = 2
                                game.reward.state = RewardStates.THINKING
                            elif game.reward.current_option > len(game.reward.items) - 1:
                                game.reward.current_option -= 1
                        elif game.reward.state == RewardStates.DEPOSITING:
                            game.reward.loot.items.append(game.reward.loot.claimed[game.reward.current_option])
                            del game.reward.loot.claimed[game.reward.current_option]
                            if len(game.reward.loot.claimed) == 0:
                                game.reward.current_option = 0
                                game.reward.state = RewardStates.SIFTING
                            elif game.reward.current_option > len(game.reward.loot.claimed) - 1:
                                game.reward.current_option -= 1

                if exit:
                    if game.state == GameStates.REWARD:
                        if game.reward.state in (RewardStates.SIFTING, RewardStates.DEPOSITING):
                            game.reward.state = RewardStates.THINKING
                        elif game.reward.state == RewardStates.THINKING and game.reward.current_option == 2:
                            loot_results.append({'LEAVE': True})
                        elif game.reward.state == RewardStates.THINKING:
                            game.reward.current_option = 2

                    elif game.state == GameStates.TARGETING:
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

                    if take_all:
                        loot.claimed.extend(loot.items)
                        loot.items = []
                        game.reward.current_option = 2
                    if take_some and (len(loot.items) + len(loot.claimed)) > 0:
                        game.reward.current_option = 0

                        if len(loot.items) > 0:
                            game.reward.state = RewardStates.SIFTING
                        else:
                            game.reward.state = RewardStates.DEPOSITING
                    if leave:
                        player.combatant.level.add_xp(loot.xp)
                        party.inventory.take_loot(loot.claimed)
                        game.reward.current_option = 0

                        game.state_handler = game.life
                    if toggle == 'right':
                        loot.state = RewardStates.DEPOSITING
                    elif toggle == 'left':
                        loot.state = RewardStates.SIFTING






if __name__ == '__main__':
    main()
