from enum import Enum	


class GameStates(Enum):
    TITLE = 1
    LIFE = 2
    MENUS = 3
    DIALOGUE = 4
    ENCOUNTER = 5
    REWARD = 6
    DEBUG = 7
    # States that need to be reimplemented
    # PLAYER_DEAD = 8
    # TARGETING = 9
    # LEVEL_UP = 10
    # COMPETENCE_MENU = 11


class EncounterStates(Enum):

    THINKING = 1
    FIGHT_TARGETING = 2
    ENEMY_TURN = 3
    VICTORY = 4


class RewardStates(Enum):

    THINKING = 1
    SIFTING = 2
    DEPOSITING = 3


class MenuStates(Enum):

    PARTY = 1
    JOURNAL = 2
    INVENTORY = 3
    MAP = 4
    SETTINGS = 5
