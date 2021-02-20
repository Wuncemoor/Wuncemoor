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


class TitleStates(Enum):
    """States that occur in GameStates.TITLE"""

    OPENING = 1
    MAIN = 2
    NEW_GAME = 3
    LOAD_GAME = 4
    SETTINGS = 5
    ACKNOWLEDGEMENTS = 6


class LifeStates(Enum):
    """States that occur in GameStates.LIFE"""

    ROOT = 1
    SETTINGS = 2


class LifeSubStates(Enum):
    """Substates that occur within GameStates.LIFE"""

    SETTINGS_ROOT = 1
    SETTINGS_WAKEUP = 2
    SETTINGS_COMPENDIUM = 3
    SETTINGS_OPTIONS = 4


class EncounterStates(Enum):
    """States that occur in GameStates.ENCOUNTER"""

    THINKING = 1
    FIGHT_TARGETING = 2
    ENEMY_TURN = 3
    VICTORY = 4


class RewardStates(Enum):
    """States that occur in GameStates.REWARD"""

    THINKING = 1
    SIFTING = 2
    DEPOSITING = 3


class MenusStates(Enum):
    """States that occur in GameStates.MENUS"""

    CHAR_SHEET = 1
    JOURNAL = 2
    INVENTORY = 3
    MAP = 4

class MenuSubStates(Enum):
    """Substates that occur in GameStates.MENUS"""

    BASE = 1
    SUBMENU = 2
    SELECTED_OPTIONS = 3
    EXAMINING_MENU_OBJECT = 4


class ShopStates(Enum):
    """Substates that occur in GameStates.SHOP"""

    BASE = 1
    BUYING = 2
    SELLING = 3
    TRANSACTING = 4
