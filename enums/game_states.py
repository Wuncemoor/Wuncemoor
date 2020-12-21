from enum import Enum	


class GameStates(Enum):
    """States of the game that occur discretely"""
    TITLE = 1
    LIFE = 2
    MENUS = 3
    DIALOGUE = 4
    SHOP = 5
    ENCOUNTER = 6
    REWARD = 7
    DEBUG = 8
    # States that need to be reimplemented
    # PLAYER_DEAD = 8
    # TARGETING = 9
    # LEVEL_UP = 10
    # COMPETENCE_MENU = 11


class EncounterStates(Enum):
    """Substates that occur in GameStates.ENCOUNTER"""

    THINKING = 1
    FIGHT_TARGETING = 2
    ENEMY_TURN = 3
    VICTORY = 4


class RewardStates(Enum):
    """Substates that occur in GameStates.REWARD"""

    THINKING = 1
    SIFTING = 2
    DEPOSITING = 3


class MenuStates(Enum):
    """Substates that occur in GameStates.MENUS"""

    PARTY = 1
    JOURNAL = 2
    INVENTORY = 3
    MAP = 4
    SETTINGS = 5


class InventoryStates(Enum):
    """Sub-substates that occur in MenuStates.INVENTORY"""

    BASE = 1
    SUBINVENTORY = 2
    ENTITY_OPTIONS = 3




class ShopStates(Enum):
    """Substates that occur in GameStates.SHOP"""

    BASE = 1
    BUYING = 2
    SELLING = 3
    TRANSACTING = 4
