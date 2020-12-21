from config.constants import KEYDOWN_DELAY
from handlers.log_handler import LogHandler
from handlers import state_handlers
from handlers.time_handler import TimeHandler
import pygame as py
import sys

from world_objects.loot import Loot


class GameHandler:
    """Handler that holds nearly all aspects of the game while delegating the heavy lifting to StateHandlers"""

    def __init__(self, options):
        self.state_handler = None
        self.fullscreen = True
        self.options = options
        self.options.owner = self
        self.title = state_handlers.TitleHandler()
        self.title.owner = self
        self.life = state_handlers.LifeHandler()
        self.life.owner = self
        self.menus = state_handlers.MenusHandler()
        self.menus.owner = self
        self.debug = state_handlers.DebugHandler()
        self.debug.owner = self
        self.world = None
        self.dialogue = None
        self.time = None
        self.encounter = None
        self.reward = None
        self.party = None
        self.log = None
        self.shop = None

    @property
    def state(self):
        return self.state_handler.superstate

    def change_state(self, string):
        state_dict = {
            'title': self.title,
            'life': self.life,
            'menus': self.menus,
            'dialogue': self.dialogue,
            'shop': self.shop,
            'encounter': self.encounter,
            'reward': self.reward,
            'debug': self.debug,
        }

        self.set_key_repeat(string)
        self.state_handler = state_dict.get(string)

    @staticmethod
    def set_key_repeat(string):
        if string != 'life':
            py.key.set_repeat()
        else:
            py.key.set_repeat(KEYDOWN_DELAY)

    def take_ownership(self):
        self.world.owner = self
        self.dialogue.owner = self
        self.time.owner = self
        self.encounter.owner = self
        self.reward.owner = self
        self.party.owner = self
        self.log.owner = self
        self.shop.owner = self

    def preplay(self, world, party):
        loot = Loot()
        self.world = world
        self.dialogue = state_handlers.DialogueHandler([party.journal])
        self.shop = state_handlers.ShopHandler()
        self.time = TimeHandler([party])
        self.encounter = state_handlers.EncounterHandler(loot)
        self.reward = state_handlers.RewardHandler(loot)
        self.party = party
        # self.init_options()
        self.log = LogHandler()
        self.debug.set_allowed_objs()
        self.take_ownership()
        self.life.camera.refocus(party.p1.x, party.p1.y)
        self.life.fov.map = self.life.fov.initialize(self.world)
        self.state_handler = self.life

    # def init_options(self):
    #     for dung in self.world.dungeons.values():
    #         for map in dung.maps:
    #             for entity in map.noncombatants:
    #                 if entity.shopkeeper:
    #                     entity.shopkeeper.inventory.options = initialize_menu_options(entity.shopkeeper.inventory)


    @staticmethod
    def quit():
        py.quit()
        sys.exit()
