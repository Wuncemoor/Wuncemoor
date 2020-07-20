# code that still needs to be converted to new MVC system

def play_game(player, message_log, party, game):

    targeting_item = None

    while True:
        for event in py.event.get():
            player_turn_results = []
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