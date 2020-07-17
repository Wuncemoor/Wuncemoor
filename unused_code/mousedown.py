if event.type == py.MOUSEBUTTONDOWN:

    mouse_action = handle_mouse((event.pos, event.button))

    left_click = mouse_action.get('left_click')
    right_click = mouse_action.get('right_click')

    if game.state == GameStates.TARGETING:
        if left_click:
            target_x, target_y = left_click

            item_use_results = player.combatant.inventory.use(targeting_item, entities=entities,
                                                              fov_map=fov_map, target_x=target_x,
                                                              target_y=target_y)

            player_turn_results.extend(item_use_results)
        elif right_click:
            player_turn_results.append({'targeting_cancelled': True})