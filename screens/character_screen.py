from pygame.transform import scale
from config.constants import WHITE
from data_structures.gui_tools import get_alpha_surface, get_surface, get_text_surface, align_and_blit
from config.image_objects import CHARACTER_SHEET_BASE, XP_FILL
from screens.resources_HUD import get_resource_vals


def character_screen(self):

    char_sheet = get_surface(CHARACTER_SHEET_BASE)
    player = self.game.model.party.p1

    # level = get_level_icon(player)
    # age = get_age_icon(player)
    # species = None
    # sex = None

    xp = display_xp_fill(player)
    resources = display_resources(player)
    primaries = display_primary_stats(player)
    secondaries = display_secondary_stats(player)
    attributes = display_attributes(player)
    saves = display_saving_throws(player)

    p_name = get_text_surface(player.name, fontsize=25, color=WHITE, style='source_sans_pro')
    align_and_blit(char_sheet, p_name, x_ratio=0.23, y_ratio=0.25)
    align_and_blit(char_sheet, player.images.portrait, x_ratio=0.23)
    # surf.blit(level, (35, 110))
    # surf.blit(age, (35, 110 + level.get_height()))
    # surf.blit(species, (39, 110 + level.get_height() + age.get_height() + 10))
    # surf.blit(sex, (39, 110 + level.get_height() + age.get_height() + species.get_height() + 20))
    # surf.blit(xp, ((surf.get_width() / 4) - (xp.get_width() / 2), 420))
    align_and_blit(char_sheet, resources, x_ratio=0.23, y_ratio=0.9)
    align_and_blit(char_sheet, xp, x_ratio=0.224, y_ratio=0.948)
    char_sheet.blit(primaries, (405, 175))
    char_sheet.blit(secondaries, (475, 387))
    char_sheet.blit(attributes, (675, 145))
    char_sheet.blit(saves, (605, 386))
    align_and_blit(self.screen, char_sheet)


def display_resources(player):
    display = get_alpha_surface(260, 36)
    ratio_dict = {'HP': (0.25, 0.25), 'MP': (0.25, 0.75), 'TP': (0.75, 0.25), 'VP': (0.75, 0.75)}
    for resource in ('HP', 'MP', 'TP', 'VP'):
        percent, now_val, max_val, font_color = get_resource_vals(player, resource)
        ratio = ratio_dict.get(resource)
        x_ratio, y_ratio = ratio

        text = get_text_surface(str(now_val) + '  /  ' + str(max_val), 16, font_color, )
        align_and_blit(display, text, x_ratio, y_ratio)

    return display


def display_primary_stats(player):
    ts = 19
    display = get_alpha_surface(92, ts*8)

    align_and_blit(display, get_text_surface(str(player.combatant.power_slash), 16, WHITE, ),
                   x_ratio=0.20, y_ratio=.0625)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_slash), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.0625)
    align_and_blit(display, get_text_surface(str(player.combatant.power_pierce), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.1875)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_pierce), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.1875)
    align_and_blit(display, get_text_surface(str(player.combatant.power_blunt), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.3125)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_blunt), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.3125)
    align_and_blit(display, get_text_surface(str(player.combatant.power_heat), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.4375)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_heat), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.4375)
    align_and_blit(display, get_text_surface(str(player.combatant.power_cold), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.5625)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_cold), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.5625)
    align_and_blit(display, get_text_surface(str(player.combatant.power_acid), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.6875)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_acid), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.6875)
    align_and_blit(display, get_text_surface(str(player.combatant.power_current), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.8125)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_current), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.8125)
    align_and_blit(display, get_text_surface(str(player.combatant.power_aether), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.20, y_ratio=.9375)
    align_and_blit(display, get_text_surface(str(player.combatant.resist_aether), 16, WHITE, 'source_sans_pro'),
                   x_ratio=0.80, y_ratio=.9375)

    return display


def display_secondary_stats(player):
    gap = 19
    c = player.combatant
    stats = [c.initiative, c.speed, c.accuracy, c.dodge, c.critical_strike, c.critical_damage, c.teamwork, c.presence]
    display = get_alpha_surface(38, gap*len(stats))
    for ind, stat in enumerate(stats):
        align_and_blit(display, get_text_surface(str(stat), 16, WHITE, 'source_sans_pro'), y_ratio=.0625 + (0.125*ind))

    return display


def display_attributes(player):
    gap = 19
    a = player.combatant.attributes
    atts = [a.strength, a.instinct, a.coordination, a.endurance, a.arcana, a.improvisation, a.wisdom, a.finesse,
            a.charisma, a.devotion]
    display = get_alpha_surface(28, gap*len(atts))
    for ind, stat in enumerate(atts):
        align_and_blit(display, get_text_surface(str(stat), 16, WHITE, 'source_sans_pro'), y_ratio=.05 + (0.1*ind))
    return display


def display_saving_throws(player):
    gap = 25
    c = player.combatant
    save_l = [c.savethrow_injury, c.savethrow_tenacity, c.savethrow_composure, c.savethrow_cognition, c.savethrow_breath, c.savethrow_corruption]
    save_r = [c.savethrow_illness, c.savethrow_apathy, c.savethrow_pain, c.savethrow_force, c.savethrow_reflex, c.savethrow_will]
    display = get_alpha_surface(100, gap*len(save_r))
    for ind, stat in enumerate(save_l):
        align_and_blit(display, get_text_surface(str(stat), 16, WHITE, 'source_sans_pro'), x_ratio=0.1, y_ratio=.0833 + (0.1666*ind))
    for ind, stat in enumerate(save_r):
        align_and_blit(display, get_text_surface(str(stat), 16, WHITE, 'source_sans_pro'), x_ratio=0.9, y_ratio=.0833 + (0.1666*ind))

    return display


def display_xp_fill(player):
    fill = get_surface(XP_FILL)
    l = player.combatant.level
    display = get_alpha_surface(fill.get_width(), fill.get_height())
    align_and_blit(display, scale(fill, (int(fill.get_width() * l.percentage_leveled/100), fill.get_height())))
    xp_text = get_text_surface('XP:  ' + str(l.current_xp) + '  /  ' + str(l.experience_to_next_level) + '  ( ' + str(int(l.percentage_leveled)) + '% )', fontsize=8, color=WHITE)
    align_and_blit(display, xp_text)

    return display
#
# def get_level_icon(player):
#
#     icon = get_surface(CHARACTER_SCREEN.get('level'))
#     level = get_text_surface(str(player.combatant.level.current_level), fontsize=10, color=libtcod.white)
#     align_and_blit(icon, level, x_ratio=0.5, y_ratio=0.68)
#
#     return icon
#
# def get_age_icon(player):
#     icon = get_surface(CHARACTER_SCREEN.get('age'))
#
#     age = get_text_surface(str(player.age.year), fontsize=10, color=libtcod.white)
#     align_and_blit(icon, age, x_ratio=0.5, y_ratio=0.68)
#
#     return icon

