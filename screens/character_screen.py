from screens.gui_tools import get_alpha_surface, get_surface, get_offset, get_text_surface, align_and_blit
import tcod as libtcod
import math


def character_screen(screen, images, player):
    img = images.get('gui').get('character_screen')
    level = get_level_icon(images.get('gui').get('level_icon'), player)
    age = get_age_icon(images.get('gui').get('age_icon'), player)
    species = species_sex_icon(images.get('gui').get('species_sex_icons').get(player.combatant.phylo.species))
    sex = species_sex_icon(images.get('gui').get('species_sex_icons').get(player.combatant.sex))
    xp = get_xp_icon(images.get('gui').get('xp_bar_objs'), player)
    combat_stats = get_combat_stats(images.get('gui').get('combat_stats_objs'), player)
    saving_throws = get_saving_throws(images.get('gui').get('saving_throws_objs'), player)
    secondary_stats = get_secondary_stats(images.get('gui').get('secondary_stats_objs'), player)
    surf = get_alpha_surface(img.get_width() * 2, img.get_height())

    surf.blit(img, (0, 0))
    surf.blit(img, (img.get_width(), 0))
    p_name = get_text_surface(player.name, fontsize=25, color=libtcod.white)
    surf.blit(p_name, (surf.get_width() / 4 - p_name.get_width() / 2, 27))
    surf.blit(player.images.portrait, (get_offset(img, player.images.portrait, 'x'), 82))
    surf.blit(level, (35, 110))
    surf.blit(age, (35, 110 + level.get_height()))
    surf.blit(species, (39, 110 + level.get_height() + age.get_height() + 10))
    surf.blit(sex, (39, 110 + level.get_height() + age.get_height() + species.get_height() + 20))
    surf.blit(xp, ((surf.get_width() / 4) - (xp.get_width() / 2), 420))
    surf.blit(combat_stats, (320, 110))
    surf.blit(saving_throws, (500, 120))
    surf.blit(secondary_stats, (475, 345))
    screen.blit(surf, (215, 136))

def get_saving_throws(objs, player):
    ts = 32
    surf = get_alpha_surface(320, 288)

    surf.blit(objs.get('reflex'), (ts * 0, ts * 0))
    surf.blit(get_text_surface(str(player.combatant.savethrow_reflex), 18, libtcod.black), (ts * 1 + 20, ts * 0))
    surf.blit(objs.get('balance'), (ts * 0, ts * 1 + 10))
    surf.blit(get_text_surface(str(player.combatant.savethrow_balance), 18, libtcod.black), (ts * 1 + 20, ts * 1 + 15))
    surf.blit(objs.get('breath'), (ts * 0, ts * 2 + 20))
    surf.blit(get_text_surface(str(player.combatant.savethrow_breath), 18, libtcod.black), (ts * 1 + 20, ts * 2 + 25))
    surf.blit(objs.get('grapple'), (ts * 0, ts * 3 + 30))
    surf.blit(get_text_surface(str(player.combatant.savethrow_grapple), 18, libtcod.black), (ts * 1 + 20, ts * 3 + 35))
    surf.blit(objs.get('stun'), (ts * 0, ts * 4 + 40))
    surf.blit(get_text_surface(str(player.combatant.savethrow_stun), 18, libtcod.black), (ts * 1 + 20, ts * 4 + 45))

    surf.blit(objs.get('panic'), (ts * 3, ts * 0))
    surf.blit(get_text_surface(str(player.combatant.savethrow_panic), 18, libtcod.black), (ts * 4 + 20, ts * 0))
    surf.blit(objs.get('apathy'), (ts * 3, ts * 1 + 10))
    surf.blit(get_text_surface(str(player.combatant.savethrow_apathy), 18, libtcod.black), (ts * 4 + 20, ts * 1 + 15))
    surf.blit(objs.get('pain'), (ts * 3, ts * 2 + 20))
    surf.blit(get_text_surface(str(player.combatant.savethrow_pain), 18, libtcod.black), (ts * 4 + 20, ts * 2 + 25))
    surf.blit(objs.get('bewitch'), (ts * 3, ts * 3 + 30))
    surf.blit(get_text_surface(str(player.combatant.savethrow_bewitch), 18, libtcod.black), (ts * 4 + 20, ts * 3 + 35))
    surf.blit(objs.get('enrage'), (ts * 3, ts * 4 + 40))
    surf.blit(get_text_surface(str(player.combatant.savethrow_enrage), 18, libtcod.black), (ts * 4 + 20, ts * 4 + 45))

    surf.blit(objs.get('illness'), (ts * 6, ts * 0))
    surf.blit(get_text_surface(str(player.combatant.savethrow_illness), 18, libtcod.black), (ts * 7 + 20, ts * 0))
    surf.blit(objs.get('tenacity'), (ts * 6, ts * 1 + 10))
    surf.blit(get_text_surface(str(player.combatant.savethrow_tenacity), 18, libtcod.black), (ts * 7 + 20, ts * 1 + 15))
    surf.blit(objs.get('pressure'), (ts * 6, ts * 2 + 20))
    surf.blit(get_text_surface(str(player.combatant.savethrow_pressure), 18, libtcod.black), (ts * 7 + 20, ts * 2 + 25))
    surf.blit(objs.get('bleed'), (ts * 6, ts * 3 + 30))
    surf.blit(get_text_surface(str(player.combatant.savethrow_bleed), 18, libtcod.black), (ts * 7 + 20, ts * 3 + 35))
    surf.blit(objs.get('injury'), (ts * 6, ts * 4 + 40))
    surf.blit(get_text_surface(str(player.combatant.savethrow_injury), 18, libtcod.black), (ts * 7 + 20, ts * 4 + 45))

    return surf

def get_combat_stats(objs, player):
    ts = 32
    surf = get_alpha_surface(96, 320)
    surf.blit(objs.get('power'), (ts * 1, ts * 0))
    surf.blit(objs.get('resistance'), (ts * 2, ts * 0))
    surf.blit(objs.get('slash'), (ts * 0, ts * 1))
    surf.blit(get_text_surface(str(player.combatant.power_slash), 18, libtcod.black), (ts * 1, ts * 1))
    surf.blit(get_text_surface(str(player.combatant.resist_slash), 18, libtcod.black), (ts * 2, ts * 1))
    surf.blit(objs.get('pierce'), (ts * 0, ts * 2))
    surf.blit(get_text_surface(str(player.combatant.power_pierce), 18, libtcod.black), (ts * 1, ts * 2))
    surf.blit(get_text_surface(str(player.combatant.resist_pierce), 18, libtcod.black), (ts * 2, ts * 2))
    surf.blit(objs.get('blunt'), (ts * 0, ts * 3))
    surf.blit(get_text_surface(str(player.combatant.power_blunt), 18, libtcod.black), (ts * 1, ts * 3))
    surf.blit(get_text_surface(str(player.combatant.resist_blunt), 18, libtcod.black), (ts * 2, ts * 3))
    surf.blit(objs.get('heat'), (ts * 0, ts * 4))
    surf.blit(get_text_surface(str(player.combatant.spirit_heat), 18, libtcod.black), (ts * 1, ts * 4))
    surf.blit(get_text_surface(str(player.combatant.resist_heat), 18, libtcod.black), (ts * 2, ts * 4))
    surf.blit(objs.get('cold'), (ts * 0, ts * 5))
    surf.blit(get_text_surface(str(player.combatant.spirit_cold), 18, libtcod.black), (ts * 1, ts * 5))
    surf.blit(get_text_surface(str(player.combatant.resist_cold), 18, libtcod.black), (ts * 2, ts * 5))
    surf.blit(objs.get('acid'), (ts * 0, ts * 6))
    surf.blit(get_text_surface(str(player.combatant.spirit_acid), 18, libtcod.black), (ts * 1, ts * 6))
    surf.blit(get_text_surface(str(player.combatant.resist_acid), 18, libtcod.black), (ts * 2, ts * 6))
    surf.blit(objs.get('current'), (ts * 0, ts * 7))
    surf.blit(get_text_surface(str(player.combatant.spirit_current), 18, libtcod.black), (ts * 1, ts * 7))
    surf.blit(get_text_surface(str(player.combatant.resist_current), 18, libtcod.black), (ts * 2, ts * 7))
    surf.blit(objs.get('aether'), (ts * 0, ts * 8))
    surf.blit(get_text_surface(str(player.combatant.spirit_aether), 18, libtcod.black), (ts * 1, ts * 8))
    surf.blit(get_text_surface(str(player.combatant.resist_aether), 18, libtcod.black), (ts * 2, ts * 8))

    return surf

def get_secondary_stats(objs, player):
    ts = 32
    surf = get_alpha_surface(336, 64)
    surf.blit(objs.get('initiative'), (ts * 0, ts * 0))
    surf.blit(get_text_surface(str(player.combatant.initiative), 18, libtcod.black), (ts * 1 + 15, ts * 0))
    surf.blit(objs.get('speed'), (ts * 0, ts * 1))
    surf.blit(get_text_surface(str(player.combatant.speed), 18, libtcod.black), (ts * 1 + 15, ts * 1))
    surf.blit(objs.get('accuracy'), (ts * 2 + 20, ts * 0))
    surf.blit(get_text_surface(str(player.combatant.accuracy), 18, libtcod.black), (ts * 3 + 35, ts * 0))
    surf.blit(objs.get('dodge'), (ts * 2 + 20, ts * 1))
    surf.blit(get_text_surface(str(player.combatant.dodge), 18, libtcod.black), (ts * 3 + 35, ts * 1))
    surf.blit(objs.get('leadership'), (ts * 4 + 40, ts * 0))
    surf.blit(get_text_surface(str(player.combatant.leadership), 18, libtcod.black), (ts * 5 + 55, ts * 0))
    surf.blit(objs.get('teamwork'), (ts * 4 + 40, ts * 1))
    surf.blit(get_text_surface(str(player.combatant.teamwork), 18, libtcod.black), (ts * 5 + 55, ts * 1))
    surf.blit(objs.get('presence'), (ts * 6 + 60, ts * 0.5))
    surf.blit(get_text_surface(str(player.combatant.presence), 18, libtcod.black), (ts * 7 + 75, ts * 0.5))
    return surf


def get_xp_icon(xp_objs, player):
    surf = get_alpha_surface(300, 20)
    surf.blit(xp_objs.get('xp_bar'), (0, 0))

    off_x = 35
    off_y = 8
    step = 5
    current_chunk = 0
    chunks = math.floor(player.combatant.level.percentage_leveled / 2)
    if chunks > 50:
        chunks = 50
    for i in range(chunks):
        surf.blit(xp_objs.get('xp' + str(current_chunk)), (off_x, off_y))
        off_x += step
        if current_chunk == 4:
            current_chunk = 0
        else:
            current_chunk += 1

    return surf


def get_level_icon(bg, player):

    icon = get_surface()
    level = get_text_surface(str(player.combatant.level.current_level), fontsize=10, color=libtcod.white)
    align_and_blit(icon, level, x_ratio=0.5, y_ratio=0.68)

    return icon

def get_age_icon(bg, player):
    icon = get_surface(bg)

    age = get_text_surface(str(player.combatant.age), fontsize=10, color=libtcod.white)
    align_and_blit(icon, age, x_ratio=0.5, y_ratio=0.68)

    return icon

def species_sex_icon(img):
    icon = get_surface(img)
    return icon


