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
    'current': py.image.load('images\\GUI\\journal\\current.png'),
    'text0': py.image.load('images\\GUI\\journal\\current_text.png'),
    'completed': py.image.load('images\\GUI\\journal\\completed.png'),
    'text1': py.image.load('images\\GUI\\journal\\completed_text.png'),
    'codex': py.image.load('images\\GUI\\journal\\codex.png'),
    'text2': py.image.load('images\\GUI\\journal\\codex_text.png'),
    'history': py.image.load('images\\GUI\\journal\\history.png'),
    'text3': py.image.load('images\\GUI\\journal\\history_text.png'),
    'selected_icon': py.image.load('images\\GUI\\journal\\selected_icon.png'),
    'selected_quest': py.image.load('images\\GUI\\journal\\selected_quest.png'),
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

SAMWISE_DOWN0 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_00.png')
SAMWISE_DOWN1 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_01.png')
SAMWISE_DOWN2 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_02.png')
SAMWISE_LEFT0 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_03.png')
SAMWISE_LEFT1 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_04.png')
SAMWISE_LEFT2 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_05.png')
SAMWISE_RIGHT0 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_06.png')
SAMWISE_RIGHT1 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_07.png')
SAMWISE_RIGHT2 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_08.png')
SAMWISE_UP0 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_09.png')
SAMWISE_UP1 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_10.png')
SAMWISE_UP2 = py.image.load('images\\entities\\noncombatants\\samwise\\sprite_11.png')
SAMWISE_PORTRAIT = py.image.load('images\\entities\\noncombatants\\samwise\\portrait.png')
SAMWISE_PORTMINI = py.image.load('images\\entities\\noncombatants\\samwise\\port_mini.png')
SAMWISE_ACTOR = None

SAMWISE_SPRITE_DICT = {(0, 1): [SAMWISE_DOWN0, SAMWISE_DOWN0, SAMWISE_DOWN0, SAMWISE_DOWN1, SAMWISE_DOWN1, SAMWISE_DOWN1, SAMWISE_DOWN2, SAMWISE_DOWN2, SAMWISE_DOWN2, SAMWISE_DOWN1, SAMWISE_DOWN1, SAMWISE_DOWN1],
                       (0, -1): [SAMWISE_UP0, SAMWISE_UP0, SAMWISE_UP0, SAMWISE_UP1, SAMWISE_UP1, SAMWISE_UP1, SAMWISE_UP2, SAMWISE_UP2, SAMWISE_UP2,SAMWISE_UP1, SAMWISE_UP1, SAMWISE_UP1],
                       (-1, 0): [SAMWISE_LEFT0, SAMWISE_LEFT0, SAMWISE_LEFT0, SAMWISE_LEFT1, SAMWISE_LEFT1, SAMWISE_LEFT1, SAMWISE_LEFT2, SAMWISE_LEFT2, SAMWISE_LEFT2, SAMWISE_LEFT1, SAMWISE_LEFT1, SAMWISE_LEFT1],
                       (1, 0): [SAMWISE_RIGHT0, SAMWISE_RIGHT0, SAMWISE_RIGHT0, SAMWISE_RIGHT1, SAMWISE_RIGHT1, SAMWISE_RIGHT1, SAMWISE_RIGHT2, SAMWISE_RIGHT2, SAMWISE_RIGHT2, SAMWISE_RIGHT1, SAMWISE_RIGHT1, SAMWISE_RIGHT1],}

BUNDLE_SAMWISE = ImageBundle(SAMWISE_SPRITE_DICT,
                             SAMWISE_SPRITE_DICT.get((0, 1)),
                             SAMWISE_PORTRAIT,
                             SAMWISE_PORTMINI,
                             SAMWISE_ACTOR)

MAGE_DOWN0 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_00.png')
MAGE_DOWN1 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_01.png')
MAGE_DOWN2 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_02.png')
MAGE_LEFT0 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_03.png')
MAGE_LEFT1 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_04.png')
MAGE_LEFT2 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_05.png')
MAGE_RIGHT0 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_06.png')
MAGE_RIGHT1 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_07.png')
MAGE_RIGHT2 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_08.png')
MAGE_UP0 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_09.png')
MAGE_UP1 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_10.png')
MAGE_UP2 = py.image.load('images\\entities\\noncombatants\\mage\\sprite_11.png')
MAGE_PORTRAIT = py.image.load('images\\entities\\noncombatants\\mage\\portrait.png')
MAGE_PORTMINI = py.image.load('images\\entities\\noncombatants\\mage\\port_mini.png')
MAGE_ACTOR = None

MAGE_SPRITE_DICT = {(0, 1): [MAGE_DOWN0, MAGE_DOWN0, MAGE_DOWN0, MAGE_DOWN1, MAGE_DOWN1, MAGE_DOWN1, MAGE_DOWN2, MAGE_DOWN2, MAGE_DOWN2, MAGE_DOWN1, MAGE_DOWN1, MAGE_DOWN1],
                       (0, -1): [MAGE_UP0, MAGE_UP0, MAGE_UP0, MAGE_UP1, MAGE_UP1, MAGE_UP1, MAGE_UP2, MAGE_UP2, MAGE_UP2,MAGE_UP1, MAGE_UP1, MAGE_UP1],
                       (-1, 0): [MAGE_LEFT0, MAGE_LEFT0, MAGE_LEFT0, MAGE_LEFT1, MAGE_LEFT1, MAGE_LEFT1, MAGE_LEFT2, MAGE_LEFT2, MAGE_LEFT2, MAGE_LEFT1, MAGE_LEFT1, MAGE_LEFT1],
                       (1, 0): [MAGE_RIGHT0, MAGE_RIGHT0, MAGE_RIGHT0, MAGE_RIGHT1, MAGE_RIGHT1, MAGE_RIGHT1, MAGE_RIGHT2, MAGE_RIGHT2, MAGE_RIGHT2, MAGE_RIGHT1, MAGE_RIGHT1, MAGE_RIGHT1],}

BUNDLE_MAGE = ImageBundle(MAGE_SPRITE_DICT,
                          MAGE_SPRITE_DICT.get((0, 1)),
                          MAGE_PORTRAIT,
                          MAGE_PORTMINI,
                          MAGE_ACTOR)

GUARD_CAPTAIN_DOWN0 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_00.png')
GUARD_CAPTAIN_DOWN1 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_01.png')
GUARD_CAPTAIN_DOWN2 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_02.png')
GUARD_CAPTAIN_LEFT0 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_03.png')
GUARD_CAPTAIN_LEFT1 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_04.png')
GUARD_CAPTAIN_LEFT2 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_05.png')
GUARD_CAPTAIN_RIGHT0 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_06.png')
GUARD_CAPTAIN_RIGHT1 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_07.png')
GUARD_CAPTAIN_RIGHT2 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_08.png')
GUARD_CAPTAIN_UP0 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_09.png')
GUARD_CAPTAIN_UP1 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_10.png')
GUARD_CAPTAIN_UP2 = py.image.load('images\\entities\\noncombatants\\guard_captain\\sprite_11.png')
GUARD_CAPTAIN_PORTRAIT = py.image.load('images\\entities\\noncombatants\\guard_captain\\portrait.png')
GUARD_CAPTAIN_PORTMINI = py.image.load('images\\entities\\noncombatants\\guard_captain\\port_mini.png')
GUARD_CAPTAIN_ACTOR = None

GUARD_CAPTAIN_SPRITE_DICT = {(0, 1): [GUARD_CAPTAIN_DOWN0, GUARD_CAPTAIN_DOWN0, GUARD_CAPTAIN_DOWN0, GUARD_CAPTAIN_DOWN1, GUARD_CAPTAIN_DOWN1, GUARD_CAPTAIN_DOWN1, GUARD_CAPTAIN_DOWN2, GUARD_CAPTAIN_DOWN2, GUARD_CAPTAIN_DOWN2, GUARD_CAPTAIN_DOWN1, GUARD_CAPTAIN_DOWN1, GUARD_CAPTAIN_DOWN1],
                       (0, -1): [GUARD_CAPTAIN_UP0, GUARD_CAPTAIN_UP0, GUARD_CAPTAIN_UP0, GUARD_CAPTAIN_UP1, GUARD_CAPTAIN_UP1, GUARD_CAPTAIN_UP1, GUARD_CAPTAIN_UP2, GUARD_CAPTAIN_UP2, GUARD_CAPTAIN_UP2,GUARD_CAPTAIN_UP1, GUARD_CAPTAIN_UP1, GUARD_CAPTAIN_UP1],
                       (-1, 0): [GUARD_CAPTAIN_LEFT0, GUARD_CAPTAIN_LEFT0, GUARD_CAPTAIN_LEFT0, GUARD_CAPTAIN_LEFT1, GUARD_CAPTAIN_LEFT1, GUARD_CAPTAIN_LEFT1, GUARD_CAPTAIN_LEFT2, GUARD_CAPTAIN_LEFT2, GUARD_CAPTAIN_LEFT2, GUARD_CAPTAIN_LEFT1, GUARD_CAPTAIN_LEFT1, GUARD_CAPTAIN_LEFT1],
                       (1, 0): [GUARD_CAPTAIN_RIGHT0, GUARD_CAPTAIN_RIGHT0, GUARD_CAPTAIN_RIGHT0, GUARD_CAPTAIN_RIGHT1, GUARD_CAPTAIN_RIGHT1, GUARD_CAPTAIN_RIGHT1, GUARD_CAPTAIN_RIGHT2, GUARD_CAPTAIN_RIGHT2, GUARD_CAPTAIN_RIGHT2, GUARD_CAPTAIN_RIGHT1, GUARD_CAPTAIN_RIGHT1, GUARD_CAPTAIN_RIGHT1],}

BUNDLE_GUARD_CAPTAIN = ImageBundle(GUARD_CAPTAIN_SPRITE_DICT,
                          GUARD_CAPTAIN_SPRITE_DICT.get((0, 1)),
                          GUARD_CAPTAIN_PORTRAIT,
                          GUARD_CAPTAIN_PORTMINI,
                          GUARD_CAPTAIN_ACTOR)

PRIEST_DOWN0 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_00.png')
PRIEST_DOWN1 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_01.png')
PRIEST_DOWN2 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_02.png')
PRIEST_LEFT0 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_03.png')
PRIEST_LEFT1 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_04.png')
PRIEST_LEFT2 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_05.png')
PRIEST_RIGHT0 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_06.png')
PRIEST_RIGHT1 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_07.png')
PRIEST_RIGHT2 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_08.png')
PRIEST_UP0 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_09.png')
PRIEST_UP1 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_10.png')
PRIEST_UP2 = py.image.load('images\\entities\\noncombatants\\priest\\sprite_11.png')
PRIEST_PORTRAIT = py.image.load('images\\entities\\noncombatants\\priest\\portrait.png')
PRIEST_PORTMINI = py.image.load('images\\entities\\noncombatants\\priest\\port_mini.png')
PRIEST_ACTOR = None

PRIEST_SPRITE_DICT = {(0, 1): [PRIEST_DOWN0, PRIEST_DOWN0, PRIEST_DOWN0, PRIEST_DOWN1, PRIEST_DOWN1, PRIEST_DOWN1, PRIEST_DOWN2, PRIEST_DOWN2, PRIEST_DOWN2, PRIEST_DOWN1, PRIEST_DOWN1, PRIEST_DOWN1],
                       (0, -1): [PRIEST_UP0, PRIEST_UP0, PRIEST_UP0, PRIEST_UP1, PRIEST_UP1, PRIEST_UP1, PRIEST_UP2, PRIEST_UP2, PRIEST_UP2,PRIEST_UP1, PRIEST_UP1, PRIEST_UP1],
                       (-1, 0): [PRIEST_LEFT0, PRIEST_LEFT0, PRIEST_LEFT0, PRIEST_LEFT1, PRIEST_LEFT1, PRIEST_LEFT1, PRIEST_LEFT2, PRIEST_LEFT2, PRIEST_LEFT2, PRIEST_LEFT1, PRIEST_LEFT1, PRIEST_LEFT1],
                       (1, 0): [PRIEST_RIGHT0, PRIEST_RIGHT0, PRIEST_RIGHT0, PRIEST_RIGHT1, PRIEST_RIGHT1, PRIEST_RIGHT1, PRIEST_RIGHT2, PRIEST_RIGHT2, PRIEST_RIGHT2, PRIEST_RIGHT1, PRIEST_RIGHT1, PRIEST_RIGHT1],}

BUNDLE_PRIEST = ImageBundle(PRIEST_SPRITE_DICT,
                          PRIEST_SPRITE_DICT.get((0, 1)),
                          PRIEST_PORTRAIT,
                          PRIEST_PORTMINI,
                          PRIEST_ACTOR)

ROGUE_DOWN0 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_00.png')
ROGUE_DOWN1 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_01.png')
ROGUE_DOWN2 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_02.png')
ROGUE_LEFT0 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_03.png')
ROGUE_LEFT1 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_04.png')
ROGUE_LEFT2 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_05.png')
ROGUE_RIGHT0 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_06.png')
ROGUE_RIGHT1 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_07.png')
ROGUE_RIGHT2 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_08.png')
ROGUE_UP0 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_09.png')
ROGUE_UP1 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_10.png')
ROGUE_UP2 = py.image.load('images\\entities\\noncombatants\\rogue\\sprite_11.png')
ROGUE_PORTRAIT = py.image.load('images\\entities\\noncombatants\\rogue\\portrait.png')
ROGUE_PORTMINI = py.image.load('images\\entities\\noncombatants\\rogue\\port_mini.png')
ROGUE_ACTOR = None

ROGUE_SPRITE_DICT = {(0, 1): [ROGUE_DOWN0, ROGUE_DOWN0, ROGUE_DOWN0, ROGUE_DOWN1, ROGUE_DOWN1, ROGUE_DOWN1, ROGUE_DOWN2, ROGUE_DOWN2, ROGUE_DOWN2, ROGUE_DOWN1, ROGUE_DOWN1, ROGUE_DOWN1],
                       (0, -1): [ROGUE_UP0, ROGUE_UP0, ROGUE_UP0, ROGUE_UP1, ROGUE_UP1, ROGUE_UP1, ROGUE_UP2, ROGUE_UP2, ROGUE_UP2,ROGUE_UP1, ROGUE_UP1, ROGUE_UP1],
                       (-1, 0): [ROGUE_LEFT0, ROGUE_LEFT0, ROGUE_LEFT0, ROGUE_LEFT1, ROGUE_LEFT1, ROGUE_LEFT1, ROGUE_LEFT2, ROGUE_LEFT2, ROGUE_LEFT2, ROGUE_LEFT1, ROGUE_LEFT1, ROGUE_LEFT1],
                       (1, 0): [ROGUE_RIGHT0, ROGUE_RIGHT0, ROGUE_RIGHT0, ROGUE_RIGHT1, ROGUE_RIGHT1, ROGUE_RIGHT1, ROGUE_RIGHT2, ROGUE_RIGHT2, ROGUE_RIGHT2, ROGUE_RIGHT1, ROGUE_RIGHT1, ROGUE_RIGHT1],}

BUNDLE_ROGUE = ImageBundle(ROGUE_SPRITE_DICT,
                          ROGUE_SPRITE_DICT.get((0, 1)),
                          ROGUE_PORTRAIT,
                          ROGUE_PORTMINI,
                          ROGUE_ACTOR)

HOMER_DOWN0 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_00.png')
HOMER_DOWN1 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_01.png')
HOMER_DOWN2 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_02.png')
HOMER_LEFT0 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_03.png')
HOMER_LEFT1 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_04.png')
HOMER_LEFT2 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_05.png')
HOMER_RIGHT0 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_06.png')
HOMER_RIGHT1 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_07.png')
HOMER_RIGHT2 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_08.png')
HOMER_UP0 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_09.png')
HOMER_UP1 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_10.png')
HOMER_UP2 = py.image.load('images\\entities\\noncombatants\\homer\\sprite_11.png')
HOMER_PORTRAIT = py.image.load('images\\entities\\noncombatants\\homer\\portrait.png')
HOMER_PORTMINI = py.image.load('images\\entities\\noncombatants\\homer\\port_mini.png')
HOMER_ACTOR = None

HOMER_SPRITE_DICT = {(0, 1): [HOMER_DOWN0, HOMER_DOWN0, HOMER_DOWN0, HOMER_DOWN1, HOMER_DOWN1, HOMER_DOWN1, HOMER_DOWN2, HOMER_DOWN2, HOMER_DOWN2, HOMER_DOWN1, HOMER_DOWN1, HOMER_DOWN1],
                       (0, -1): [HOMER_UP0, HOMER_UP0, HOMER_UP0, HOMER_UP1, HOMER_UP1, HOMER_UP1, HOMER_UP2, HOMER_UP2, HOMER_UP2,HOMER_UP1, HOMER_UP1, HOMER_UP1],
                       (-1, 0): [HOMER_LEFT0, HOMER_LEFT0, HOMER_LEFT0, HOMER_LEFT1, HOMER_LEFT1, HOMER_LEFT1, HOMER_LEFT2, HOMER_LEFT2, HOMER_LEFT2, HOMER_LEFT1, HOMER_LEFT1, HOMER_LEFT1],
                       (1, 0): [HOMER_RIGHT0, HOMER_RIGHT0, HOMER_RIGHT0, HOMER_RIGHT1, HOMER_RIGHT1, HOMER_RIGHT1, HOMER_RIGHT2, HOMER_RIGHT2, HOMER_RIGHT2, HOMER_RIGHT1, HOMER_RIGHT1, HOMER_RIGHT1],}

BUNDLE_HOMER = ImageBundle(HOMER_SPRITE_DICT, HOMER_SPRITE_DICT.get((0, 1)), HOMER_PORTRAIT, HOMER_PORTMINI, HOMER_ACTOR)

MAYOR_DOWN0 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_00.png')
MAYOR_DOWN1 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_01.png')
MAYOR_DOWN2 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_02.png')
MAYOR_LEFT0 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_03.png')
MAYOR_LEFT1 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_04.png')
MAYOR_LEFT2 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_05.png')
MAYOR_RIGHT0 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_06.png')
MAYOR_RIGHT1 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_07.png')
MAYOR_RIGHT2 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_08.png')
MAYOR_UP0 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_09.png')
MAYOR_UP1 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_10.png')
MAYOR_UP2 = py.image.load('images\\entities\\noncombatants\\mayor\\sprite_11.png')
MAYOR_PORTRAIT = py.image.load('images\\entities\\noncombatants\\mayor\\portrait.png')
MAYOR_PORTMINI = py.image.load('images\\entities\\noncombatants\\mayor\\port_mini.png')
MAYOR_ACTOR = None

MAYOR_SPRITE_DICT = {(0, 1): [MAYOR_DOWN0, MAYOR_DOWN0, MAYOR_DOWN0, MAYOR_DOWN1, MAYOR_DOWN1, MAYOR_DOWN1, MAYOR_DOWN2, MAYOR_DOWN2, MAYOR_DOWN2, MAYOR_DOWN1, MAYOR_DOWN1, MAYOR_DOWN1],
                       (0, -1): [MAYOR_UP0, MAYOR_UP0, MAYOR_UP0, MAYOR_UP1, MAYOR_UP1, MAYOR_UP1, MAYOR_UP2, MAYOR_UP2, MAYOR_UP2,MAYOR_UP1, MAYOR_UP1, MAYOR_UP1],
                       (-1, 0): [MAYOR_LEFT0, MAYOR_LEFT0, MAYOR_LEFT0, MAYOR_LEFT1, MAYOR_LEFT1, MAYOR_LEFT1, MAYOR_LEFT2, MAYOR_LEFT2, MAYOR_LEFT2, MAYOR_LEFT1, MAYOR_LEFT1, MAYOR_LEFT1],
                       (1, 0): [MAYOR_RIGHT0, MAYOR_RIGHT0, MAYOR_RIGHT0, MAYOR_RIGHT1, MAYOR_RIGHT1, MAYOR_RIGHT1, MAYOR_RIGHT2, MAYOR_RIGHT2, MAYOR_RIGHT2, MAYOR_RIGHT1, MAYOR_RIGHT1, MAYOR_RIGHT1],}

BUNDLE_MAYOR = ImageBundle(MAYOR_SPRITE_DICT,
                          MAYOR_SPRITE_DICT.get((0, 1)),
                          MAYOR_PORTRAIT,
                          MAYOR_PORTMINI,
                          MAYOR_ACTOR)

INNKEEPER_DOWN0 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_00.png')
INNKEEPER_DOWN1 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_01.png')
INNKEEPER_DOWN2 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_02.png')
INNKEEPER_LEFT0 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_03.png')
INNKEEPER_LEFT1 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_04.png')
INNKEEPER_LEFT2 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_05.png')
INNKEEPER_RIGHT0 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_06.png')
INNKEEPER_RIGHT1 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_07.png')
INNKEEPER_RIGHT2 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_08.png')
INNKEEPER_UP0 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_09.png')
INNKEEPER_UP1 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_10.png')
INNKEEPER_UP2 = py.image.load('images\\entities\\noncombatants\\innkeeper\\sprite_11.png')
INNKEEPER_PORTRAIT = py.image.load('images\\entities\\noncombatants\\innkeeper\\portrait.png')
INNKEEPER_PORTMINI = py.image.load('images\\entities\\noncombatants\\innkeeper\\port_mini.png')
INNKEEPER_ACTOR = None

INNKEEPER_SPRITE_DICT = {(0, 1): [INNKEEPER_DOWN0, INNKEEPER_DOWN0, INNKEEPER_DOWN0, INNKEEPER_DOWN1, INNKEEPER_DOWN1, INNKEEPER_DOWN1, INNKEEPER_DOWN2, INNKEEPER_DOWN2, INNKEEPER_DOWN2, INNKEEPER_DOWN1, INNKEEPER_DOWN1, INNKEEPER_DOWN1],
                       (0, -1): [INNKEEPER_UP0, INNKEEPER_UP0, INNKEEPER_UP0, INNKEEPER_UP1, INNKEEPER_UP1, INNKEEPER_UP1, INNKEEPER_UP2, INNKEEPER_UP2, INNKEEPER_UP2,INNKEEPER_UP1, INNKEEPER_UP1, INNKEEPER_UP1],
                       (-1, 0): [INNKEEPER_LEFT0, INNKEEPER_LEFT0, INNKEEPER_LEFT0, INNKEEPER_LEFT1, INNKEEPER_LEFT1, INNKEEPER_LEFT1, INNKEEPER_LEFT2, INNKEEPER_LEFT2, INNKEEPER_LEFT2, INNKEEPER_LEFT1, INNKEEPER_LEFT1, INNKEEPER_LEFT1],
                       (1, 0): [INNKEEPER_RIGHT0, INNKEEPER_RIGHT0, INNKEEPER_RIGHT0, INNKEEPER_RIGHT1, INNKEEPER_RIGHT1, INNKEEPER_RIGHT1, INNKEEPER_RIGHT2, INNKEEPER_RIGHT2, INNKEEPER_RIGHT2, INNKEEPER_RIGHT1, INNKEEPER_RIGHT1, INNKEEPER_RIGHT1],}

BUNDLE_INNKEEPER = ImageBundle(INNKEEPER_SPRITE_DICT,
                          INNKEEPER_SPRITE_DICT.get((0, 1)),
                          INNKEEPER_PORTRAIT,
                          INNKEEPER_PORTMINI,
                          INNKEEPER_ACTOR)

TAVERNKEEPER_DOWN0 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_00.png')
TAVERNKEEPER_DOWN1 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_01.png')
TAVERNKEEPER_DOWN2 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_02.png')
TAVERNKEEPER_LEFT0 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_03.png')
TAVERNKEEPER_LEFT1 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_04.png')
TAVERNKEEPER_LEFT2 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_05.png')
TAVERNKEEPER_RIGHT0 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_06.png')
TAVERNKEEPER_RIGHT1 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_07.png')
TAVERNKEEPER_RIGHT2 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_08.png')
TAVERNKEEPER_UP0 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_09.png')
TAVERNKEEPER_UP1 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_10.png')
TAVERNKEEPER_UP2 = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\sprite_11.png')
TAVERNKEEPER_PORTRAIT = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\portrait.png')
TAVERNKEEPER_PORTMINI = py.image.load('images\\entities\\noncombatants\\tavernkeeper\\port_mini.png')
TAVERNKEEPER_ACTOR = None

TAVERNKEEPER_SPRITE_DICT = {(0, 1): [TAVERNKEEPER_DOWN0, TAVERNKEEPER_DOWN0, TAVERNKEEPER_DOWN0, TAVERNKEEPER_DOWN1, TAVERNKEEPER_DOWN1, TAVERNKEEPER_DOWN1, TAVERNKEEPER_DOWN2, TAVERNKEEPER_DOWN2, TAVERNKEEPER_DOWN2, TAVERNKEEPER_DOWN1, TAVERNKEEPER_DOWN1, TAVERNKEEPER_DOWN1],
                       (0, -1): [TAVERNKEEPER_UP0, TAVERNKEEPER_UP0, TAVERNKEEPER_UP0, TAVERNKEEPER_UP1, TAVERNKEEPER_UP1, TAVERNKEEPER_UP1, TAVERNKEEPER_UP2, TAVERNKEEPER_UP2, TAVERNKEEPER_UP2,TAVERNKEEPER_UP1, TAVERNKEEPER_UP1, TAVERNKEEPER_UP1],
                       (-1, 0): [TAVERNKEEPER_LEFT0, TAVERNKEEPER_LEFT0, TAVERNKEEPER_LEFT0, TAVERNKEEPER_LEFT1, TAVERNKEEPER_LEFT1, TAVERNKEEPER_LEFT1, TAVERNKEEPER_LEFT2, TAVERNKEEPER_LEFT2, TAVERNKEEPER_LEFT2, TAVERNKEEPER_LEFT1, TAVERNKEEPER_LEFT1, TAVERNKEEPER_LEFT1],
                       (1, 0): [TAVERNKEEPER_RIGHT0, TAVERNKEEPER_RIGHT0, TAVERNKEEPER_RIGHT0, TAVERNKEEPER_RIGHT1, TAVERNKEEPER_RIGHT1, TAVERNKEEPER_RIGHT1, TAVERNKEEPER_RIGHT2, TAVERNKEEPER_RIGHT2, TAVERNKEEPER_RIGHT2, TAVERNKEEPER_RIGHT1, TAVERNKEEPER_RIGHT1, TAVERNKEEPER_RIGHT1],}

BUNDLE_TAVERNKEEPER = ImageBundle(TAVERNKEEPER_SPRITE_DICT,
                          TAVERNKEEPER_SPRITE_DICT.get((0, 1)),
                          TAVERNKEEPER_PORTRAIT,
                          TAVERNKEEPER_PORTMINI,
                          TAVERNKEEPER_ACTOR)

DUNGEON_ALPHA_NONCOMBATANT_IMAGE_BUNDLES = {'samwise': BUNDLE_SAMWISE,
                                            'mage': BUNDLE_MAGE,
                                            'guard_captain': BUNDLE_GUARD_CAPTAIN,
                                            'priest': BUNDLE_PRIEST,
                                            'rogue': BUNDLE_ROGUE,
                                            'mayor': BUNDLE_MAYOR,
                                            'homer': BUNDLE_HOMER,
                                            'innkeeper': BUNDLE_INNKEEPER,
                                            'tavernkeeper': BUNDLE_TAVERNKEEPER, }

BUNDLE_STICK = ImageBundle(sprite=py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\sprite.png'),
                           portrait=py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\portrait.png'),
                           port_mini=py.image.load('images\\entities\\items\\equippables\\weapons\\stick\\port_mini.png'))

BUNDLE_WEAPONS = {
    'staff': ImageBundle(sprite=py.image.load('images\\entities\\items\\equippables\\weapons\\staff\\sprite.png')),
    'dagger': ImageBundle(sprite=py.image.load('images\\entities\\items\\equippables\\weapons\\dagger\\sprite.png')),
    'shield': ImageBundle(sprite=py.image.load('images\\entities\\items\\equippables\\weapons\\shield\\sprite.png')),
    'longsword': ImageBundle(sprite=py.image.load('images\\entities\\items\\equippables\\weapons\\longsword\\sprite.png'),
                             portrait=py.image.load('images\\entities\\items\\equippables\\weapons\\longsword\\portrait.png')),
}

BUNDLE_POTION = ImageBundle(sprite=py.image.load('images\\entities\\items\\useables\\potion\\sprite.png'),
                            portrait=py.image.load('images\\entities\\items\\useables\\potion\\portrait.png'),
                            port_mini=py.image.load('images\\entities\\items\\useables\\potion\\port_mini.png'))
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
H_WOODPLANK_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank.png')
H_WOODPLANK_YELLOWRUG_TOPLEFT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_topleft.png')
H_WOODPLANK_YELLOWRUG_TOP_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_top.png')
H_WOODPLANK_YELLOWRUG_TOPRIGHT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_topright.png')
H_WOODPLANK_YELLOWRUG_RIGHT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_right.png')
H_WOODPLANK_YELLOWRUG_LEFT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_left.png')
H_WOODPLANK_YELLOWRUG_BOTLEFT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_botleft.png')
H_WOODPLANK_YELLOWRUG_BOT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_bot.png')
H_WOODPLANK_YELLOWRUG_BOTRIGHT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_yellowrug_botright.png')
H_WOODPLANK_REDRUG_TOPLEFT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_topleft.png')
H_WOODPLANK_REDRUG_TOP_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_top.png')
H_WOODPLANK_REDRUG_TOPRIGHT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_topright.png')
H_WOODPLANK_REDRUG_RIGHT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_right.png')
H_WOODPLANK_REDRUG_LEFT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_left.png')
H_WOODPLANK_REDRUG_BOTLEFT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_botleft.png')
H_WOODPLANK_REDRUG_BOT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_bot.png')
H_WOODPLANK_REDRUG_BOTRIGHT_TILEFLOOR = py.image.load('images\\tiles\\wood\\h_woodplank_redrug_botright.png')
V_WOODPLANK_TILEFLOOR = py.image.load('images\\tiles\\wood\\v_woodplank.png')
S_WOODPLANK_TILEFLOOR = py.image.load('images\\tiles\\wood\\s_woodplank.png')
D_WOODPLANK_TILEFLOOR = py.image.load('images\\tiles\\wood\\d_woodplank.png')

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

INT_EXTEND_BOT = py.image.load('images\\structures\\wood\\int_extend_bot.png')
INT_EXTEND_MID = py.image.load('images\\structures\\wood\\int_extend_mid.png')
INT_EXTEND_TOP = py.image.load('images\\structures\\wood\\int_extend_top.png')
INT_LEFT_BOT = py.image.load('images\\structures\\wood\\int_left_bot1.png')
INT_LEFT_MID = py.image.load('images\\structures\\wood\\int_left_mid.png')
INT_LEFT_TOP = py.image.load('images\\structures\\wood\\int_left_top1.png')
INT_RIGHT_BOT = py.image.load('images\\structures\\wood\\int_right_bot1.png')
INT_RIGHT_MID = py.image.load('images\\structures\\wood\\int_right_mid.png')
INT_RIGHT_TOP = py.image.load('images\\structures\\wood\\int_right_top1.png')
INT_SUPPORT_BOT = py.image.load('images\\structures\\wood\\int_support_bot.png')
INT_SUPPORT_MID = py.image.load('images\\structures\\wood\\int_support_mid.png')
INT_SUPPORT_TOP = py.image.load('images\\structures\\wood\\int_support_top.png')
INT_LEFT_WALL = py.image.load('images\\structures\\wood\\int_left_wall.png')
INT_RIGHT_WALL = py.image.load('images\\structures\\wood\\int_right_wall.png')
INT_CEILING_BOT = py.image.load('images\\structures\\wood\\int_ceiling_bot.png')
INT_CEILING_BOTLEFT = py.image.load('images\\structures\\wood\\int_ceiling_botleft.png')
INT_CEILING_BOTRIGHT = py.image.load('images\\structures\\wood\\int_ceiling_botright.png')
INT_CEILING_LEFT = py.image.load('images\\structures\\wood\\int_ceiling_left.png')
INT_CEILING_RIGHT = py.image.load('images\\structures\\wood\\int_ceiling_right.png')
INT_CEILING_TOPLEFT = py.image.load('images\\structures\\wood\\int_ceiling_topleft.png')
INT_CEILING_TOPRIGHT = py.image.load('images\\structures\\wood\\int_ceiling_topright.png')
INT_CEILING_TOP = py.image.load('images\\structures\\wood\\int_ceiling_top.png')




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