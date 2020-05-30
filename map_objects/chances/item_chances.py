from random_utils import from_dungeon_level


def get_item_chances(d_level):

    item_chances = {
        'healing_potion': 35,
        'sword': from_dungeon_level([[15, 2]], d_level),
        'shield': from_dungeon_level([[15, 2]], d_level),
        'lightning_scroll': from_dungeon_level([[25, 2]], d_level),
        'fireball_scroll': from_dungeon_level([[25, 2]], d_level),
        'confusion_scroll': from_dungeon_level([[10, 2]], d_level)
        }

    return item_chances
