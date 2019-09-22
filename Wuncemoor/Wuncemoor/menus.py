import tcod as libtcod


def menu(con, header, options, width, screen_width, screen_height):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')
    
    #calculate total height for the header (after auto-wrap)
    header_height = libtcod.console_get_height_rect(con, 0, 0, width, screen_height, header)
    height = len(options) + header_height
    
    #create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)
    
    #print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header)
    
    #print all the options
    y = header_height
    letter_index = ord('a')
    for option_text in options:
        text = '(' + chr(letter_index) + ') ' + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1
        
    #blit the contents of "window" to the root console
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
    
def inventory_menu(con, header, player, inventory_width, screen_width, screen_height):
    #show a menu with each item of the inventory as an option
    if len(player.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []
        
        for item in player.inventory.items:
            if player.equipment.main_hand == item:
                options.append('{0} (Main Hand)'.format(item.name))
            elif player.equipment.off_hand == item:
                options.append('{0} (Off Hand)'.format(item.name))
            elif player.equipment.head == item:
                options.append('{0} (Head)'.format(item.name))
            elif player.equipment.body == item:
                options.append('{0} (Body)'.format(item.name))
            elif player.equipment.feet == item:
                options.append('{0} (Feet)'.format(item.name))
            elif player.equipment.belt == item:
                options.append('{0} (Belt)'.format(item.name))
            elif player.equipment.hands == item:
                options.append('{0} (Hands)'.format(item.name))
            elif player.equipment.finger == item:
                options.append('{0} (Finger)'.format(item.name))
            elif player.equipment.neck == item:
                options.append('{0} (Neck)'.format(item.name))
            elif player.equipment.back == item:
                options.append('{0} (Back)'.format(item.name))
            elif player.equipment.accessory == item:
                options.append('{0} (Accessory)'.format(item.name))
            else:
                options.append(item.name)
        
    menu(con, header, options, inventory_width, screen_width, screen_height)

def main_menu(con, background_image, screen_width, screen_height):
    libtcod.image_blit_2x(background_image, 0, 0, 0)
    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height/ 2 )- 4, libtcod.BKGND_NONE, libtcod.CENTER, 'WUNCEMOOR: THE ETERNAL DREAM' )
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER, 'A ZenSymphony Production')
    
    menu(con, '', ['Start A New Game', 'Continue Previous Game', 'Quit'], 24, screen_width, screen_height) 

def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
    options = ['+1 Strength (Currently {0})'.format(player.combatant.strength), '+1 Instinct (Currently {0})'.format(player.combatant.instinct), '+1 Coordination (Currently {0})'.format(player.combatant.coordination), '+1 Endurance (Currently {0})'.format(player.combatant.endurance), '+1 Arcana (Currently {0})'.format(player.combatant.arcana), '+1 Improvisation (Currently {0})'.format(player.combatant.improvisation), '+1 Wisdom (Currently {0})'.format(player.combatant.wisdom), '+1 Finesse (Currently {0})'.format(player.combatant.finesse), '+1 Charisma (Currently {0})'.format(player.combatant.charisma), '+1 Devotion (Currently {0})'.format(player.combatant.devotion)]
    menu(con, header, options, menu_width, screen_width, screen_height)
    
def feats_screen(player, character_screen_width, character_screen_height, screen_width, screen_height):
    window = libtcod.console_new(character_screen_width, character_screen_height)
    options = ['Mighty Strength']
    
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 0.7)

def character_screen(player, character_screen_width, character_screen_height, screen_width, screen_height):  
    window = libtcod.console_new(character_screen_width, character_screen_height)
    
    
    libtcod.console_set_default_foreground(window, libtcod.white)
    
    libtcod.console_print_rect_ex(window, 0, 1, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Character Information')
    libtcod.console_print_rect_ex(window, 0, 2, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Level: {0}'.format(player.level.current_level))
    libtcod.console_print_rect_ex(window, 0, 3, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Experience: {0}'.format(player.level.current_xp))
    libtcod.console_print_rect_ex(window, 0, 4, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Experience till next levelup: {0}'.format(player.level.experience_to_next_level))
    libtcod.console_print_rect_ex(window, 0, 6, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Strength: {0}'.format(player.combatant.strength)) 
    libtcod.console_print_rect_ex(window, 0, 7, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Instinct: {0}'.format(player.combatant.instinct))
    libtcod.console_print_rect_ex(window, 0, 8, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Coordination: {0}'.format(player.combatant.coordination))
    libtcod.console_print_rect_ex(window, 0, 9, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Endurance: {0}'.format(player.combatant.endurance))
    libtcod.console_print_rect_ex(window, 0, 10, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Arcana: {0}'.format(player.combatant.arcana))
    libtcod.console_print_rect_ex(window, 0, 11, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Improvisation: {0}'.format(player.combatant.improvisation))
    libtcod.console_print_rect_ex(window, 0, 12, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Wisdom: {0}'.format(player.combatant.wisdom))
    libtcod.console_print_rect_ex(window, 0, 13, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Finesse: {0}'.format(player.combatant.finesse))
    libtcod.console_print_rect_ex(window, 0, 14, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Charisma: {0}'.format(player.combatant.charisma))
    libtcod.console_print_rect_ex(window, 0, 15, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Devotion: {0}'.format(player.combatant.devotion))
    libtcod.console_print_rect_ex(window, 0, 17, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Attack: {0} ({1})'.format(player.combatant.power, player.combatant.base_power))
    libtcod.console_print_rect_ex(window, 0, 18, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Defence: {0} ({1})'.format(player.combatant.defence, player.combatant.base_defence))

    

    
    
    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 0.7)
def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)