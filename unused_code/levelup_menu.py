from config.image_objects import LEVELUP_MENU


def level_up_menu(screen, player):
    att = player.combatant.attributes
    options = ['Strength ({0} -> {1})'.format(att.strength, att.strength + 1),
               'Instinct ({0} -> {1})'.format(att.instinct, att.instinct + 1),
               'Coordination ({0} -> {1})'.format(att.coordination, att.coordination + 1),
               'Vitality ({0} -> {1})'.format(att.vitality, att.vitality + 1),
               'Arcana ({0} -> {1})'.format(att.arcana, att.arcana + 1),
               'Improvisation ({0} -> {1})'.format(att.improvisation, att.improvisation + 1),
               'Wisdom ({0} -> {1})'.format(att.wisdom, att.wisdom + 1),
               'Finesse ({0} -> {1})'.format(att.finesse, att.finesse + 1),
               'Charisma ({0} -> {1})'.format(att.charisma, att.charisma + 1),
               'Devotion ({0} -> {1})'.format(att.devotion, att.devotion + 1)]
    fontsize = 14
    menu_width = 200
    menu_height = 200
    off_x = 16
    off_y = 21
    gui_img = LEVELUP_MENU


