import pygame as py
from screens.frozen_surface import FrozenSurface
from ECS.image_bundle import ImageBundle

TITLE_SCREEN_BG = py.image.load('images\\background\\main_menu.png')
TITLE_MENU_BG = py.image.load('images\\GUI\\menus\\title_menu.png')
TITLE_MENU_BUTTON = py.image.load('images\\GUI\\menus\\title_button.png')

ENCOUNTER_MESSAGE_BG = py.image.load('images\\GUI\\encounter\\message_bg.png')
ENCOUNTER_MENU = py.image.load('images\\GUI\\menus\\encounter_menu.png')
ENCOUNTER_BUTTON = py.image.load('images\\GUI\\menus\\option_button.png')
DIALOGUE_MENU = py.image.load('images\\GUI\\dialogue_menu.png')
SHOP_MENU = py.image.load('images\\GUI\\shop_menu.png')
LEVELUP_MENU = py.image.load('images\\GUI\\levelup_menu.png')

INVENTORY_BG = py.image.load('images\\GUI\\inventory\\inven_bg.png')
EQUIPMENT_BG = py.image.load('images\\GUI\\inventory\\equipment_bg.png')
INVENTORY_OPTIONS = [py.image.load('images\\GUI\\inventory\\miscellaneous.png'),
                     py.image.load('images\\GUI\\inventory\\weapons.png'),
                     py.image.load('images\\GUI\\inventory\\armor.png'),
                     py.image.load('images\\GUI\\inventory\\accessories.png'),
                     py.image.load('images\\GUI\\inventory\\satchel.png'),
                     py.image.load('images\\GUI\\inventory\\materials.png'),
                     py.image.load('images\\GUI\\inventory\\plot.png')]

LIFE_BACKDROP = py.image.load('images\\GUI\\life\\life_backdrop.png')
MINI_MAP = py.image.load('images\\GUI\\life\\minimap.png')
CLOCK = py.image.load('images\\GUI\\life\\clock.png')
UPCOMING_EVENTS = py.image.load('images\\GUI\\life\\upcoming_events.png')
EVENT_LOG_BG = py.image.load('images\\GUI\\life\\event_log_bg.png')

TURN_ORDER_QUEUE = py.image.load('images\\GUI\\encounter\\turn_order_queue.png')

GOLD = py.image.load('images\\GUI\\menus\\silver.png')
SILVER = py.image.load('images\\GUI\\menus\\silver.png')
COPPER = py.image.load('images\\GUI\\menus\\copper.png')

JOURNAL_OBJS = {
    'bg': py.image.load('images\\GUI\\journal\\journal_bg.png'),
    'icon0': py.image.load('images\\GUI\\journal\\current.png'),
    'text0': py.image.load('images\\GUI\\journal\\current_text.png'),
    'icon1': py.image.load('images\\GUI\\journal\\completed.png'),
    'text1': py.image.load('images\\GUI\\journal\\completed_text.png'),
    'icon2': py.image.load('images\\GUI\\journal\\codex.png'),
    'text2': py.image.load('images\\GUI\\journal\\codex_text.png'),
    'icon3': py.image.load('images\\GUI\\journal\\history.png'),
    'text3': py.image.load('images\\GUI\\journal\\history_text.png'),
    'quest_holder': py.image.load('images\\GUI\\journal\\quest_holder.png'),
}

LOOT_BG = py.image.load('images\\GUI\\looting\\loot_bg.png')
LOOT_BANNER = py.image.load('images\\GUI\\looting\\loot_banner.png')

CALENDAR_BG = py.image.load('images\\GUI\\life\\calendar.png')
CALENDAR_CIRCLE = py.image.load('images\\GUI\\life\\calendar_circle.png')

INDICATOR_H = py.image.load('images\\GUI\\menus\\indicator_h.png')
INDICATOR_V = py.image.load('images\\GUI\\menus\\indicator_v.png')
POINTER_RIGHT = py.image.load('images\\GUI\\icons\\pointer_right.png')

STAIRS_DOWN = ImageBundle(py.image.load('images\\entities\\transitions\\stairsdown.png'))
STAIRS_UP = ImageBundle(py.image.load('images\\entities\\transitions\\stairsup.png'))

ALPHA = py.image.load('images\\alpha.png')
BUNDLE_ALPHA = ImageBundle(ALPHA)


BUNDLE_SAMWISE = ImageBundle(py.image.load('images\\entities\\noncombatants\\samwise\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\samwise\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\samwise\\port_mini.png'))

BUNDLE_MAGE = ImageBundle(py.image.load('images\\entities\\noncombatants\\mage\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\mage\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\mage\\port_mini.png'))

BUNDLE_GUARD_CAPTAIN = ImageBundle(py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\guard_captain\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\guard_captain\\port_mini.png'))

BUNDLE_PRIEST = ImageBundle(py.image.load('images\\entities\\noncombatants\\priest\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\priest\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\priest\\port_mini.png'))

BUNDLE_ROGUE = ImageBundle(py.image.load('images\\entities\\noncombatants\\rogue\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\rogue\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\rogue\\port_mini.png'))

BUNDLE_HOMER = ImageBundle(py.image.load('images\\entities\\noncombatants\\homer\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\homer\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\homer\\port_mini.png'))

BUNDLE_MAYOR = ImageBundle(py.image.load('images\\entities\\noncombatants\\mayor\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\mayor\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\mayor\\port_mini.png'))

BUNDLE_INNKEEPER = ImageBundle(py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\innkeeper\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\innkeeper\\port_mini.png'))

BUNDLE_TAVERNKEEPER = ImageBundle(py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\tavernkeeper\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\tavernkeeper\\port_mini.png'))
HERO_DOWN0 = py.image.load('images\\entities\\combatants\\hero\\sprite_00.png')
HERO_DOWN1 = py.image.load('images\\entities\\combatants\\hero\\sprite_01.png')
HERO_DOWN2 = py.image.load('images\\entities\\combatants\\hero\\sprite_02.png')
HERO_LEFT0 = py.image.load('images\\entities\\combatants\\hero\\sprite_03.png')
HERO_LEFT1 = py.image.load('images\\entities\\combatants\\hero\\sprite_04.png')
HERO_LEFT2 = py.image.load('images\\entities\\combatants\\hero\\sprite_05.png')
HERO_RIGHT0 = py.image.load('images\\entities\\combatants\\hero\\sprite_06.png')
HERO_RIGHT1 = py.image.load('images\\entities\\combatants\\hero\\sprite_07.png')
HERO_RIGHT2 = py.image.load('images\\entities\\combatants\\hero\\sprite_08.png')
HERO_UP0 = py.image.load('images\\entities\\combatants\\hero\\sprite_09.png')
HERO_UP1 = py.image.load('images\\entities\\combatants\\hero\\sprite_10.png')
HERO_UP2 = py.image.load('images\\entities\\combatants\\hero\\sprite_11.png')
HERO_PORTRAIT = py.image.load('images\\entities\\combatants\\hero\\portrait.png')
HERO_PORTMINI = py.image.load('images\\entities\\combatants\\hero\\port_mini.png')
HERO_ACTOR = py.image.load('images\\entities\\combatants\\hero\\actor.png')

HERO_SPRITE_DICT = {(0, 1): [HERO_DOWN0, HERO_DOWN0, HERO_DOWN0, HERO_DOWN1, HERO_DOWN1, HERO_DOWN1, HERO_DOWN2,
                             HERO_DOWN2, HERO_DOWN2, HERO_DOWN1, HERO_DOWN1, HERO_DOWN1],
                    (0, -1): [HERO_UP0, HERO_UP0, HERO_UP0, HERO_UP1, HERO_UP1, HERO_UP1, HERO_UP2, HERO_UP2, HERO_UP2,
                              HERO_UP1, HERO_UP1, HERO_UP1],
                    (-1, 0): [HERO_LEFT0, HERO_LEFT0, HERO_LEFT0, HERO_LEFT1, HERO_LEFT1, HERO_LEFT1, HERO_LEFT2,
                              HERO_LEFT2, HERO_LEFT2, HERO_LEFT1, HERO_LEFT1, HERO_LEFT1],
                    (1, 0): [HERO_RIGHT0, HERO_RIGHT0, HERO_RIGHT0, HERO_RIGHT1, HERO_RIGHT1, HERO_RIGHT1, HERO_RIGHT2,
                             HERO_RIGHT2, HERO_RIGHT2, HERO_RIGHT1, HERO_RIGHT1, HERO_RIGHT1],
                    }

BUNDLE_HERO = ImageBundle(HERO_SPRITE_DICT,
                          HERO_SPRITE_DICT.get((0, 1)),
                          HERO_PORTRAIT,
                          HERO_PORTMINI,
                          HERO_ACTOR)


DUNGEON_ALPHA_NONCOMBATANT_IMAGE_BUNDLES = {'samwise': BUNDLE_SAMWISE,
                                            'mage': BUNDLE_MAGE,
                                            'guard_captain': BUNDLE_GUARD_CAPTAIN,
                                            'priest': BUNDLE_PRIEST,
                                            'rogue': BUNDLE_ROGUE,
                                            'mayor': BUNDLE_MAYOR,
                                            'homer': BUNDLE_HOMER,
                                            'innkeeper': BUNDLE_INNKEEPER,
                                            'tavernkeeper': BUNDLE_TAVERNKEEPER, }

BUNDLE_STICK = ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\sprite.png'),
                           py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\portrait.png'),
                           py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\port_mini.png'))

BUNDLE_WEAPONS = {
    'staff': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\staff\\sprite.png')),
    'dagger': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\dagger\\sprite.png')),
    'shield': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\shield\\sprite.png')),
    'longsword': ImageBundle(py.image.load('images\\entities\\items\\equippables\\weapons\\longsword\\sprite.png'),
                             py.image.load('images\\entities\\items\\equippables\\weapons\\longsword\\portrait.png')),
}

BUNDLE_POTION = ImageBundle(py.image.load('images\\entities\\items\\useables\\potion\\sprite.png'),
                            py.image.load('images\\entities\\items\\useables\\potion\\portrait.png'),
                            py.image.load('images\\entities\\items\\useables\\potion\\port_mini.png'))
SCROLL = py.image.load('images\\entities\\items\\useables\\scroll\\sprite.png')

BUNDLE_MOBS = {
    'rat': ImageBundle(actor=py.image.load('images\\entities\\combatants\\rat\\actor.png')),
    'bat': ImageBundle(actor=py.image.load('images\\entities\\combatants\\bat\\actor.png')),
    'bear': ImageBundle(actor=py.image.load('images\\entities\\combatants\\bear\\actor.png')),
    'goblin': ImageBundle(actor=py.image.load('images\\entities\\combatants\\goblin\\actor.png')),
    'kobold': ImageBundle(actor=py.image.load('images\\entities\\combatants\\kobold\\actor.png')),
    'raccoon': ImageBundle(actor=py.image.load('images\\entities\\combatants\\raccoon\\actor.png')),
    'salamander': ImageBundle(actor=py.image.load('images\\entities\\combatants\\salamander\\actor.png')),
    'snail': ImageBundle(actor=py.image.load('images\\entities\\combatants\\snail\\actor.png')),
    'shrimp': ImageBundle(actor=py.image.load('images\\entities\\combatants\\shrimp\\actor.png')),
    'spider': ImageBundle(actor=py.image.load('images\\entities\\combatants\\spider\\actor.png')),
}

CHARACTER_SCREEN = {
    'bg': py.image.load('images\\GUI\\character_sheet\\char_sheet.png'),
    'level': py.image.load('images\\GUI\\character_sheet\\level_icon.png'),
    'age': py.image.load('images\\GUI\\character_sheet\\age_icon.png'),
    'power': py.image.load('images\\GUI\\character_sheet\\power.png'),
    'resistance': py.image.load('images\\GUI\\character_sheet\\resistance.png'),
    'slash': py.image.load('images\\GUI\\character_sheet\\slash.png'),
    'pierce': py.image.load('images\\GUI\\character_sheet\\pierce.png'),
    'blunt': py.image.load('images\\GUI\\character_sheet\\blunt.png'),
    'heat': py.image.load('images\\GUI\\character_sheet\\heat.png'),
    'cold': py.image.load('images\\GUI\\character_sheet\\cold.png'),
    'acid': py.image.load('images\\GUI\\character_sheet\\acid.png'),
    'current': py.image.load('images\\GUI\\character_sheet\\current.png'),
    'aether': py.image.load('images\\GUI\\character_sheet\\aether.png'),
    'accuracy': py.image.load('images\\GUI\\character_sheet\\accuracy.png'),
    'dodge': py.image.load('images\\GUI\\character_sheet\\dodge.png'),
    'initiative': py.image.load('images\\GUI\\character_sheet\\initiative.png'),
    'speed': py.image.load('images\\GUI\\character_sheet\\speed.png'),
    'teamwork': py.image.load('images\\GUI\\character_sheet\\teamwork.png'),
    'leadership': py.image.load('images\\GUI\\character_sheet\\leadership.png'),
    'presence': py.image.load('images\\GUI\\character_sheet\\presence.png'),
    'reflex': py.image.load('images\\GUI\\character_sheet\\reflex.png'),
    'balance': py.image.load('images\\GUI\\character_sheet\\balance.png'),
    'breath': py.image.load('images\\GUI\\character_sheet\\breath.png'),
    'grapple': py.image.load('images\\GUI\\character_sheet\\grapple.png'),
    'stun': py.image.load('images\\GUI\\character_sheet\\stun.png'),
    'panic': py.image.load('images\\GUI\\character_sheet\\panic.png'),
    'apathy': py.image.load('images\\GUI\\character_sheet\\apathy.png'),
    'pain': py.image.load('images\\GUI\\character_sheet\\pain.png'),
    'bewitch': py.image.load('images\\GUI\\character_sheet\\bewitch.png'),
    'enrage': py.image.load('images\\GUI\\character_sheet\\enrage.png'),
    'illness': py.image.load('images\\GUI\\character_sheet\\illness.png'),
    'tenacity': py.image.load('images\\GUI\\character_sheet\\tenacity.png'),
    'pressure': py.image.load('images\\GUI\\character_sheet\\pressure.png'),
    'bleed': py.image.load('images\\GUI\\character_sheet\\bleed.png'),
    'injury': py.image.load('images\\GUI\\character_sheet\\injury.png'),
    'xp_bar': py.image.load('images\\GUI\\character_sheet\\xp_bar.png'),
    'xp0': py.image.load('images\\GUI\\character_sheet\\xp0.png'),
    'xp1': py.image.load('images\\GUI\\character_sheet\\xp1.png'),
    'xp2': py.image.load('images\\GUI\\character_sheet\\xp2.png'),
    'xp3': py.image.load('images\\GUI\\character_sheet\\xp3.png'),
    'xp4': py.image.load('images\\GUI\\character_sheet\\xp4.png'),
    'human': py.image.load('images\\GUI\\character_sheet\\human_icon.png'),
    'male': py.image.load('images\\GUI\\character_sheet\\male_icon.png'),
    'female': py.image.load('images\\GUI\\character_sheet\\female_icon.png'),
}
RESOURCE_HUD_BASE = py.image.load('images\\GUI\\life\\resources_hud\\base_layer.png')
RESOURCE_HUD_OVERLAY = py.image.load('images\\GUI\\life\\resources_hud\\portrait_overlay.png')
HP = py.image.load('images\\GUI\\life\\resources_hud\\hp.png')
MP = py.image.load('images\\GUI\\life\\resources_hud\\mp.png')
TP = py.image.load('images\\GUI\\life\\resources_hud\\tp.png')
VP = py.image.load('images\\GUI\\life\\resources_hud\\vp.png')

PARTY_SETTINGS_FRAME = py.image.load('images\\GUI\\life\\party_settings_frame.png')

RESOURCE_HUD = {
    'frame': py.image.load('images\\GUI\\resources_hud\\portrait_mini_frame.png'),
    'resource_bar': py.image.load('images\\GUI\\resources_hud\\resource_bar.png'),
    'HP': py.image.load('images\\GUI\\resources_hud\\HP.png'),
    'MP': py.image.load('images\\GUI\\resources_hud\\MP.png'),
    'TP': py.image.load('images\\GUI\\resources_hud\\TP.png'),
    'VP': py.image.load('images\\GUI\\resources_hud\\VP.png'),
    'HPleft0': py.image.load('images\\GUI\\resources_hud\\real_hp\\left0.png'),
    'HPleft1': py.image.load('images\\GUI\\resources_hud\\real_hp\\left1.png'),
    'HPmid': py.image.load('images\\GUI\\resources_hud\\real_hp\\mid.png'),
    'HPright0': py.image.load('images\\GUI\\resources_hud\\real_hp\\right0.png'),
    'HPright1': py.image.load('images\\GUI\\resources_hud\\real_hp\\right1.png'),
    'MPleft0': py.image.load('images\\GUI\\resources_hud\\real_mp\\left0.png'),
    'MPleft1': py.image.load('images\\GUI\\resources_hud\\real_mp\\left1.png'),
    'MPmid': py.image.load('images\\GUI\\resources_hud\\real_mp\\mid.png'),
    'MPright0': py.image.load('images\\GUI\\resources_hud\\real_mp\\right0.png'),
    'MPright1': py.image.load('images\\GUI\\resources_hud\\real_mp\\right1.png'),
    'TPleft0': py.image.load('images\\GUI\\resources_hud\\real_tp\\left0.png'),
    'TPleft1': py.image.load('images\\GUI\\resources_hud\\real_tp\\left1.png'),
    'TPmid': py.image.load('images\\GUI\\resources_hud\\real_tp\\mid.png'),
    'TPright0': py.image.load('images\\GUI\\resources_hud\\real_tp\\right0.png'),
    'TPright1': py.image.load('images\\GUI\\resources_hud\\real_tp\\right1.png'),
    'VPleft0': py.image.load('images\\GUI\\resources_hud\\real_vp\\left0.png'),
    'VPleft1': py.image.load('images\\GUI\\resources_hud\\real_vp\\left1.png'),
    'VPmid': py.image.load('images\\GUI\\resources_hud\\real_vp\\mid.png'),
    'VPright0': py.image.load('images\\GUI\\resources_hud\\real_vp\\right0.png'),
    'VPright1': py.image.load('images\\GUI\\resources_hud\\real_vp\\right1.png'),
}
BACKGROUNDS = {
    'deep': py.image.load('images\\background\\deep.png'),
    'desert': py.image.load('images\\background\\desert.png'),
    'forest': py.image.load('images\\background\\forest.png'),
    'plains': py.image.load('images\\background\\plains.png'),
    'savannah': py.image.load('images\\background\\savannah.png'),
    'shallow': py.image.load('images\\background\\shallow.png'),
    'snow': py.image.load('images\\background\\snow.png'),
    'taiga': py.image.load('images\\background\\taiga.png'),
    'temprain': py.image.load('images\\background\\temprain.png'),
    'tropicrain': py.image.load('images\\background\\tropicrain.png'),
    'tundra': py.image.load('images\\background\\tundra.png'),
    'cave': py.image.load('images\\background\\cave.png'),
}

MINIMAP = {
    'deep': py.image.load('images\\tiles\\overworld\\mini_map\\deep.png'),
    'desert': py.image.load('images\\tiles\\overworld\\mini_map\\desert.png'),
    'forest': py.image.load('images\\tiles\\overworld\\mini_map\\forest.png'),
    'plains': py.image.load('images\\tiles\\overworld\\mini_map\\plains.png'),
    'savannah': py.image.load('images\\tiles\\overworld\\mini_map\\savannah.png'),
    'shallow': py.image.load('images\\tiles\\overworld\\mini_map\\shallow.png'),
    'snow': py.image.load('images\\tiles\\overworld\\mini_map\\snow.png'),
    'taiga': py.image.load('images\\tiles\\overworld\\mini_map\\taiga.png'),
    'temprain': py.image.load('images\\tiles\\overworld\\mini_map\\temprain.png'),
    'tropicrain': py.image.load('images\\tiles\\overworld\\mini_map\\tropicrain.png'),
    'tundra': py.image.load('images\\tiles\\overworld\\mini_map\\tundra.png')

}

DEEP_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\deep_base.png')
DESERT_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\desert_base.png')
FOREST_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\forest_base.png')
PLAINS_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\plains_base.png')
SAVANNAH_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\savannah_base.png')
SHALLOW_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\shallow_base.png')
SNOW_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\snow_base.png')
TAIGA_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\taiga_base.png')
TEMPRAIN_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\temprain_base.png')
TROPICRAIN_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\tropicrain_base.png')
TUNDRA_TILE_FLOOR = py.image.load('images\\tiles\\overworld\\tundra_base.png')


TILE_BASE = {
    'black': py.image.load('images\\tiles\\black.png'),
}

GRASS_TILE_FLOOR = py.image.load('images\\tiles\\grass.png')

STONE_WALL = {
    '00001000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00001000.png'),
    '00010000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00010000.png'),
    '00001010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00001010.png'),
    '00011000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00011000.png'),
    '00011100': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00011000.png'),
    '00011001': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00011000.png'),
    '10011000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00011000.png'),
    '00111000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00011000.png'),
    '00010010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00010010.png'),
    '00000010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00000010.png'),
    '01001010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01001010.png'),
    '01100010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01000010.png'),
    '11000010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01000010.png'),
    '01000011': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01000010.png'),
    '01000110': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01000010.png'),
    '01010010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01010010.png'),
    '01000010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01000010.png'),
    '01011010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01011010.png'),
    '01000000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01000000.png'),
    '00011010': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall00011010.png'),
    '01011000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01011000.png'),
    '01001000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01001000.png'),
    '01010000': py.image.load('images\\entities\\blockers\\stone_wall\\stone_wall01010000.png'),
}

DIRT_TILE_FLOOR = {
    '00001011': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road00001011.png'),
    '00010110': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road00010110.png'),
    '00011111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road00011111.png'),
    '01101000': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road01101000.png'),
    '01101011': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road01101011.png'),
    '01111111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road01111111.png'),
    '11010000': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11010000.png'),
    '11010110': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11010110.png'),
    '11011111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11011111.png'),
    '11111000': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11111000.png'),
    '11111110': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11111110.png'),
    '11111111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11111111.png'),
    '00111111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road00111111.png'),
    '01101111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road01101111.png'),
    '10011111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road10011111.png'),
    '11010111': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11010111.png'),
    '11101011': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11101011.png'),
    '11110110': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11110110.png'),
    '11111001': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11111001.png'),
    '11111100': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11111100.png'),
    '11111011': FrozenSurface.load('images\\tiles\\roads\\', 'dirt_road11111011.png'),
}

OVERWORLD_TOWN = [[py.image.load('images\\tiles\\overworld\\town\\town0.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town1.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town2.png')],
                  [py.image.load('images\\tiles\\overworld\\town\\town3.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town4.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town5.png')],
                  [py.image.load('images\\tiles\\overworld\\town\\town6.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town7.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town8.png')]]

EXT_LEFT_EDGE_BOT = py.image.load('images\\structures\\wood\\ext_left_edge_bot.png')
EXT_LEFT_EDGE_TOP = py.image.load('images\\structures\\wood\\ext_left_edge_top.png')
EXT_LEFT_WALL = py.image.load('images\\structures\\wood\\ext_left_wall.png')
EXT_EXTEND_BOT = py.image.load('images\\structures\\wood\\ext_extend_bot.png')
EXT_EXTEND_TOP = py.image.load('images\\structures\\wood\\ext_extend_top.png')
EXT_LEFT_DOORFRAME_BOT = py.image.load('images\\structures\\wood\\ext_left_doorframe_bot.png')
EXT_LEFT_DOORFRAME_TOP = py.image.load('images\\structures\\wood\\ext_left_doorframe_top.png')
EXT_DOORWAY_BOT = py.image.load('images\\structures\\wood\\ext_doorway_bot.png')
EXT_DOORWAY_TOP = py.image.load('images\\structures\\wood\\ext_doorway_top.png')
EXT_RIGHT_DOORFRAME_BOT = py.image.load('images\\structures\\wood\\ext_right_doorframe_bot.png')
EXT_RIGHT_DOORFRAME_TOP = py.image.load('images\\structures\\wood\\ext_right_doorframe_top.png')
EXT_WINDOW_LEFT_BOT = py.image.load('images\\structures\\wood\\ext_window_left_bot.png')
EXT_WINDOW_LEFT_TOP = py.image.load('images\\structures\\wood\\ext_window_left_top.png')
EXT_WINDOW_RIGHT_BOT = py.image.load('images\\structures\\wood\\ext_window_right_bot.png')
EXT_WINDOW_RIGHT_TOP = py.image.load('images\\structures\\wood\\ext_window_right_top.png')
EXT_RIGHT_EDGE_BOT = py.image.load('images\\structures\\wood\\ext_right_edge_bot.png')
EXT_RIGHT_EDGE_TOP = py.image.load('images\\structures\\wood\\ext_right_edge_top.png')
EXT_RIGHT_WALL = py.image.load('images\\structures\\wood\\ext_right_wall.png')

BLACK_ROOF_BACK_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_back_left_connect.png')
BLACK_ROOF_BACK_MID_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_back_mid_connect.png')
BLACK_ROOF_BACK_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_back_right_connect.png')
BLACK_ROOF_FRONT_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_front_left_connect.png')
BLACK_ROOF_FRONT_MID_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_front_mid_connect.png')
BLACK_ROOF_FRONT_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_front_right_connect.png')
BLACK_ROOF_LEFT = py.image.load('images\\structures\\roofs\\black_roof_left.png')
BLACK_ROOF_MID = py.image.load('images\\structures\\roofs\\black_roof_mid.png')
BLACK_ROOF_BACK_LEFT_PEAK = py.image.load('images\\structures\\roofs\\black_roof_back_left_peak.png')
BLACK_ROOF_BACK_LEFT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_back_left_peak_connect.png')
BLACK_ROOF_BACK_MID_PEAK = py.image.load('images\\structures\\roofs\\black_roof_back_mid_peak.png')
BLACK_ROOF_BACK_MID_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_back_mid_peak_connect.png')
BLACK_ROOF_BACK_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\black_roof_back_right_peak.png')
BLACK_ROOF_BACK_RIGHT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\black_roof_back_right_peak_connect.png')
BLACK_ROOF_FRONT_LEFT_PEAK = py.image.load('images\\structures\\roofs\\black_roof_front_left_peak.png')
BLACK_ROOF_FRONT_MID_PEAK = py.image.load('images\\structures\\roofs\\black_roof_front_mid_peak.png')
BLACK_ROOF_FRONT_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\black_roof_front_right_peak.png')
BLACK_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\black_roof_right.png')

RED_ROOF_BACK_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_back_left_connect.png')
RED_ROOF_BACK_MID_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_back_mid_connect.png')
RED_ROOF_BACK_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_back_right_connect.png')
RED_ROOF_FRONT_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_front_left_connect.png')
RED_ROOF_FRONT_MID_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_front_mid_connect.png')
RED_ROOF_FRONT_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_front_right_connect.png')
RED_ROOF_LEFT = py.image.load('images\\structures\\roofs\\red_roof_left.png')
RED_ROOF_MID = py.image.load('images\\structures\\roofs\\red_roof_mid.png')
RED_ROOF_BACK_LEFT_PEAK = py.image.load('images\\structures\\roofs\\red_roof_back_left_peak.png')
RED_ROOF_BACK_LEFT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_back_left_peak_connect.png')
RED_ROOF_BACK_MID_PEAK = py.image.load('images\\structures\\roofs\\red_roof_back_mid_peak.png')
RED_ROOF_BACK_MID_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_back_mid_peak_connect.png')
RED_ROOF_BACK_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\red_roof_back_right_peak.png')
RED_ROOF_BACK_RIGHT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\red_roof_back_right_peak_connect.png')
RED_ROOF_FRONT_LEFT_PEAK = py.image.load('images\\structures\\roofs\\red_roof_front_left_peak.png')
RED_ROOF_FRONT_MID_PEAK = py.image.load('images\\structures\\roofs\\red_roof_front_mid_peak.png')
RED_ROOF_FRONT_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\red_roof_front_right_peak.png')
RED_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\red_roof_right.png')

BLUE_ROOF_BACK_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_back_left_connect.png')
BLUE_ROOF_BACK_MID_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_back_mid_connect.png')
BLUE_ROOF_BACK_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_back_right_connect.png')
BLUE_ROOF_FRONT_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_front_left_connect.png')
BLUE_ROOF_FRONT_MID_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_front_mid_connect.png')
BLUE_ROOF_FRONT_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_front_right_connect.png')
BLUE_ROOF_LEFT = py.image.load('images\\structures\\roofs\\blue_roof_left.png')
BLUE_ROOF_MID = py.image.load('images\\structures\\roofs\\blue_roof_mid.png')
BLUE_ROOF_BACK_LEFT_PEAK = py.image.load('images\\structures\\roofs\\blue_roof_back_left_peak.png')
BLUE_ROOF_BACK_LEFT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_back_left_peak_connect.png')
BLUE_ROOF_BACK_MID_PEAK = py.image.load('images\\structures\\roofs\\blue_roof_back_mid_peak.png')
BLUE_ROOF_BACK_MID_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_back_mid_peak_connect.png')
BLUE_ROOF_BACK_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\blue_roof_back_right_peak.png')
BLUE_ROOF_BACK_RIGHT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\blue_roof_back_right_peak_connect.png')
BLUE_ROOF_FRONT_LEFT_PEAK = py.image.load('images\\structures\\roofs\\blue_roof_front_left_peak.png')
BLUE_ROOF_FRONT_MID_PEAK = py.image.load('images\\structures\\roofs\\blue_roof_front_mid_peak.png')
BLUE_ROOF_FRONT_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\blue_roof_front_right_peak.png')
BLUE_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\blue_roof_right.png')

GREEN_ROOF_BACK_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_back_left_connect.png')
GREEN_ROOF_BACK_MID_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_back_mid_connect.png')
GREEN_ROOF_BACK_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_back_right_connect.png')
GREEN_ROOF_FRONT_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_front_left_connect.png')
GREEN_ROOF_FRONT_MID_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_front_mid_connect.png')
GREEN_ROOF_FRONT_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_front_right_connect.png')
GREEN_ROOF_LEFT = py.image.load('images\\structures\\roofs\\green_roof_left.png')
GREEN_ROOF_MID = py.image.load('images\\structures\\roofs\\green_roof_mid.png')
GREEN_ROOF_BACK_LEFT_PEAK = py.image.load('images\\structures\\roofs\\green_roof_back_left_peak.png')
GREEN_ROOF_BACK_LEFT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_back_left_peak_connect.png')
GREEN_ROOF_BACK_MID_PEAK = py.image.load('images\\structures\\roofs\\green_roof_back_mid_peak.png')
GREEN_ROOF_BACK_MID_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_back_mid_peak_connect.png')
GREEN_ROOF_BACK_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\green_roof_back_right_peak.png')
GREEN_ROOF_BACK_RIGHT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\green_roof_back_right_peak_connect.png')
GREEN_ROOF_FRONT_LEFT_PEAK = py.image.load('images\\structures\\roofs\\green_roof_front_left_peak.png')
GREEN_ROOF_FRONT_MID_PEAK = py.image.load('images\\structures\\roofs\\green_roof_front_mid_peak.png')
GREEN_ROOF_FRONT_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\green_roof_front_right_peak.png')
GREEN_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\green_roof_right.png')

GREY_ROOF_BACK_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_back_left_connect.png')
GREY_ROOF_BACK_MID_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_back_mid_connect.png')
GREY_ROOF_BACK_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_back_right_connect.png')
GREY_ROOF_FRONT_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_front_left_connect.png')
GREY_ROOF_FRONT_MID_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_front_mid_connect.png')
GREY_ROOF_FRONT_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_front_right_connect.png')
GREY_ROOF_LEFT = py.image.load('images\\structures\\roofs\\grey_roof_left.png')
GREY_ROOF_MID = py.image.load('images\\structures\\roofs\\grey_roof_mid.png')
GREY_ROOF_BACK_LEFT_PEAK = py.image.load('images\\structures\\roofs\\grey_roof_back_left_peak.png')
GREY_ROOF_BACK_LEFT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_back_left_peak_connect.png')
GREY_ROOF_BACK_MID_PEAK = py.image.load('images\\structures\\roofs\\grey_roof_back_mid_peak.png')
GREY_ROOF_BACK_MID_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_back_mid_peak_connect.png')
GREY_ROOF_BACK_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\grey_roof_back_right_peak.png')
GREY_ROOF_BACK_RIGHT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\grey_roof_back_right_peak_connect.png')
GREY_ROOF_FRONT_LEFT_PEAK = py.image.load('images\\structures\\roofs\\grey_roof_front_left_peak.png')
GREY_ROOF_FRONT_MID_PEAK = py.image.load('images\\structures\\roofs\\grey_roof_front_mid_peak.png')
GREY_ROOF_FRONT_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\grey_roof_front_right_peak.png')
GREY_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\grey_roof_right.png')

GOLD_ROOF_BACK_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_back_left_connect.png')
GOLD_ROOF_BACK_MID_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_back_mid_connect.png')
GOLD_ROOF_BACK_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_back_right_connect.png')
GOLD_ROOF_FRONT_LEFT_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_front_left_connect.png')
GOLD_ROOF_FRONT_MID_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_front_mid_connect.png')
GOLD_ROOF_FRONT_RIGHT_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_front_right_connect.png')
GOLD_ROOF_LEFT = py.image.load('images\\structures\\roofs\\gold_roof_left.png')
GOLD_ROOF_MID = py.image.load('images\\structures\\roofs\\gold_roof_mid.png')
GOLD_ROOF_BACK_LEFT_PEAK = py.image.load('images\\structures\\roofs\\gold_roof_back_left_peak.png')
GOLD_ROOF_BACK_LEFT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_back_left_peak_connect.png')
GOLD_ROOF_BACK_MID_PEAK = py.image.load('images\\structures\\roofs\\gold_roof_back_mid_peak.png')
GOLD_ROOF_BACK_MID_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_back_mid_peak_connect.png')
GOLD_ROOF_BACK_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\gold_roof_back_right_peak.png')
GOLD_ROOF_BACK_RIGHT_PEAK_CONNECT = py.image.load('images\\structures\\roofs\\gold_roof_back_right_peak_connect.png')
GOLD_ROOF_FRONT_LEFT_PEAK = py.image.load('images\\structures\\roofs\\gold_roof_front_left_peak.png')
GOLD_ROOF_FRONT_MID_PEAK = py.image.load('images\\structures\\roofs\\gold_roof_front_mid_peak.png')
GOLD_ROOF_FRONT_RIGHT_PEAK = py.image.load('images\\structures\\roofs\\gold_roof_front_right_peak.png')
GOLD_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\gold_roof_right.png')

V_RED_ROOF_FRONT_CONNECT0 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect0.png')
V_RED_ROOF_FRONT_CONNECT1 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect1.png')
V_RED_ROOF_FRONT_CONNECT2 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect2.png')
V_RED_ROOF_FRONT_CONNECT3 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect3.png')
V_RED_ROOF_FRONT_CONNECT4 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect4.png')
V_RED_ROOF_FRONT_CONNECT5 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect5.png')
V_RED_ROOF_FRONT_CONNECT6 = py.image.load('images\\structures\\roofs\\v_red_roof_front_connect6.png')
V_RED_ROOF_FRONT_ABOVE0 = py.image.load('images\\structures\\roofs\\v_red_roof_front_above0.png')
V_RED_ROOF_FRONT_ABOVE1 = py.image.load('images\\structures\\roofs\\v_red_roof_front_above1.png')
V_RED_ROOF_FRONT_ABOVE2 = py.image.load('images\\structures\\roofs\\v_red_roof_front_above2.png')
V_RED_ROOF_LEFT = py.image.load('images\\structures\\roofs\\v_red_roof_left.png')
V_RED_ROOF_LEFT_LIGHT = py.image.load('images\\structures\\roofs\\v_red_roof_left_light.png')
V_RED_ROOF_LEFT_DARK = py.image.load('images\\structures\\roofs\\v_red_roof_left_dark.png')
V_RED_ROOF_MID = py.image.load('images\\structures\\roofs\\v_red_roof_mid.png')
V_RED_ROOF_RIGHT_DARK = py.image.load('images\\structures\\roofs\\v_red_roof_right_dark.png')
V_RED_ROOF_RIGHT_LIGHT = py.image.load('images\\structures\\roofs\\v_red_roof_right_light.png')
V_RED_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\v_red_roof_right.png')
V_RED_ROOF_LEFTDOORWAY_BOT = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_bot.png')
V_RED_ROOF_LEFTDOORWAY_MID0 = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_mid0.png')
V_RED_ROOF_LEFTDOORWAY_MID1 = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_mid1.png')
V_RED_ROOF_LEFTDOORWAY_MID2 = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_mid2.png')
V_RED_ROOF_LEFTDOORWAY_TOP0 = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_top0.png')
V_RED_ROOF_LEFTDOORWAY_TOP1 = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_top1.png')
V_RED_ROOF_LEFTDOORWAY_TOP2 = py.image.load('images\\structures\\roofs\\v_red_roof_leftdoorway_top2.png')
V_RED_ROOF_TOP0 = py.image.load('images\\structures\\roofs\\v_red_roof_top0.png')
V_RED_ROOF_TOP1 = py.image.load('images\\structures\\roofs\\v_red_roof_top1.png')
V_RED_ROOF_TOP2 = py.image.load('images\\structures\\roofs\\v_red_roof_top2.png')
V_RED_ROOF_TOP3 = py.image.load('images\\structures\\roofs\\v_red_roof_top3.png')
V_RED_ROOF_TOP4 = py.image.load('images\\structures\\roofs\\v_red_roof_top4.png')
V_RED_ROOF_TOP5 = py.image.load('images\\structures\\roofs\\v_red_roof_top5.png')
V_RED_ROOF_TOP6 = py.image.load('images\\structures\\roofs\\v_red_roof_top6.png')
V_RED_ROOF_TIPTOP_LEFT = py.image.load('images\\structures\\roofs\\v_red_roof_tiptop_left.png')
V_RED_ROOF_TIPTOP_MID = py.image.load('images\\structures\\roofs\\v_red_roof_tiptop_mid.png')
V_RED_ROOF_TIPTOP_RIGHT = py.image.load('images\\structures\\roofs\\v_red_roof_tiptop_right.png')

V_GREY_ROOF_FRONT_CONNECT0 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect0.png')
V_GREY_ROOF_FRONT_CONNECT1 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect1.png')
V_GREY_ROOF_FRONT_CONNECT2 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect2.png')
V_GREY_ROOF_FRONT_CONNECT3 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect3.png')
V_GREY_ROOF_FRONT_CONNECT4 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect4.png')
V_GREY_ROOF_FRONT_CONNECT5 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect5.png')
V_GREY_ROOF_FRONT_CONNECT6 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_connect6.png')
V_GREY_ROOF_FRONT_ABOVE0 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_above0.png')
V_GREY_ROOF_FRONT_ABOVE1 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_above1.png')
V_GREY_ROOF_FRONT_ABOVE2 = py.image.load('images\\structures\\roofs\\v_grey_roof_front_above2.png')
V_GREY_ROOF_LEFT = py.image.load('images\\structures\\roofs\\v_grey_roof_left.png')
V_GREY_ROOF_LEFT_LIGHT = py.image.load('images\\structures\\roofs\\v_grey_roof_left_light.png')
V_GREY_ROOF_LEFT_DARK = py.image.load('images\\structures\\roofs\\v_grey_roof_left_dark.png')
V_GREY_ROOF_MID = py.image.load('images\\structures\\roofs\\v_grey_roof_mid.png')
V_GREY_ROOF_RIGHT_DARK = py.image.load('images\\structures\\roofs\\v_grey_roof_right_dark.png')
V_GREY_ROOF_RIGHT_LIGHT = py.image.load('images\\structures\\roofs\\v_grey_roof_right_light.png')
V_GREY_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\v_grey_roof_right.png')
V_GREY_ROOF_LEFTDOORWAY_BOT = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_bot.png')
V_GREY_ROOF_LEFTDOORWAY_MID0 = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_mid0.png')
V_GREY_ROOF_LEFTDOORWAY_MID1 = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_mid1.png')
V_GREY_ROOF_LEFTDOORWAY_MID2 = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_mid2.png')
V_GREY_ROOF_LEFTDOORWAY_TOP0 = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_top0.png')
V_GREY_ROOF_LEFTDOORWAY_TOP1 = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_top1.png')
V_GREY_ROOF_LEFTDOORWAY_TOP2 = py.image.load('images\\structures\\roofs\\v_grey_roof_leftdoorway_top2.png')
V_GREY_ROOF_RIGHTDOORWAY_BOT = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_bot.png')
V_GREY_ROOF_RIGHTDOORWAY_MID0 = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_mid0.png')
V_GREY_ROOF_RIGHTDOORWAY_MID1 = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_mid1.png')
V_GREY_ROOF_RIGHTDOORWAY_MID2 = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_mid2.png')
V_GREY_ROOF_RIGHTDOORWAY_TOP0 = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_top0.png')
V_GREY_ROOF_RIGHTDOORWAY_TOP1 = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_top1.png')
V_GREY_ROOF_RIGHTDOORWAY_TOP2 = py.image.load('images\\structures\\roofs\\v_grey_roof_rightdoorway_top2.png')
V_GREY_ROOF_TOP0 = py.image.load('images\\structures\\roofs\\v_grey_roof_top0.png')
V_GREY_ROOF_TOP1 = py.image.load('images\\structures\\roofs\\v_grey_roof_top1.png')
V_GREY_ROOF_TOP2 = py.image.load('images\\structures\\roofs\\v_grey_roof_top2.png')
V_GREY_ROOF_TOP3 = py.image.load('images\\structures\\roofs\\v_grey_roof_top3.png')
V_GREY_ROOF_TOP4 = py.image.load('images\\structures\\roofs\\v_grey_roof_top4.png')
V_GREY_ROOF_TOP5 = py.image.load('images\\structures\\roofs\\v_grey_roof_top5.png')
V_GREY_ROOF_TOP6 = py.image.load('images\\structures\\roofs\\v_grey_roof_top6.png')
V_GREY_ROOF_TIPTOP_LEFT = py.image.load('images\\structures\\roofs\\v_grey_roof_tiptop_left.png')
V_GREY_ROOF_TIPTOP_MID = py.image.load('images\\structures\\roofs\\v_grey_roof_tiptop_mid.png')
V_GREY_ROOF_TIPTOP_RIGHT = py.image.load('images\\structures\\roofs\\v_grey_roof_tiptop_right.png')
V_GREY_ROOF_DOWNUP_CONNECT = py.image.load('images\\structures\\roofs\\v_grey_roof_downup_connect.png')
V_GREY_ROOF_DOWNUP = py.image.load('images\\structures\\roofs\\v_grey_roof_downup.png')
V_GREY_ROOF_DOWNUP_TOP = py.image.load('images\\structures\\roofs\\v_grey_roof_downup_top.png')

V_GOLD_ROOF_FRONT_CONNECT0 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect0.png')
V_GOLD_ROOF_FRONT_CONNECT1 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect1.png')
V_GOLD_ROOF_FRONT_CONNECT2 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect2.png')
V_GOLD_ROOF_FRONT_CONNECT3 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect3.png')
V_GOLD_ROOF_FRONT_CONNECT4 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect4.png')
V_GOLD_ROOF_FRONT_CONNECT5 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect5.png')
V_GOLD_ROOF_FRONT_CONNECT6 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_connect6.png')
V_GOLD_ROOF_FRONT_ABOVE0 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_above0.png')
V_GOLD_ROOF_FRONT_ABOVE1 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_above1.png')
V_GOLD_ROOF_FRONT_ABOVE2 = py.image.load('images\\structures\\roofs\\V_gold_roof_front_above2.png')
V_GOLD_ROOF_LEFT = py.image.load('images\\structures\\roofs\\V_gold_roof_left.png')
V_GOLD_ROOF_LEFT_LIGHT = py.image.load('images\\structures\\roofs\\V_gold_roof_left_light.png')
V_GOLD_ROOF_LEFT_DARK = py.image.load('images\\structures\\roofs\\V_gold_roof_left_dark.png')
V_GOLD_ROOF_MID = py.image.load('images\\structures\\roofs\\V_gold_roof_mid.png')
V_GOLD_ROOF_RIGHT_DARK = py.image.load('images\\structures\\roofs\\V_gold_roof_right_dark.png')
V_GOLD_ROOF_RIGHT_LIGHT = py.image.load('images\\structures\\roofs\\V_gold_roof_right_light.png')
V_GOLD_ROOF_RIGHT = py.image.load('images\\structures\\roofs\\V_gold_roof_right.png')
V_GOLD_ROOF_LEFTDOORWAY_BOT = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_bot.png')
V_GOLD_ROOF_LEFTDOORWAY_MID0 = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_mid0.png')
V_GOLD_ROOF_LEFTDOORWAY_MID1 = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_mid1.png')
V_GOLD_ROOF_LEFTDOORWAY_MID2 = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_mid2.png')
V_GOLD_ROOF_LEFTDOORWAY_TOP0 = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_top0.png')
V_GOLD_ROOF_LEFTDOORWAY_TOP1 = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_top1.png')
V_GOLD_ROOF_LEFTDOORWAY_TOP2 = py.image.load('images\\structures\\roofs\\V_gold_roof_leftdoorway_top2.png')
V_GOLD_ROOF_TOP0 = py.image.load('images\\structures\\roofs\\V_gold_roof_top0.png')
V_GOLD_ROOF_TOP1 = py.image.load('images\\structures\\roofs\\V_gold_roof_top1.png')
V_GOLD_ROOF_TOP2 = py.image.load('images\\structures\\roofs\\V_gold_roof_top2.png')
V_GOLD_ROOF_TOP3 = py.image.load('images\\structures\\roofs\\V_gold_roof_top3.png')
V_GOLD_ROOF_TOP4 = py.image.load('images\\structures\\roofs\\V_gold_roof_top4.png')
V_GOLD_ROOF_TOP5 = py.image.load('images\\structures\\roofs\\V_gold_roof_top5.png')
V_GOLD_ROOF_TOP6 = py.image.load('images\\structures\\roofs\\V_gold_roof_top6.png')
V_GOLD_ROOF_TIPTOP_LEFT = py.image.load('images\\structures\\roofs\\V_gold_roof_tiptop_left.png')
V_GOLD_ROOF_TIPTOP_MID = py.image.load('images\\structures\\roofs\\V_gold_roof_tiptop_mid.png')
V_GOLD_ROOF_TIPTOP_RIGHT = py.image.load('images\\structures\\roofs\\V_gold_roof_tiptop_right.png')