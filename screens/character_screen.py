from screens.gui_tools import get_alpha_surface, get_offset, get_text_surface, get_and_blit
import tcod as libtcod


def character_screen(screen, images, player):
    img = images.get('gui').get('character_screen')
    level = get_level_icon(images.get('gui').get('level_icon'), player)
    age = get_age_icon(images.get('gui').get('age_icon'), player)
    species = species_sex_icon(images.get('gui').get('species_sex_icons').get(player.combatant.phylo.species))
    sex = species_sex_icon(images.get('gui').get('species_sex_icons').get(player.combatant.sex))
    xp_bar = get_xp_icon(images.get('gui').get('xp_bar_icon'))
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
    surf.blit(xp_bar, ((surf.get_width() / 4) - (xp_bar.get_width() / 2), 420))
    screen.blit(surf, (215, 136))

def get_xp_icon(xp_bar):
    surf = get_alpha_surface(300, 20)
    surf.blit(xp_bar, (0, 0))

    return surf
def get_level_icon(bg, player):

    icon = get_alpha_surface(64, 46)
    icon.blit(bg, (0, 0))
    level = get_text_surface(str(player.combatant.level.current_level), fontsize=10, color=libtcod.white)
    get_and_blit(icon, level, 'x', 23)

    return icon

def get_age_icon(bg, player):
    icon = get_alpha_surface(64, 46)
    icon.blit(bg, (0, 0))
    age = get_text_surface(str(player.combatant.age), fontsize=10, color=libtcod.white)
    get_and_blit(icon, age, 'x', 23)

    return icon

def species_sex_icon(img):
    icon = get_alpha_surface(56, 56)
    icon.blit(img, (0, 0))
    return icon


