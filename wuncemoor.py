import tcod as libtcod
from fov_function import initialize_fov, recompute_fov
from death_functions import kill_monster, kill_player
from enums.game_states import GameStates, EncounterStates, LootStates, MenuStates
from game_messages import Message
from handlers.input_handlers import handle_keys, handle_mouse, handle_main_menu
from loader_functions.initialize_new_game import get_game_variables
from loader_functions.data_loaders import load_game, save_game
from config.constants import START, BLACK
from handlers.state_handlers import MenuHandler, DialogueHandler, TimeHandler, EncounterHandler
from handlers.game_handler import GameHandler
from handlers.view_handler import ViewHandler
from render_functions import render_all
import sys
import pygame as py


# Main menu
def main():

    (screen_size, cscreen_size, mscreen_size, game_title) = START

    py.init()

    screen = py.display.set_mode(screen_size)
    view = ViewHandler(screen)
    message_surface = py.Surface(mscreen_size)
    camera_surface = py.Surface(cscreen_size)

    py.display.set_caption(game_title)

    player = None
    dungeons = {}
    entities = []
    game_map = None
    message_log = None

    show_main_menu = True

    running = True

    while running:
        view.title_screen()
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:

                if show_main_menu:

                    action = handle_main_menu(event.key)
                    traverse_menu = action.get('traverse_menu')
                    choose_option = action.get('choose_menu_option')

                    if traverse_menu:
                        if (traverse_menu < 0 and view.option == 0) or \
                                (traverse_menu > 0 and view.option == 2):
                            pass
                        else:
                            view.option += traverse_menu
                    elif choose_option:
                        if view.option == 0:
                            player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera, \
                            message_log, party, journal = get_game_variables()
                            camera.refocus(player.x, player.y, game_map)

                            show_main_menu = False
                        elif view.option == 1:
                            player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera, \
                            message_log, party, journal = load_game()
                            show_main_menu = False
                        elif view.option == 2:
                            py.quit()
                            sys.exit()
                else:
                    view.screen.fill(BLACK)
                    show_main_menu = False
                    game = GameHandler()
                    play_game(player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera,
                              message_log, party, journal, game, view, camera_surface, message_surface)
        py.display.flip()


def play_game(player, dungeons, entities, structures, transitions, noncombatants, game_map, world_map, camera,
              message_log, party, journal, game, view, camera_surface, message_surface):

    fov_recompute = True
    fov_map = initialize_fov(game_map)
    targeting_item = None
    dialogue_handler = DialogueHandler([journal])
    encounter_handler = EncounterHandler()
    encounter = None
    loot = None
    menu_handler = MenuHandler()
    time_handler = TimeHandler([party])

    while True:
        for event in py.event.get():
            player_turn_results = []
            encounter_results = []
            loot_results = []
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.KEYDOWN:

                action = handle_keys(event.key, game.state)

                move = action.get('move')
                interact = action.get('interact')
                show_inventory = action.get('show_inventory')
                show_map = action.get('show_map')
                inventory_index = action.get('inventory_index')
                show_menus = action.get('show_menus')
                exit = action.get('exit')
                level_up = action.get('level_up')
                converse = action.get('converse')
                traverse_menu = action.get('traverse_menu')
                choose_menu_option = action.get('choose_menu_option')
                toggle = action.get('toggle')

                if move and game.state == GameStates.PLAYERS_TURN:
                    dx, dy = move
                    destination_x = player.x + dx
                    destination_y = player.y + dy

                    if not game_map.is_blocked(destination_x, destination_y):

                        player.move(dx, dy)
                        camera.refocus(player.x, player.y, game_map)

                        fov_recompute = True

                        if game_map.dangerous:
                            time_handler.time_goes_on()
                            encountering = encounter_handler.encounter_check()
                            if encountering:
                                tile = game_map.tiles[destination_x][destination_y]

                                options = ['FIGHT', 'ITEM', 'RUN']
                                encounter = game_map.current_map.get_encounter(tile, options)
                                encounter_handler.steps_since = 0

                                game.state = GameStates.ENCOUNTER
                            else:
                                encounter_handler.steps_since += 1

                if interact and game.state == GameStates.PLAYERS_TURN:
                    nothing = True
                    for entity in entities:
                        if entity.x == player.x and entity.y == player.y:
                            if entity.item:
                                game_map.current_map.map_entities.remove(entity)
                                pickup_results = party.inventory.add_item(entity)
                                player_turn_results.extend(pickup_results)
                                nothing = False
                                break
                    for transition in transitions:
                        if transition.x == player.x and transition.y == player.y:
                            new_dungeon = dungeons[transition.transition.go_to_dungeon]
                            if game_map.current_dungeon.name != transition.transition.go_to_dungeon:
                                game_map.current_dungeon.time_dilation = time_handler.time_stamp()
                                time_handler.apply_time_dilation(new_dungeon)
                                game_map.current_dungeon = new_dungeon

                            new_map = new_dungeon.maps[transition.transition.go_to_floor]
                            game_map.current_map = new_map
                            player.x, player.y = transition.transition.go_to_xy[0], transition.transition.go_to_xy[1]
                            camera.refocus(player.x, player.y, game_map)
                            entities = [player]
                            entities.extend(game_map.current_map.map_entities)
                            transitions = []
                            transitions.extend(game_map.current_map.transitions)
                            structures = []
                            structures.extend(game_map.current_map.structures)
                            noncombatants = []
                            noncombatants.extend(game_map.current_map.noncombatants)
                            fov_map = initialize_fov(game_map)
                            fov_recompute = True
                            nothing = False
                            break
                    for noncom in noncombatants:
                        if noncom.x == player.x and noncom.y == player.y:
                            dialogue_handler.partner = noncom
                            dialogue_handler.set_real_talk()
                            game.state = GameStates.DIALOGUE
                            nothing = False
                    if nothing:
                        message_log.add_message(Message('Nothing to see here, move along...', libtcod.dark_blue))

                if show_inventory:
                    game.state = GameStates.SHOW_INVENTORY

                if show_menus:
                    game.state = GameStates.MENUS
                    menus = {
                        'inventory': party.inventory,
                        'journal': journal,
                        'party': party,
                    }
                    menu_handler.handle_menu(menus.get(show_menus))

                if show_map:
                    game.state = GameStates.SHOW_MAP

                if inventory_index is not None and inventory_index < len(player.combatant.inventory.items):
                    item = player.combatant.inventory.items[inventory_index]

                    if game.state == GameStates.SHOW_INVENTORY:
                        player_turn_results.extend(
                            player.combatant.inventory.use(item, entities=entities, fov_map=fov_map))


                if level_up:

                    if level_up == 'Strength':
                        player.combatant.attributes.strength += 1
                    elif level_up == 'Instinct':
                        player.combatant.attributes.instinct += 1
                    elif level_up == 'Coordination':
                        player.combatant.attributes.coordination += 1
                    elif level_up == 'Vitality':
                        player.combatant.attributes.vitality += 1
                    elif level_up == 'Arcana':
                        player.combatant.attributes.arcana += 1
                    elif level_up == 'Improvisation':
                        player.combatant.attributes.improvisation += 1
                    elif level_up == 'Wisdom':
                        player.combatant.attributes.wisdom += 1
                    elif level_up == 'Finesse':
                        player.combatant.attributes.finesse += 1
                    elif level_up == 'Charisma':
                        player.combatant.attributes.charisma += 1
                    elif level_up == 'Devotion':
                        player.combatant.attributes.devotion += 1

                if converse:
                    key = chr(converse)
                    dialogue = dialogue_handler.partner.noncombatant.dialogue

                    if key in dialogue_handler.real_io.keys():
                        dialogue.current_convo = dialogue_handler.real_io.get(key)
                        current_node = dialogue.graph_dict.get(dialogue.current_convo)
                        current_node.visited = True
                        dialogue_handler.set_real_talk()
                        dialogue_handler.broadcast_choice(current_node.signal)

                        if dialogue.current_convo == 'exit':
                            dialogue.current_convo = 'root'
                            game.state = GameStates.PLAYERS_TURN

                if traverse_menu:
                    if game.state == GameStates.ENCOUNTER:
                        if (traverse_menu < 0 and encounter.current_option == 0) or \
                                (traverse_menu > 0 and encounter.current_option == len(encounter.options) - 1):
                            pass
                        else:
                            encounter.current_option += traverse_menu
                    elif game.state == GameStates.LOOTING:
                        if loot.state == LootStates.THINKING:
                            if (traverse_menu < 0 and loot.current_option == 0) or (
                                    traverse_menu > 0 and loot.current_option == (len(loot.options) - 1)):
                                pass
                            else:
                                loot.current_option += traverse_menu
                        elif loot.state == LootStates.SIFTING:
                            if (traverse_menu < 0 and loot.current_option == 0) or (
                                    traverse_menu > 0 and loot.current_option == (len(loot.items) - 1)):
                                pass
                            else:
                                loot.current_option += traverse_menu
                        elif loot.state == LootStates.DEPOSITING:
                            if (traverse_menu < 0 and loot.current_option == 0) or (
                                    traverse_menu > 0 and loot.current_option == (len(loot.claimed) - 1)):
                                pass
                            else:
                                loot.current_option += traverse_menu
                    elif game.state is GameStates.MENUS:
                        if menu_handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and menu_handler.display is None:
                            if (traverse_menu[0] < 0 and menu_handler.current_option == 0) or (
                                    traverse_menu[0] > 0 and menu_handler.current_option == (
                                    len(menu_handler.options) - 1)):
                                pass
                            else:
                                menu_handler.current_option += traverse_menu[0]
                        elif menu_handler.state == MenuStates.JOURNAL:
                            if (traverse_menu[1] < 0 and menu_handler.current_option == 0) or (
                                    traverse_menu[1] > 0 and menu_handler.current_option == (
                                    len(journal.get_subjournal(menu_handler.display)) - 1)):
                                pass
                            else:
                                menu_handler.current_option += traverse_menu[1]
                        elif menu_handler.state == MenuStates.INVENTORY:
                            ind = menu_handler.menu.options.index(menu_handler.display)
                            sg = menu_handler.menu.subgroups[ind]
                            if (traverse_menu[1] < 0 and menu_handler.current_option == 0) or (
                                    traverse_menu[1] > 0 and menu_handler.current_option == (
                                    len(sg) - 1)):
                                pass
                            else:
                                menu_handler.current_option += traverse_menu[1]

                if toggle:
                    if game.state == GameStates.LOOTING:
                        if loot.state == LootStates.SIFTING and toggle == 'right' and len(loot.claimed) > 0:
                            loot_results.append({'toggle': 'right'})
                        elif loot.state == LootStates.DEPOSITING and toggle == 'left' and len(loot.items) > 0:
                            loot_results.append({'toggle': 'left'})

                if choose_menu_option:
                    if game.state == GameStates.ENCOUNTER:
                        if encounter.state == EncounterStates.THINKING:
                            encounter_results.append({encounter.options[encounter.current_option]: True})
                        elif encounter.state == EncounterStates.FIGHT_TARGETING:
                            attack_results = player.combatant.attack(encounter.event)
                            encounter_results.extend(attack_results)
                        elif encounter.state == EncounterStates.VICTORY:
                            loot = encounter.loot

                            encounter = None
                            game.state = GameStates.LOOTING
                    elif game.state == GameStates.LOOTING:
                        if loot.state == LootStates.THINKING:
                            loot_results.append({loot.options[loot.current_option]: True})
                        elif loot.state == LootStates.SIFTING:
                            loot.claimed.append(loot.items[loot.current_option])
                            del loot.items[loot.current_option]
                            if len(loot.items) == 0:
                                loot.current_option = 2
                                loot.state = LootStates.THINKING
                            elif loot.current_option > len(loot.items) - 1:
                                loot.current_option -= 1
                        elif loot.state == LootStates.DEPOSITING:
                            loot.items.append(loot.claimed[loot.current_option])
                            del loot.claimed[loot.current_option]
                            if len(loot.claimed) == 0:
                                loot.current_option = 0
                                loot.state = LootStates.SIFTING
                            elif loot.current_option > len(loot.claimed) - 1:
                                loot.current_option -= 1
                    elif game.state == GameStates.MENUS:
                        if menu_handler.state is MenuStates.JOURNAL:
                            if len(journal.get_subjournal(menu_handler.options[menu_handler.current_option])) > 0:
                                menu_handler.display = menu_handler.options[menu_handler.current_option]
                                menu_handler.current_option = 0
                        elif menu_handler.state is MenuStates.INVENTORY and menu_handler.display is None:
                            subgroup = menu_handler.menu.subgroups[menu_handler.current_option]
                            if len(subgroup) > 0:
                                menu_handler.display = menu_handler.options[menu_handler.current_option]
                                menu_handler.current_option = 0
                        elif menu_handler.state is MenuStates.INVENTORY:
                            ind = menu_handler.menu.options.index(menu_handler.display)


                if exit:
                    if game.state == GameStates.ENCOUNTER:
                        if encounter.state == EncounterStates.FIGHT_TARGETING:
                            encounter.state = EncounterStates.THINKING
                    elif game.state == GameStates.LOOTING:
                        if loot.state in (LootStates.SIFTING, LootStates.DEPOSITING):
                            loot.state = LootStates.THINKING
                        elif loot.state == LootStates.THINKING and loot.current_option == 2:
                            loot_results.append({'LEAVE': True})
                        elif loot.state == LootStates.THINKING:
                            loot.current_option = 2
                    elif game.state == GameStates.MENUS:
                        if menu_handler.state is MenuStates.PARTY:
                            game.state = GameStates.PLAYERS_TURN
                        elif menu_handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY) and menu_handler.display is None:
                            game.state = GameStates.PLAYERS_TURN
                        elif menu_handler.state in (MenuStates.JOURNAL, MenuStates.INVENTORY):
                            if menu_handler.state == MenuStates.INVENTORY:
                                menu_handler.current_option = menu_handler.menu.options.index(menu_handler.display)
                            menu_handler.display = None

                    elif game.state in (GameStates.SHOW_INVENTORY, GameStates.SHOW_MAP):
                        game.state = GameStates.PLAYERS_TURN

                    elif game.state == GameStates.TARGETING:
                        player_turn_results.append({'targeting_cancelled': True})
                    else:
                        save_game(player, dungeons, entities, game_map, message_log, game.state)

                        py.quit()
                        sys.exit()

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
                        entities.remove(item_added)

                    if item_dropped:
                        game_map.current_map.map_entities.append(item_dropped)
                        entities = [player]
                        entities.extend(game_map.current_map.map_entities)

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

                        if leveled_up:
                            message_log.add_message(Message(
                                'Your skills grow once more! Level {0}!'.format(
                                    player.combatant.level.current_level) + '!',
                                libtcod.dark_orange))
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
                        encounter.state = EncounterStates.FIGHT_TARGETING
                    elif run:
                        game.state = GameStates.PLAYERS_TURN
                        player.combatant.level.add_xp(encounter.loot.xp)
                        if xp is None:
                            xp_text = Message("You didn't learn much there...", libtcod.dark_orange)
                        else:
                            xp_text = Message('You gain {0} experience points!'.format(xp), libtcod.dark_orange)
                        message_log.add_message(xp_text)
                        encounter = None
                    elif message:
                        message_log.add_message(message)
                    elif xp:
                        encounter.loot.xp += xp
                    elif dead_entity:
                        if dead_entity == player:
                            message, game.state = kill_player(dead_entity)
                        else:
                            encounter.loot.add_loot(dead_entity)
                            message = kill_monster(dead_entity)
                            message_log.add_message(message)
                    elif end_turn:
                        if encounter.event.combatant:
                            encounter.state = EncounterStates.ENEMY_TURN
                        else:
                            message_log.add_message(Message('YOU WIN THE FIGHT!', libtcod.black))
                            message_log.add_message(Message('Press [Enter] to loot.', libtcod.black))
                            encounter.state = EncounterStates.VICTORY

                for loot_result in loot_results:

                    take_all = loot_result.get('AUTO')
                    take_some = loot_result.get('MANUAL')
                    leave = loot_result.get('LEAVE')
                    toggle = loot_result.get('toggle')

                    if take_all:
                        loot.claimed.extend(loot.items)
                        loot.items = []
                        loot.current_option = 2
                    if take_some and (len(loot.items) + len(loot.claimed)) > 0:
                        loot.current_option = 0

                        if len(loot.items) > 0:
                            loot.state = LootStates.SIFTING
                        else:
                            loot.state = LootStates.DEPOSITING
                    if leave:
                        player.combatant.level.add_xp(loot.xp)
                        party.inventory.take_loot(loot.claimed)

                        loot = None
                        game.state = GameStates.PLAYERS_TURN
                    if toggle == 'right':
                        loot.state = LootStates.DEPOSITING
                    elif toggle == 'left':
                        loot.state = LootStates.SIFTING

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

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y)

        render_all(view.screen, camera_surface, message_surface, entities, player, structures, transitions,
                   noncombatants, game_map, world_map, camera, fov_map, fov_recompute, message_log,
                        game.state, menu_handler, time_handler, encounter, loot, dialogue_handler)

        fov_recompute = False

        py.display.flip()

        if encounter:
            if encounter.state == EncounterStates.ENEMY_TURN:
                if encounter.event.combatant:
                    enemy_turn_results = encounter.event.combatant.ai.take_turn_e(player)
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
                    encounter.state = EncounterStates.THINKING


if __name__ == '__main__':
    main()
