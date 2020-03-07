import tcod as libtcod
from fov_function import initialize_fov, recompute_fov
from entity import get_blocking_entities_at_location
from death_functions import kill_monster, kill_player
from game_states import GameStates
from game_messages import Message
from input_handlers import handle_keys, handle_mouse, handle_main_menu
from render_functions import clear_all, render_nearby, render_all, render_bar
from loader_functions.constants import get_constants
from loader_functions.initialize_new_game import get_game_variables
from loader_functions.data_loaders import load_game, save_game
from menus import main_menu, message_box
from PIL import Image

def play_game(player, dungeons, entities, game_map, camera, message_log, game_state, con, panel, constants):
    
    fov_recompute = True
    fov_map = initialize_fov(game_map)
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    game_state = GameStates.PLAYERS_TURN
    previous_game_state = game_state
    targeting_item = None
    
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, constants['fov_radius'], constants['fov_light_walls'], constants['fov_algorithm'])
            
        render_nearby(con, panel, entities, player, game_map, camera, fov_map, fov_recompute, message_log, constants['map_width'], constants['map_height'], constants['bar_width'], constants['panel_height'], constants['panel_y'], mouse, constants['colors'], game_state)
        
        fov_recompute = False
        
        libtcod.console_flush()
        
        clear_all(con, entities)
        
        action = handle_keys(key, game_state)
        mouse_action = handle_mouse(mouse)
        
        move = action.get('move')
        interact = action.get('interact')
        show_inventory = action.get('show_inventory')
        drop_inventory = action.get('drop_inventory')
        show_competence = action.get('show_competence')
        inventory_index = action.get('inventory_index')
        show_stats_menu = action.get('show_stats_menu')
        show_primary_stats = action.get('show_primary_stats')
        show_combat_stats = action.get('show_combat_stats')
        show_noncombat_stats = action.get('show_noncombat_stats')
        show_strength_feats = action.get('show_strength_feats')
        show_instinct_feats = action.get('show_instinct_feats')
        show_coordination_feats = action.get('show_coordination_feats')
        show_vitality_feats = action.get('show_vitality_feats')
        show_arcana_feats = action.get('show_arcana_feats')
        show_improvisation_feats = action.get('show_improvisation_feats')
        show_wisdom_feats = action.get('show_wisdom_feats')
        show_finesse_feats = action.get('show_finesse_feats')
        show_charisma_feats = action.get('show_charisma_feats')
        show_devotion_feats = action.get('show_devotion_feats')
        gain_competence = action.get('gain_competence')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        level_up = action.get('level_up')
        wait = action.get('wait')
        encounter = action.get('encounter')
        
        
        
        left_click = mouse_action.get('left_click')
        right_click = mouse_action.get('right_click')
        
        player_turn_results = []
        
        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy
            
            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)
                
                if target:
                    if target.combatant:
                        attack_results = player.combatant.attack(target)
                        player_turn_results.extend(attack_results)
                    elif target.shopkeeper:
                        talk_results = player.combatant.talk_to(target)
                        game_state = GameStates.DIALOGUE
                else:
                    player.move(dx,dy)
                    camera.refocus(player.x,player.y, game_map, constants)

                    
                    fov_recompute = True
                    
                game_state = GameStates.ENEMY_TURN
        
        if interact and game_state == GameStates.PLAYERS_TURN:
            for entity in entities:
                if entity.x == player.x and entity.y == player.y:
                    if entity.item:
                        game_map.current_map.map_entities.remove(entity)
                        pickup_results = player.combatant.inventory.add_item(entity)
                        player_turn_results.extend(pickup_results)
                        break
                    elif entity.stairs:
                        new_dungeon = dungeons[entity.stairs.go_to_dungeon]
                        new_map = new_dungeon.maps[entity.stairs.go_to_floor]
                        game_map.set_current_map(new_map)
                        player.x, player.y = entity.stairs.go_to_xy[0], entity.stairs.go_to_xy[1]
                        camera.refocus(player.x, player.y, game_map, constants)
                        entities = [player]
                        entities.extend(game_map.current_map.map_entities)
                        fov_map = initialize_fov(game_map)
                        fov_recompute = True
                        libtcod.console_clear(con)
                        
                        break
            else:
                message_log.add_message(Message('Nothing to see here, move along...', libtcod.yellow))
                

        if show_inventory:
            previous_game_state = game_state
            game_state = GameStates.SHOW_INVENTORY
            
        if drop_inventory:
            previous_game_state = game_state
            game_state = GameStates.DROP_INVENTORY
        
        if show_competence:
            previous_game_state = game_state
            game_state = GameStates.COMPETENCE_MENU
        
        if encounter:
            previous_game_state = game_state
            game_state = GameStates.ENCOUNTER
            
        if inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and inventory_index < len(player.combatant.inventory.items):
            item = player.combatant.inventory.items[inventory_index]
            
            if game_state == GameStates.SHOW_INVENTORY:
                player_turn_results.extend(player.combatant.inventory.use(item, entities=entities, fov_map=fov_map))
            elif game_state == GameStates.DROP_INVENTORY:
                player_turn_results.extend(player.combatant.inventory.drop_item(item))
                
        if gain_competence:
            attribute, competence = gain_competence
            
            player_turn_results.extend(player.competencies.comp_setter(attribute, competence))
            
        if show_stats_menu:
            previous_game_state = game_state
            game_state = GameStates.CHARACTER_MENU
        if show_primary_stats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.PRIMARY_STATS_SCREEN
        if show_combat_stats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.COMBAT_STATS_SCREEN
        if show_noncombat_stats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.NONCOMBAT_STATS_SCREEN
        if show_competence:
            previous_game_state = game_state
            game_state = GameStates.COMPETENCE_MENU
        if show_strength_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.STRENGTH_FEATS
        if show_instinct_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.INSTINCT_FEATS
        if show_coordination_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.COORDINATION_FEATS
        if show_vitality_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.VITALITY_FEATS
        if show_arcana_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.ARCANA_FEATS
        if show_improvisation_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.IMPROVISATION_FEATS
        if show_wisdom_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.WISDOM_FEATS
        if show_finesse_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.FINESSE_FEATS
        if show_charisma_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.CHARISMA_FEATS
        if show_devotion_feats:
            older_game_state = previous_game_state
            previous_game_state = game_state
            game_state = GameStates.DEVOTION_FEATS
            
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
                
            
            game_state = previous_game_state
        if game_state == GameStates.TARGETING:
            if left_click:
                target_x, target_y = left_click
                
                item_use_results = player.combatant.inventory.use(targeting_item, entities=entities, fov_map=fov_map, target_x=target_x, target_y=target_y)
                
                player_turn_results.extend(item_use_results)
            elif right_click:
                player_turn_results.append({'targeting_cancelled': True})
        
        if wait:
            game_state = GameStates.ENEMY_TURN
        if exit:
            if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY, GameStates.CHARACTER_MENU):
                game_state = previous_game_state
            elif game_state in (GameStates.PRIMARY_STATS_SCREEN, GameStates.COMBAT_STATS_SCREEN, GameStates.NONCOMBAT_STATS_SCREEN):
                game_state = previous_game_state
                previous_game_state = older_game_state
            elif game_state in (GameStates.STRENGTH_FEATS, GameStates.INSTINCT_FEATS, GameStates.COORDINATION_FEATS, GameStates.VITALITY_FEATS, GameStates.ARCANA_FEATS, GameStates.IMPROVISATION_FEATS, GameStates.WISDOM_FEATS, GameStates.FINESSE_FEATS, GameStates.CHARISMA_FEATS, GameStates.DEVOTION_FEATS):
                game_state = previous_game_state
                previous_game_state = older_game_state
                older_game_state = even_older_game_state
            elif game_state == GameStates.COMPETENCE_MENU:
                game_state = GameStates.PLAYERS_TURN
            elif game_state == GameStates.TARGETING:
                player_turn_results.append({'targeting_cancelled': True})
            else:
                save_game(player, dungeons, entities, game_map, message_log, game_state)
   
                return True
                
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
            
        for player_turn_result in player_turn_results:
            message = player_turn_result.get('message')
            dead_entity = player_turn_result.get('dead')
            item_added = player_turn_result.get('item_added')
            item_consumed = player_turn_result.get('consumed')
            item_dropped = player_turn_result.get('item_dropped')
            equip = player_turn_result.get('equip')
            targeting = player_turn_result.get('targeting')
            targeting_cancelled = player_turn_result.get('targeting_cancelled')
            xp = player_turn_result.get('xp')
            
            if message:
                message_log.add_message(message)
                
            if dead_entity:
                if dead_entity == player:
                    message, game_state = kill_player(dead_entity)
                else:
                    message = kill_monster(dead_entity)
                
                message_log.add_message(message)
                
            if item_added:
                entities.remove(item_added)
                
                game_state = GameStates.ENEMY_TURN
                
            if item_consumed:
                game_state = GameStates.ENEMY_TURN
                
            if item_dropped:
                entities.append(item_dropped)
                
                game_state = GameStates.ENEMY_TURN
            
            if equip:
                equip_results = player.combatant.equipment.toggle_equip(equip)
                
                for equip_result in equip_results:
                    equipped = equip_result.get('equipped')
                    dequipped = equip_result.get('dequipped')
                    
                    if equipped:
                        message_log.add_message(Message('You equip the {0}!'.format(equipped.name)))
                    if dequipped:
                        message_log.add_message(Message('You dequipped the {0}!'.format(dequipped.name)))
                    
                game_state = GameStates.ENEMY_TURN
                
            if targeting:
                previous_game_state = GameStates.PLAYERS_TURN
                game_state = GameStates.TARGETING
                
                targeting_item = targeting
                
                message_log.add_message(targeting_item.item.useable.targeting_message)
                
            if targeting_cancelled:
                game_state = previous_game_state
                
                message_log.add_message(Message('Targeting cancelled.'))
                
            if xp:
                leveled_up = player.combatant.level.add_xp(xp)
                message_log.add_message(Message('You gain {0} experience points!'.format(xp)))
                
                if leveled_up:
                    message_log.add_message(Message('Your skills grow once more! Level {0}!'.format(player.combatant.level.current_level) + '!', libtcod.yellow))
                    if not GameStates.TARGETING:
                        previous_game_state = game_state
                        game_state = GameStates.LEVEL_UP
                    else:
                        previous_game_state = GameStates.PLAYERS_TURN
                        game_state = GameStates.LEVEL_UP
                    
                    
        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity.combatant:
                    if entity.combatant.ai:
                        enemy_turn_results = entity.combatant.ai.take_turn(player, fov_map, game_map, entities)
                        
                        for enemy_turn_result in enemy_turn_results:
                            message = enemy_turn_result.get('message')
                            dead_entity = enemy_turn_result.get('dead')
                            
                            if message:
                                message_log.add_message(message)
                                
                            if dead_entity:
                                if dead_entity == player:
                                    message, game_state = kill_player(dead_entity)
                                else:
                                    message = kill_monster(dead_entity)
                                
                                message_log.add_message(message)
                                
                                if game_state == GameStates.PLAYER_DEAD:
                                    break
                if game_state == GameStates.PLAYER_DEAD:
                    break
            else:
                game_state = GameStates.PLAYERS_TURN
         


def main():
    constants = get_constants()
    
    libtcod.console_set_custom_font(r'C:\Users\penic\Desktop\Projects\wuncemoor_testzone\\arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    
    libtcod.console_init_root(constants['screen_width'], constants['screen_height'], constants['window_title'], False)
    
    con = libtcod.console_new(constants['map_width'],constants['map_height'])
    panel = libtcod.console_new(constants['map_width'], constants['map_height'])
    
    view_con = libtcod.console_new(constants['alpha_width'], constants['alpha_height'])
    view_panel = libtcod.console_new(constants['alpha_width'], constants['alpha_height'])
    
    player = None
    dungeons = { }
    entities = []
    game_map = None
    message_log = None
    game_state = None
    
    show_main_menu = True
    show_load_error_message = False
    
    main_menu_background_image = libtcod.image_load('the_fall_of_icarus.jpg')
    
    key = libtcod.Key()
    mouse = libtcod.Mouse()
   
    while not libtcod.console_is_window_closed():
    
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        if show_main_menu:
            main_menu(con, main_menu_background_image, constants['screen_width'], constants['screen_height'])
            
            if show_load_error_message:
                message_box(con, 'No save game to load :(', 50, constants['screen_width'], constants['screen_height'])
                
            libtcod.console_flush()
            
            action = handle_main_menu(key)
            
            new_game = action.get('new_game')
            load_saved_game = action.get('load_game')
            exit_game = action.get('exit')
            
            if show_load_error_message and (new_game or load_saved_game or exit_game):
                show_load_error_message = False
            elif new_game:
                player, dungeons, entities, game_map, camera, message_log, game_state = get_game_variables(constants)
                game_state = GameStates.PLAYERS_TURN
                
                show_main_menu = False
            elif load_saved_game:
                try:
                    player, dungeons, entities, game_map, camera, message_log, game_state = load_game()
                    show_main_menu = False
                except FileNotFoundError:
                    show_load_error_message = True
            elif exit_game:
                break
            
        else:
            libtcod.console_clear(con)
            play_game(player, dungeons, entities, game_map, camera, message_log, game_state, con, panel, constants)
            
            show_main_menu = True
      
if __name__ == '__main__':
    main()