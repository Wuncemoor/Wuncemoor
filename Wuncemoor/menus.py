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
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height / 2 )- 4, libtcod.BKGND_NONE, libtcod.CENTER, 'WUNCEMOOR: THE ETERNAL DREAM' )
    libtcod.console_print_ex(0, int(screen_width / 2), int(screen_height - 2), libtcod.BKGND_NONE, libtcod.CENTER, 'A ZenSymphony Production')
    
    menu(con, '', ['Start A New Game', 'Continue Previous Game', 'Quit'], 24, screen_width, screen_height) 

def level_up_menu(con, header, player, menu_width, screen_width, screen_height):
    options = ['+1 Strength (Currently {0})'.format(player.combatant.attributes.strength), '+1 Instinct (Currently {0})'.format(player.combatant.attributes.instinct), '+1 Coordination (Currently {0})'.format(player.combatant.attributes.coordination), '+1 Vitality (Currently {0})'.format(player.combatant.attributes.vitality), '+1 Arcana (Currently {0})'.format(player.combatant.attributes.arcana), '+1 Improvisation (Currently {0})'.format(player.combatant.attributes.improvisation), '+1 Wisdom (Currently {0})'.format(player.combatant.attributes.wisdom), '+1 Finesse (Currently {0})'.format(player.combatant.attributes.finesse), '+1 Charisma (Currently {0})'.format(player.combatant.attributes.charisma), '+1 Devotion (Currently {0})'.format(player.combatant.attributes.devotion)]
    menu(con, header, options, menu_width, screen_width, screen_height)
    
def feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Strength Feats', 'Instinct Feats', 'Coordination Feats', 'Vitality Feats', 'Arcana Feats', 'Improvisation Feats', 'Wisdom Feats', 'Finesse Feats', 'Charisma Feats', 'Devotion Feats']
    menu(con, header, options, menu_width, screen_width, screen_height)
    
def strength_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Strength']
    menu(con, 'Strength Feats', options, menu_width, screen_width, screen_height)
    
def instinct_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Instinct']
    menu(con, 'Instinct Feats', options, menu_width, screen_width, screen_height)

def coordinaton_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Coordination']
    menu(con, 'Coordination Feats', options, menu_width, screen_width, screen_height)

def vitality_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Vitality']
    menu(con, 'Vitality Feats', options, menu_width, screen_width, screen_height)

def arcana_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Arcana']
    menu(con, 'Arcana Feats', options, menu_width, screen_width, screen_height)

def improvisation_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Improvisation']
    menu(con, 'Improvisation Feats', options, menu_width, screen_width, screen_height)

def wisdom_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Wisdom']
    menu(con, 'Wisdom Feats', options, menu_width, screen_width, screen_height)

def finesse_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Finesse']
    menu(con, 'Finesse Feats', options, menu_width, screen_width, screen_height)
    
def charisma_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Charisma']
    menu(con, 'Charisma Feats', options, menu_width, screen_width, screen_height)

def devotion_feats_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Mighty Devotion']
    menu(con, 'Devotion Feats', options, menu_width, screen_width, screen_height)
    
   
def character_menu(con, header, menu_width, screen_width, screen_height):
    options = ['Primary Stats', 'Combat Stats', 'Non-Combat Stats', 'Feats']
    menu(con, header, options, menu_width, screen_width, screen_height)
    

def primary_stats_screen(player, character_screen_width, character_screen_height, screen_width, screen_height):  
    window = libtcod.console_new(character_screen_width, character_screen_height)
    
    
    libtcod.console_set_default_foreground(window, libtcod.white)
    
    libtcod.console_print_rect_ex(window, 0, 1, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Character Information')
    libtcod.console_print_rect_ex(window, 0, 2, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Level: {0}'.format(player.level.current_level))
    libtcod.console_print_rect_ex(window, 0, 3, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Experience: {0}'.format(player.level.current_xp))
    libtcod.console_print_rect_ex(window, 0, 4, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Experience till next levelup: {0}'.format(player.level.experience_to_next_level))
    libtcod.console_print_rect_ex(window, 0, 6, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Strength: {0}'.format(player.combatant.attributes.strength)) 
    libtcod.console_print_rect_ex(window, 0, 7, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Instinct: {0}'.format(player.combatant.attributes.instinct))
    libtcod.console_print_rect_ex(window, 0, 8, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Coordination: {0}'.format(player.combatant.attributes.coordination))
    libtcod.console_print_rect_ex(window, 0, 9, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Vitality: {0}'.format(player.combatant.attributes.vitality))
    libtcod.console_print_rect_ex(window, 0, 10, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Arcana: {0}'.format(player.combatant.attributes.arcana))
    libtcod.console_print_rect_ex(window, 0, 11, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Improvisation: {0}'.format(player.combatant.attributes.improvisation))
    libtcod.console_print_rect_ex(window, 0, 12, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Wisdom: {0}'.format(player.combatant.attributes.wisdom))
    libtcod.console_print_rect_ex(window, 0, 13, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Finesse: {0}'.format(player.combatant.attributes.finesse))
    libtcod.console_print_rect_ex(window, 0, 14, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Charisma: {0}'.format(player.combatant.attributes.charisma))
    libtcod.console_print_rect_ex(window, 0, 15, character_screen_width, character_screen_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Devotion: {0}'.format(player.combatant.attributes.devotion))

    

    
    
    x = screen_width // 2 - character_screen_width // 2
    y = screen_height // 2 - character_screen_height // 2
    libtcod.console_blit(window, 0, 0, character_screen_width, character_screen_height, 0, x, y, 1.0, 0.7)
    
def combat_stats_screen(player, css_width, css_height, screen_width, screen_height):
    window = libtcod.console_new(css_width, css_height)
    
    libtcod.console_set_default_foreground(window, libtcod.white)
    
    libtcod.console_print_rect_ex(window, 10, 0, css_width, css_height, libtcod.BKGND_NONE, libtcod.CENTER, 'Power')
    libtcod.console_print_rect_ex(window, 30, 0, css_width, css_height, libtcod.BKGND_NONE, libtcod.CENTER, 'Resistance')


    libtcod.console_print_rect_ex(window, 0, 2, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Slash: {0} ({1})'.format(player.combatant.power_slash, player.combatant.attributes.base_power_slash))
    libtcod.console_print_rect_ex(window, 0, 3, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Pierce: {0} ({1})'.format(player.combatant.power_pierce, player.combatant.attributes.base_power_pierce))
    libtcod.console_print_rect_ex(window, 0, 4, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Blunt: {0} ({1})'.format(player.combatant.power_blunt, player.combatant.attributes.base_power_blunt))
    libtcod.console_print_rect_ex(window, 0, 5, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Heat: {0} ({1})'.format(player.combatant.spirit_heat, player.combatant.attributes.base_spirit_heat))
    libtcod.console_print_rect_ex(window, 0, 6, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Cold: {0} ({1})'.format(player.combatant.spirit_cold, player.combatant.attributes.base_spirit_cold))
    libtcod.console_print_rect_ex(window, 0, 7, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Acid: {0} ({1})'.format(player.combatant.spirit_acid, player.combatant.attributes.base_spirit_acid))
    libtcod.console_print_rect_ex(window, 0, 8, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Current: {0} ({1})'.format(player.combatant.spirit_current, player.combatant.attributes.base_spirit_current))
    libtcod.console_print_rect_ex(window, 0, 9, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Aether: {0} ({1})'.format(player.combatant.spirit_aether, player.combatant.attributes.base_spirit_aether))

    libtcod.console_print_rect_ex(window, 0, 11, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Accuracy: {0} ({1})'.format(player.combatant.accuracy, player.combatant.attributes.base_accuracy))

    libtcod.console_print_rect_ex(window, 20, 2, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Slash: {0} ({1})'.format(player.combatant.resist_slash, player.combatant.attributes.base_resist_slash))
    libtcod.console_print_rect_ex(window, 20, 3, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Pierce: {0} ({1})'.format(player.combatant.resist_pierce, player.combatant.attributes.base_resist_pierce))
    libtcod.console_print_rect_ex(window, 20, 4, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Blunt: {0} ({1})'.format(player.combatant.resist_blunt, player.combatant.attributes.base_resist_blunt))
    libtcod.console_print_rect_ex(window, 20, 5, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Heat: {0} ({1})'.format(player.combatant.resist_heat, player.combatant.attributes.base_resist_heat))
    libtcod.console_print_rect_ex(window, 20, 6, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Cold: {0} ({1})'.format(player.combatant.resist_cold, player.combatant.attributes.base_resist_cold))
    libtcod.console_print_rect_ex(window, 20, 7, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Acid: {0} ({1})'.format(player.combatant.resist_acid, player.combatant.attributes.base_resist_acid))
    libtcod.console_print_rect_ex(window, 20, 8, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Current: {0} ({1})'.format(player.combatant.resist_current, player.combatant.attributes.base_resist_current))
    libtcod.console_print_rect_ex(window, 20, 9, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Aether: {0} ({1})'.format(player.combatant.resist_aether, player.combatant.attributes.base_resist_aether))
    
    libtcod.console_print_rect_ex(window, 20, 11, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Dodge: {0} ({1})'.format(player.combatant.dodge, player.combatant.attributes.base_dodge))


    libtcod.console_print_rect_ex(window, 20, 14, css_width, css_height, libtcod.BKGND_NONE, libtcod.CENTER, 'Saving Throws')
    libtcod.console_print_rect_ex(window, 0, 16, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Athletics')
    libtcod.console_print_rect_ex(window, 20, 16, css_width, css_height, libtcod.BKGND_NONE, libtcod.CENTER, 'Fortitude')
    libtcod.console_print_rect_ex(window, 28, 16, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Resilience')
    
    libtcod.console_print_rect_ex(window, 0, 18, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Reflex: {0}'.format(player.combatant.savethrow_reflex))
    libtcod.console_print_rect_ex(window, 0, 19, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Balance: {0}'.format(player.combatant.savethrow_balance))
    libtcod.console_print_rect_ex(window, 0, 20, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Breath: {0}'.format(player.combatant.savethrow_breath))
    libtcod.console_print_rect_ex(window, 0, 21, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Grapple: {0}'.format(player.combatant.savethrow_grapple))
    libtcod.console_print_rect_ex(window, 0, 22, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Stun: {0}'.format(player.combatant.savethrow_stun))

    libtcod.console_print_rect_ex(window, 14, 18, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Panic: {0}'.format(player.combatant.savethrow_panic))
    libtcod.console_print_rect_ex(window, 14, 19, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Apathy: {0}'.format(player.combatant.savethrow_apathy))
    libtcod.console_print_rect_ex(window, 14, 20, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Pain: {0}'.format(player.combatant.savethrow_pain))
    libtcod.console_print_rect_ex(window, 14, 21, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Bewitch: {0}'.format(player.combatant.savethrow_bewitch))
    libtcod.console_print_rect_ex(window, 14, 22, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Enrage: {0}'.format(player.combatant.savethrow_enrage))

    libtcod.console_print_rect_ex(window, 28, 18, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Illness: {0}'.format(player.combatant.savethrow_illness))
    libtcod.console_print_rect_ex(window, 28, 19, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Tenacity: {0}'.format(player.combatant.savethrow_tenacity))
    libtcod.console_print_rect_ex(window, 28, 20, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Pressure: {0}'.format(player.combatant.savethrow_pressure))
    libtcod.console_print_rect_ex(window, 28, 21, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Bleed: {0}'.format(player.combatant.savethrow_bleed))
    libtcod.console_print_rect_ex(window, 28, 22, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Injury: {0}'.format(player.combatant.savethrow_injury))

    libtcod.console_print_rect_ex(window, 0, 24, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Presence: {0}'.format(player.combatant.presence))
    libtcod.console_print_rect_ex(window, 14, 24, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Initiative: {0}'.format(player.combatant.initiative))
    libtcod.console_print_rect_ex(window, 28, 24, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Speed: {0}'.format(player.combatant.speed))
    libtcod.console_print_rect_ex(window, 0, 25, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Teamwork: {0}'.format(player.combatant.teamwork))
    libtcod.console_print_rect_ex(window, 14, 25, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Leadership: {0}'.format(player.combatant.leadership))
    
    x = screen_width // 2 - css_width // 2
    y = screen_height // 2 - css_height // 2
    libtcod.console_blit(window, 0, 0, css_width, css_height, 0, x, y, 1.0, 0.7)

def noncombat_stats_screen(player, css_width, css_height, screen_width, screen_height):
    window = libtcod.console_new(css_width, css_height)
    libtcod.console_set_default_foreground(window, libtcod.white)
    
    libtcod.console_print_rect_ex(window, 14, 25, css_width, css_height, libtcod.BKGND_NONE, libtcod.LEFT, 'Leadership: {0}'.format(player.combatant.leadership))

    
    x = screen_width // 2 - css_width // 2
    y = screen_height // 2 - css_height // 2
    libtcod.console_blit(window, 0, 0, css_width, css_height, 0, x, y, 1.0, 0.7)
    
    
    
def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)