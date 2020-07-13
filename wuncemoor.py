import tcod as libtcod
from death_functions import kill_monster, kill_player
from enums.game_states import GameStates, EncounterStates, RewardStates, MenuStates
from handlers.views.messages import Message
from handlers.input_handler import handle_mouse
from loader_functions.data_loaders import save_game
from config.constants import START, BLACK, DARK_BLUE, DARK_ORANGE
from handlers.game_handler import GameHandler
from handlers.artist_handler import ArtistHandler
import pygame as py


# Main menu
def main():

    (screen_size, caption) = START
    py.init()
    py.display.set_caption(caption)
    screen = py.display.set_mode(screen_size)

    graphics = ArtistHandler(screen)
    game = GameHandler(graphics)
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

        # if game.encounter.state == EncounterStates.ENEMY_TURN:
        #     if game.encounter.mob.combatant:
        #         enemy_turn_results = game.encounter.mob.combatant.ai.take_turn_e(player)
        #         for enemy_turn_result in enemy_turn_results:
        #             message = enemy_turn_result.get('message')
        #             dead_entity = enemy_turn_result.get('dead')
        #
        #             if message:
        #                 message_log.add_message(message)
        #
        #             if dead_entity:
        #                 if dead_entity == player:
        #                     message, game.state = kill_player(dead_entity)
        #                 else:
        #                     message = kill_monster(dead_entity)
        #
        #                 message_log.add_message(message)
        #
        #             if game.state == GameStates.PLAYER_DEAD:
        #                 break
        #         game.encounter.state = EncounterStates.THINKING


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

                move = action.get('move')
                interact = action.get('interact')
                show_map = action.get('show_map')
                show_menus = action.get('show_menus')
                exit = action.get('exit')
                level_up = action.get('level_up')
                converse = action.get('converse')
                traverse_menu = action.get('traverse_menu')
                choose_menu_option = action.get('choose_menu_option')
                toggle = action.get('toggle')

                if move and game.state == GameStates.LIFE:
                    dx, dy = move
                    destination_x = player.x + dx
                    destination_y = player.y + dy

                    if not game.world.is_blocked(destination_x, destination_y):

                        player.move(dx, dy)
                        game.view.camera.refocus(player.x, player.y)

                        game.view.fov.needs_recompute = True

                        if game.world.dangerous:
                            game.time.goes_on()
                            encountering = game.encounter.check()
                            if encountering:
                                tile = game.world.tiles[destination_x][destination_y]
                                options = ['FIGHT', 'ITEM', 'RUN']
                                game.encounter.new(tile, options)
                                game.state_handler = game.encounter
                            else:
                                game.encounter.steps_since += 1

                if interact and game.state == GameStates.LIFE:
                    nothing = True
                    for entity in game.world.current_map.entities:
                        if entity.x == player.x and entity.y == player.y:
                            if entity.item:
                                pickup_results = party.inventory.add_item(entity)
                                player_turn_results.extend(pickup_results)
                                nothing = False
                                break
                    for transition in game.world.current_map.transitions:
                        if transition.x == player.x and transition.y == player.y:
                            new_dungeon = game.dungeons[transition.transition.go_to_dungeon]
                            if game.world.current_dungeon.name != transition.transition.go_to_dungeon:
                                game.world.current_dungeon.time_dilation = game.time.stamp()
                                game.time.apply_dilation(new_dungeon)
                                game.world.current_dungeon = new_dungeon

                            new_map = new_dungeon.maps[transition.transition.go_to_floor]
                            game.world.current_map = new_map
                            player.x, player.y = transition.transition.go_to_xy[0], transition.transition.go_to_xy[1]
                            game.view.camera.refocus(player.x, player.y)

                            game.view.fov.map = game.view.fov.initialize(game.world)
                            game.view.fov.needs_recompute = True
                            nothing = False
                            break
                    for noncom in game.world.current_map.noncombatants:
                        if noncom.x == player.x and noncom.y == player.y:
                            game.dialogue.partner = noncom
                            game.dialogue.set_real_talk()
                            game.state_handler = game.dialogue
                            nothing = False
                    if nothing:
                        message_log.add_message(Message('Nothing to see here, move along...', DARK_BLUE))

                if show_menus:
                    game.state_handler = game.menus
                    opts = {
                        'inventory': party.inventory,
                        'journal': party.journal,
                        'party': party,
                    }
                    game.menus.handle_menu(opts.get(show_menus))

                if show_map:
                    game.state = GameStates.SHOW_MAP

                # still reworking
                if level_up:
                    pass

                if converse:
                    key = chr(converse)
                    dialogue = game.dialogue.partner.noncombatant.dialogue

                    if key in game.dialogue.real_io.keys():
                        dialogue.conversation = game.dialogue.real_io.get(key)
                        current_node = dialogue.graph_dict.get(dialogue.conversation)
                        current_node.visited = True
                        game.dialogue.set_real_talk()
                        game.dialogue.broadcast_choice(current_node.signal)

                        if dialogue.conversation == 'exit':
                            dialogue.conversation = 'root'
                            game.state_handler = game.life

                if traverse_menu:
                    if game.state == GameStates.ENCOUNTER:
                        if (traverse_menu < 0 and game.encounter.current_option == 0) or \
                                (traverse_menu > 0 and game.encounter.current_option == len(game.encounter.options) - 1):
                            pass
                        else:
                            game.encounter.current_option += traverse_menu
                    elif game.state == GameStates.REWARD:
                        if game.reward.state == RewardStates.THINKING:
                            if (traverse_menu < 0 and game.reward.current_option == 0) or (
                                    traverse_menu > 0 and game.reward.current_option == (len(game.reward.options) - 1)):
                                pass
                            else:
                                game.reward.current_option += traverse_menu
                        elif game.reward.state == RewardStates.SIFTING:
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
                    elif game.state is GameStates.MENUS:
                        if game.menus.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and game.menus.display is None:
                            if (traverse_menu[0] < 0 and game.menus.current_option == 0) or (
                                    traverse_menu[0] > 0 and game.menus.current_option == (
                                    len(game.menus.options) - 1)):
                                pass
                            else:
                                game.menus.current_option += traverse_menu[0]
                        elif game.menus.state == MenuStates.JOURNAL:
                            if (traverse_menu[1] < 0 and game.menus.current_option == 0) or (
                                    traverse_menu[1] > 0 and game.menus.current_option == (
                                    len(party.journal.get_subjournal(game.menus.display)) - 1)):
                                pass
                            else:
                                game.menus.current_option += traverse_menu[1]
                        elif game.menus.state == MenuStates.INVENTORY:
                            ind = game.menus.menu.options.index(game.menus.display)
                            sg = game.menus.menu.subgroups[ind]
                            if (traverse_menu[1] < 0 and game.menus.current_option == 0) or (
                                    traverse_menu[1] > 0 and game.menus.current_option == (
                                    len(sg) - 1)):
                                pass
                            else:
                                game.menus.current_option += traverse_menu[1]

                if toggle:
                    if game.state == GameStates.REWARD:
                        if game.reward.state == RewardStates.SIFTING and toggle == 'right' and len(game.reward.claimed) > 0:
                            loot_results.append({'toggle': 'right'})
                        elif game.reward.state == RewardStates.DEPOSITING and toggle == 'left' and len(game.reward.items) > 0:
                            loot_results.append({'toggle': 'left'})

                if choose_menu_option:
                    if game.state == GameStates.ENCOUNTER:
                        if game.encounter.state == EncounterStates.THINKING:
                            encounter_results.append({game.encounter.options[game.encounter.current_option]: True})
                        elif game.encounter.state == EncounterStates.FIGHT_TARGETING:
                            attack_results = player.combatant.attack(game.encounter.mob)
                            encounter_results.extend(attack_results)
                        elif game.encounter.state == EncounterStates.VICTORY:
                            game.state_handler = game.reward
                            game.reward.state = RewardStates.THINKING
                    elif game.state == GameStates.REWARD:
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
                    elif game.state == GameStates.MENUS:
                        if game.menus.state is MenuStates.JOURNAL:
                            if len(party.journal.get_subjournal(game.menus.options[game.menus.current_option])) > 0:
                                game.menus.display = game.menus.options[game.menus.current_option]
                                game.menus.current_option = 0
                        elif game.menus.state is MenuStates.INVENTORY and game.menus.display is None:
                            subgroup = game.menus.menu.subgroups[game.menus.current_option]
                            if len(subgroup) > 0:
                                game.menus.display = game.menus.options[game.menus.current_option]
                                game.menus.current_option = 0
                        elif game.menus.state is MenuStates.INVENTORY:
                            ind = game.menus.menu.options.index(game.menus.display)

                if exit:
                    if game.state == GameStates.ENCOUNTER:
                        if game.encounter.state == EncounterStates.FIGHT_TARGETING:
                            game.encounter.state = EncounterStates.THINKING
                    elif game.state == GameStates.REWARD:
                        if game.reward.state in (RewardStates.SIFTING, RewardStates.DEPOSITING):
                            game.reward.state = RewardStates.THINKING
                        elif game.reward.state == RewardStates.THINKING and game.reward.current_option == 2:
                            loot_results.append({'LEAVE': True})
                        elif game.reward.state == RewardStates.THINKING:
                            game.reward.current_option = 2
                    elif game.state == GameStates.MENUS:
                        if game.menus.state is MenuStates.PARTY:
                            game.state_handler = game.life
                        elif game.menus.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and game.menus.display is None:
                            game.state_handler = game.life
                        elif game.menus.state in (MenuStates.JOURNAL, MenuStates.INVENTORY):
                            if game.menus.state == MenuStates.INVENTORY:
                                game.menus.current_option = game.menus.menu.options.index(game.menus.display)
                            game.menus.display = None

                    elif game.state in (GameStates.SHOW_INVENTORY, GameStates.SHOW_MAP):
                        game.state_handler = game.life

                    elif game.state == GameStates.TARGETING:
                        player_turn_results.append({'targeting_cancelled': True})
                    else:
                        save_game(player, game.dungeons, entities, game.world, message_log, game.state_handler)
                        game.quit()

                for player_turn_result in player_turn_results:
                    message = player_turn_result.get('message')
                    dead_entity = player_turn_result.get('dead')
                    item_added = player_turn_result.get('item_added')
                    item_dropped = player_turn_result.get('item_dropped')
                    equip = player_turn_result.get('equip')
                    targeting = player_turn_result.get('targeting')
                    targeting_cancelled = player_turn_result.get('targeting_cancelled')
                    xp = player_turn_result.get('xp')

                    if message:
                        message_log.add_message(message)

                    if dead_entity:
                        if dead_entity == player:
                            message, game.state = kill_player(dead_entity)
                        else:
                            message = kill_monster(dead_entity)

                        message_log.add_message(message)

                    if item_added:
                        game.world.current_map.entities.remove(item_added)

                    if item_dropped:
                        game.world.current_map.entities.append(item_dropped)

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

                    if xp:
                        leveled_up = player.combatant.level.add_xp(xp)
                        message_log.add_message(
                            Message('You gain {0} experience points!'.format(xp), libtcod.dark_orange))

                        # still reworking
                        if leveled_up:
                            pass
                            if not GameStates.TARGETING:
                                game.state = GameStates.LEVEL_UP
                            else:
                                game.state = GameStates.LEVEL_UP
                for encounter_result in encounter_results:

                    fight = encounter_result.get('FIGHT')

                    run = encounter_result.get('RUN')
                    end_turn = encounter_result.get('end_turn')

                    xp = encounter_result.get('xp')
                    message = encounter_result.get('message')
                    dead_entity = encounter_result.get('dead')
                    if fight:
                        game.encounter.state = EncounterStates.FIGHT_TARGETING
                    elif run:
                        game.state_handler = game.life
                        player.combatant.level.add_xp(game.reward.loot.xp)
                        if xp is None:
                            xp_text = Message("You didn't learn much there...", DARK_ORANGE)
                        else:
                            xp_text = Message('You gain {0} experience points!'.format(xp), DARK_ORANGE)
                        message_log.add_message(xp_text)
                    elif message:
                        message_log.add_message(message)
                    elif xp:
                        game.encounter.loot.xp += xp
                    elif dead_entity:
                        if dead_entity == player:
                            message, game.state = kill_player(dead_entity)
                        else:
                            game.encounter.loot.add_loot(dead_entity)
                            message = kill_monster(dead_entity)
                            message_log.add_message(message)
                    elif end_turn:
                        if game.encounter.mob.combatant:
                            game.encounter.state = EncounterStates.ENEMY_TURN
                        else:
                            message_log.add_message(Message('YOU WIN THE FIGHT!', BLACK))
                            message_log.add_message(Message('Press [Enter] to loot.', BLACK))
                            game.encounter.state = EncounterStates.VICTORY

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

        if game.view.fov.needs_recompute:
            game.view.fov.recompute(game.view.fov.map, player.x, player.y)

        game.view.render_all(player, message_log)

        game.view.fov.needs_recompute = False

        py.display.flip()

        if game.encounter.state == EncounterStates.ENEMY_TURN:
            if game.encounter.mob.combatant:
                enemy_turn_results = game.encounter.mob.combatant.ai.take_turn_e(player)
                for enemy_turn_result in enemy_turn_results:
                    message = enemy_turn_result.get('message')
                    dead_entity = enemy_turn_result.get('dead')

                    if message:
                        message_log.add_message(message)

                    if dead_entity:
                        if dead_entity == player:
                            message, game.state = kill_player(dead_entity)
                        else:
                            message = kill_monster(dead_entity)

                        message_log.add_message(message)

                    if game.state == GameStates.PLAYER_DEAD:
                        break
                game.encounter.state = EncounterStates.THINKING


if __name__ == '__main__':
    main()
