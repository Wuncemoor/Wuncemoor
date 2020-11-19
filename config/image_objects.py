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

BUNDLE_HERO = ImageBundle(py.image.load('images\\entities\\combatants\\hero\\sprite.png'),
                          py.image.load('images\\entities\\combatants\\hero\\portrait.png'),
                          py.image.load('images\\entities\\combatants\\hero\\port_mini.png'),
                          py.image.load('images\\entities\\combatants\\hero\\actor.png'))

BUNDLE_SAMWISE = ImageBundle(py.image.load('images\\entities\\noncombatants\\samwise\\sprite.png'),
                             py.image.load('images\\entities\\noncombatants\\samwise\\portrait.png'),
                             py.image.load('images\\entities\\noncombatants\\samwise\\port_mini.png'))

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
}

WALL_TOP_H = FrozenSurface.load('images\\structures\\inn\\', 'wall_top_h.png')
WALL_TOP_V = FrozenSurface.load('images\\structures\\inn\\', 'wall_top_v.png')
WALL_MID = FrozenSurface.load('images\\structures\\inn\\', 'wall_mid.png')
WALL_BOT = FrozenSurface.load('images\\structures\\inn\\', 'wall_bot.png')
PILLAR_TOP = FrozenSurface.load('images\\structures\\inn\\', 'pillar_top.png')
PILLAR_MID = FrozenSurface.load('images\\structures\\inn\\', 'pillar_mid.png')
PILLAR_BOT = FrozenSurface.load('images\\structures\\inn\\', 'pillar_bot.png')
INN_FLOOR_S = FrozenSurface.load('images\\structures\\inn\\', 'inn_floor_s.png')

OVERWORLD_TOWN = [[py.image.load('images\\tiles\\overworld\\town\\town0.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town1.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town2.png')],
                  [py.image.load('images\\tiles\\overworld\\town\\town3.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town4.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town5.png')],
                  [py.image.load('images\\tiles\\overworld\\town\\town6.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town7.png'),
                   py.image.load('images\\tiles\\overworld\\town\\town8.png')]]


EXT_LEFT_EDGE_BOT = py.image.load('images\\structures\\mage_house\\ext_left_edge_bot.png')
EXT_LEFT_EDGE_TOP = py.image.load('images\\structures\\mage_house\\ext_left_edge_top.png')
EXT_EXTEND_BOT = py.image.load('images\\structures\\mage_house\\ext_extend_bot.png')
EXT_EXTEND_TOP = py.image.load('images\\structures\\mage_house\\ext_extend_top.png')
EXT_LEFT_DOORFRAME_BOT = py.image.load('images\\structures\\mage_house\\ext_left_doorframe_bot.png')
EXT_LEFT_DOORFRAME_TOP = py.image.load('images\\structures\\mage_house\\ext_left_doorframe_top.png')
EXT_DOORWAY_BOT = py.image.load('images\\structures\\mage_house\\ext_doorway_bot.png')
EXT_DOORWAY_TOP = py.image.load('images\\structures\\mage_house\\ext_doorway_top.png')
EXT_RIGHT_DOORFRAME_BOT = py.image.load('images\\structures\\mage_house\\ext_right_doorframe_bot.png')
EXT_RIGHT_DOORFRAME_TOP = py.image.load('images\\structures\\mage_house\\ext_right_doorframe_top.png')
EXT_WINDOW_LEFT_BOT = py.image.load('images\\structures\\mage_house\\ext_window_left_bot.png')
EXT_WINDOW_LEFT_TOP = py.image.load('images\\structures\\mage_house\\ext_window_left_top.png')
EXT_WINDOW_RIGHT_BOT = py.image.load('images\\structures\\mage_house\\ext_window_right_bot.png')
EXT_WINDOW_RIGHT_TOP = py.image.load('images\\structures\\mage_house\\ext_window_right_top.png')
EXT_RIGHT_EDGE_BOT = py.image.load('images\\structures\\mage_house\\ext_right_edge_bot.png')
EXT_RIGHT_EDGE_TOP = py.image.load('images\\structures\\mage_house\\ext_right_edge_top.png')

BLUE_ROOF_LEFT_CONNECT = py.image.load('images\\structures\\mage_house\\blue_roof_left_connect.png')
BLUE_ROOF_MID_CONNECT = py.image.load('images\\structures\\mage_house\\blue_roof_mid_connect.png')