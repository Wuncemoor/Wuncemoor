import tcod as libtcod
import pygame


def menu(screen, header, fontsize, options, width, camera_width, camera_height):
    if len(options) > 26: raise ValueError('Cannot have a menu with more than 26 options.')

    # calculate total height for the header (after auto-wrap)

    height = len(options) * fontsize + fontsize * .4

    # create an off-screen console that represents the menu's window
    menu = pygame.Surface((width, height))

    # print the header, with auto-wrap

    font = pygame.font.SysFont("comicsansms", fontsize)

    # print all the options
    q = 0
    letter_index = ord('a')
    for option_text in options:
        text = font.render('(' + chr(letter_index) + ') ' + option_text, True, (255, 255, 255))
        menu.blit(text, (0, q * fontsize))
        q += 1
        letter_index += 1

    # blit the contents of "window" to the root console
    x = int((camera_width / 2) - (width / 2))
    y = int((camera_height / 2) - (height / 2))
    screen.blit(menu, (x, y))


def inventory_menu(screen, header, fontsize, player, inventory_width, camera_width, camera_height):
    # show a menu with each item of the inventory as an option
    if len(player.combatant.inventory.items) == 0:
        options = ['Inventory is empty.']
    else:
        options = []

        for item in player.combatant.inventory.items:
            if player.combatant.equipment.main_hand == item:
                options.append('{0} (Main Hand)'.format(item.name))
            elif player.combatant.equipment.off_hand == item:
                options.append('{0} (Off Hand)'.format(item.name))
            elif player.combatant.equipment.head == item:
                options.append('{0} (Head)'.format(item.name))
            elif player.combatant.equipment.body == item:
                options.append('{0} (Body)'.format(item.name))
            elif player.combatant.equipment.feet == item:
                options.append('{0} (Feet)'.format(item.name))
            elif player.combatant.equipment.belt == item:
                options.append('{0} (Belt)'.format(item.name))
            elif player.combatant.equipment.hands == item:
                options.append('{0} (Hands)'.format(item.name))
            elif player.combatant.equipment.finger == item:
                options.append('{0} (Finger)'.format(item.name))
            elif player.combatant.equipment.neck == item:
                options.append('{0} (Neck)'.format(item.name))
            elif player.combatant.equipment.back == item:
                options.append('{0} (Back)'.format(item.name))
            elif player.combatant.equipment.accessory == item:
                options.append('{0} (Accessory)'.format(item.name))
            else:
                options.append(item.name)

    menu(screen, header, fontsize, options, inventory_width, camera_width, camera_height)


def main_menu(screen, background_image, screen_width, screen_height, fontsize):
    screen.blit(background_image, (0, 0))
    font = pygame.font.SysFont("comicsansms", fontsize)
    titletext = font.render('WUNCEMOOR: THE ETERNAL DREAM', True, (255, 255, 255))
    extratext = font.render('A ZenSymphony Production', True, (255, 255, 255))
    menu_width = 650

    screen.blit(titletext, (int(screen_width / 8), int(screen_height / 10)))
    screen.blit(extratext, (int(screen_width / 8), int(3 * screen_height / 4)))
    menu(screen, '', fontsize, ['Start A New Game', 'Continue Previous Game', 'Quit'], menu_width, screen_width,
         screen_height)


def level_up_menu(screen, header, player, menu_width, camera_width, camera_height):
    options = ['+1 Strength (Currently {0})'.format(player.combatant.attributes.strength),
               '+1 Instinct (Currently {0})'.format(player.combatant.attributes.instinct),
               '+1 Coordination (Currently {0})'.format(player.combatant.attributes.coordination),
               '+1 Vitality (Currently {0})'.format(player.combatant.attributes.vitality),
               '+1 Arcana (Currently {0})'.format(player.combatant.attributes.arcana),
               '+1 Improvisation (Currently {0})'.format(player.combatant.attributes.improvisation),
               '+1 Wisdom (Currently {0})'.format(player.combatant.attributes.wisdom),
               '+1 Finesse (Currently {0})'.format(player.combatant.attributes.finesse),
               '+1 Charisma (Currently {0})'.format(player.combatant.attributes.charisma),
               '+1 Devotion (Currently {0})'.format(player.combatant.attributes.devotion)]
    fontsize = 12
    menu(screen, header, fontsize, options, menu_width, camera_width, camera_height)


def competence_menu(screen, header, cm_width, camera_width, camera_height):
    options = ['Strength', 'Instinct', 'Coordination', 'Vitality', 'Arcana', 'Improvisation', 'Wisdom', 'Finesse',
               'Charisma', 'Devotion']
    fontsize = 12
    menu(screen, header, fontsize, options, cm_width, camera_width, camera_height)


def strength_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Strength, Better Slash, Better Stab, Better Blunt']
    fontsize = 12
    menu(screen, 'Strength Feats', fontsize, options, menu_width, camera_width, camera_height)


def instinct_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Instinct']
    fontsize = 12
    menu(screen, 'Instinct Feats', fontsize, options, menu_width, camera_width, camera_height)


def coordinaton_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Coordination']
    fontsize = 12
    menu(screen, 'Coordination Feats', fontsize, options, menu_width, camera_width, camera_height)


def vitality_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Vitality']
    fontsize = 12
    menu(screen, 'Vitality Feats', fontsize, options, menu_width, camera_width, camera_height)


def arcana_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Arcana']
    fontsize = 12
    menu(screen, 'Arcana Feats', fontsize, options, menu_width, camera_width, camera_height)


def improvisation_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Improvisation']
    fontsize = 12
    menu(screen, 'Improvisation Feats', fontsize, options, menu_width, camera_width, camera_height)


def wisdom_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Wisdom']
    fontsize = 12
    menu(screen, 'Wisdom Feats', fontsize, options, menu_width, camera_width, camera_height)


def finesse_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Finesse']
    fontsize = 12
    menu(screen, 'Finesse Feats', fontsize, options, menu_width, camera_width, camera_height)


def charisma_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Charisma']
    fontsize = 12
    menu(screen, 'Charisma Feats', fontsize, options, menu_width, camera_width, camera_height)


def devotion_feats_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Mighty Devotion']
    fontsize = 12
    menu(screen, 'Devotion Feats', fontsize, options, menu_width, camera_width, camera_height)


def character_menu(screen, header, menu_width, camera_width, camera_height):
    options = ['Primary Stats', 'Combat Stats', 'Non-Combat Stats']
    fontsize = 12
    menu(screen, header, fontsize, options, menu_width, camera_width, camera_height)


def primary_stats_screen(screen, player, character_screen_width, character_screen_height, camera_width, camera_height):
    window = pygame.Surface((character_screen_width, character_screen_height))

    fontsize = 15
    font = pygame.font.SysFont("comicsansms", fontsize)

    lines = [
        'Character Information',
        'Level: {0}'.format(player.combatant.level.current_level),
        'Experience: {0}'.format(player.combatant.level.current_xp),
        'Experience till next levelup: {0}'.format(player.combatant.level.experience_to_next_level),
        'Strength: {0}'.format(player.combatant.attributes.strength),
        'Instinct: {0}'.format(player.combatant.attributes.instinct),
        'Coordination: {0}'.format(player.combatant.attributes.coordination),
        'Vitality: {0}'.format(player.combatant.attributes.vitality),
        'Arcana: {0}'.format(player.combatant.attributes.arcana),
        'Improvisation: {0}'.format(player.combatant.attributes.improvisation),
        'Wisdom: {0}'.format(player.combatant.attributes.wisdom),
        'Finesse: {0}'.format(player.combatant.attributes.finesse),
        'Charisma: {0}'.format(player.combatant.attributes.charisma),
        'Devotion: {0}'.format(player.combatant.attributes.devotion),
    ]

    libtcod.console_set_default_foreground(window, libtcod.white)
    for count, elem in enumerate(lines):
        text = font.render(elem, True, (255, 255, 255))
        window.blit(text, (0, fontsize * (count + 1)))

    x = camera_width // 2 - character_screen_width // 2
    y = camera_height // 2 - character_screen_height // 2
    screen.blit(window, (camera_width / 4, camera_height / 4))


def combat_stats_screen(screen, player, css_width, css_height, camera_width, camera_height):
    window = pygame.Surface((css_width, css_height))
    fontsize = 12
    font = pygame.font.SysFont("comicsansms", fontsize)

    power = font.render('Power', True, (255, 255, 255))
    window.blit(power, (css_width / 3, 0))
    resist = font.render('Resistance', True, (255, 255, 255))
    window.blit(resist, ((2 * css_width) / 3, 0))

    # x, y, data
    lines = [
        (0, 0, 'Power'),
        (css_width / 2, 0, 'Resistance'),
        (0, fontsize * 2,
         'Slash: {0} ({1})'.format(player.combatant.power_slash, player.combatant.attributes.base_power_slash)),
        (0, fontsize * 3,
         'Pierce: {0} ({1})'.format(player.combatant.power_pierce, player.combatant.attributes.base_power_pierce)),
        (0, fontsize * 4,
         'Blunt: {0} ({1})'.format(player.combatant.power_blunt, player.combatant.attributes.base_power_blunt)),
        (0, fontsize * 5,
         'Heat: {0} ({1})'.format(player.combatant.spirit_heat, player.combatant.attributes.base_spirit_heat)),
        (0, fontsize * 6,
         'Cold: {0} ({1})'.format(player.combatant.spirit_cold, player.combatant.attributes.base_spirit_cold)),
        (0, fontsize * 7,
         'Acid: {0} ({1})'.format(player.combatant.spirit_acid, player.combatant.attributes.base_spirit_acid)),
        (0, fontsize * 8,
         'Current: {0} ({1})'.format(player.combatant.spirit_current, player.combatant.attributes.base_spirit_current)),
        (0, fontsize * 9,
         'Aether: {0} ({1})'.format(player.combatant.spirit_aether, player.combatant.attributes.base_spirit_aether)),
        (0, fontsize * 10, 'Competence: {0}'.format(player.combatant.competence_points)),
        (0, fontsize * 11,
         'Accuracy: {0} ({1})'.format(player.combatant.accuracy, player.combatant.attributes.base_accuracy)),
        (css_width / 2, fontsize * 2,
         'Slash: {0} ({1})'.format(player.combatant.resist_slash, player.combatant.attributes.base_resist_slash)),
        (css_width / 2, fontsize * 3,
         'Pierce: {0} ({1})'.format(player.combatant.resist_pierce, player.combatant.attributes.base_resist_pierce)),
        (css_width / 2, fontsize * 4,
         'Blunt: {0} ({1})'.format(player.combatant.resist_blunt, player.combatant.attributes.base_resist_blunt)),
        (css_width / 2, fontsize * 5,
         'Heat: {0} ({1})'.format(player.combatant.resist_heat, player.combatant.attributes.base_resist_heat)),
        (css_width / 2, fontsize * 6,
         'Cold: {0} ({1})'.format(player.combatant.resist_cold, player.combatant.attributes.base_resist_cold)),
        (css_width / 2, fontsize * 7,
         'Acid: {0} ({1})'.format(player.combatant.resist_acid, player.combatant.attributes.base_resist_acid)),
        (css_width / 2, fontsize * 8,
         'Current: {0} ({1})'.format(player.combatant.resist_current, player.combatant.attributes.base_resist_current)),
        (css_width / 2, fontsize * 9,
         'Aether: {0} ({1})'.format(player.combatant.resist_aether, player.combatant.attributes.base_resist_aether)),
        (css_width / 2, fontsize * 11,
         'Dodge: {0} ({1})'.format(player.combatant.dodge, player.combatant.attributes.base_dodge)),
        (css_width / 3, fontsize * 14, 'Saving Throws'),
        (0, fontsize * 16, 'Athletics'),
        (css_width / 3, fontsize * 16, 'Fortitude'),
        (2 * css_width / 3, fontsize * 16, 'Resilience'),
        (0, fontsize * 18, 'Reflex: {0}'.format(player.combatant.savethrow_reflex)),
        (0, fontsize * 19, 'Balance: {0}'.format(player.combatant.savethrow_balance)),
        (0, fontsize * 20, 'Breath: {0}'.format(player.combatant.savethrow_breath)),
        (0, fontsize * 21, 'Grapple: {0}'.format(player.combatant.savethrow_grapple)),
        (0, fontsize * 22, 'Stun: {0}'.format(player.combatant.savethrow_stun)),
        (css_width / 3, fontsize * 18, 'Panic: {0}'.format(player.combatant.savethrow_panic)),
        (css_width / 3, fontsize * 19, 'Apathy: {0}'.format(player.combatant.savethrow_apathy)),
        (css_width / 3, fontsize * 20, 'Pain: {0}'.format(player.combatant.savethrow_pain)),
        (css_width / 3, fontsize * 21, 'Bewitch: {0}'.format(player.combatant.savethrow_bewitch)),
        (css_width / 3, fontsize * 22, 'Enrage: {0}'.format(player.combatant.savethrow_enrage)),
        (2 * css_width / 3, fontsize * 18, 'Illness: {0}'.format(player.combatant.savethrow_illness)),
        (2 * css_width / 3, fontsize * 19, 'Tenacity: {0}'.format(player.combatant.savethrow_tenacity)),
        (2 * css_width / 3, fontsize * 20, 'Pressure: {0}'.format(player.combatant.savethrow_pressure)),
        (2 * css_width / 3, fontsize * 21, 'Bleed: {0}'.format(player.combatant.savethrow_bleed)),
        (2 * css_width / 3, fontsize * 22, 'Injury: {0}'.format(player.combatant.savethrow_injury)),
        (0, fontsize * 24, 'Presence: {0}'.format(player.combatant.presence)),
        (css_width / 3, fontsize * 24, 'Initiative: {0}'.format(player.combatant.initiative)),
        (2 * css_width / 3, fontsize * 24, 'Speed: {0}'.format(player.combatant.speed)),
        (0, fontsize * 25, 'Teamwork: {0}'.format(player.combatant.teamwork)),
        (css_width / 3, fontsize * 25, 'Leadership: {0}'.format(player.combatant.leadership))
    ]

    for i in lines:
        info = font.render(i[2], True, (255, 255, 255))
        window.blit(info, (i[0], i[1]))

    x = camera_width // 2 - css_width // 2
    y = camera_height // 2 - css_height // 2
    screen.blit(window, (x, y))


def noncombat_stats_screen(screen, player, css_width, css_height, camera_width, camera_height):
    window = pygame.Surface((css_width, css_height))
    fontsize = 12
    font = pygame.font.SysFont("comicsansms", fontsize)
    info = font.render('Leadership: {0}'.format(player.combatant.leadership), True, (255, 255, 255))
    window.blit(info, (css_width / 3, fontsize * 25))

    x = camera_width // 2 - css_width // 2
    y = camera_height // 2 - css_height // 2
    screen.blit(window, (x, y))


def message_box(screen, width, screen_width, screen_height):
    fontsize = 12

    menu(screen, '', fontsize, ['No save game to load :('], width, screen_width, screen_height)
