from config.constants import BLACK
from handlers.input_handler import InputHandler
from handlers.log_handler import LogHandler
from handlers.interface_handler import InterfaceHandler
from handlers.state_handlers import MenusHandler, TitleHandler, LifeHandler, DialogueHandler, TimeHandler, \
    EncounterHandler, RewardHandler
from handlers.logic_handler import LogicHandler
import pygame as py
import sys

from map_objects.loot import Loot


class GameHandler:

    def __init__(self, view):
        self.state_handler = None
        self.view = view
        self.view.owner = self
        self.logic = LogicHandler()
        self.logic.owner = self
        self.input = InputHandler()
        self.input.owner = self
        self.title = TitleHandler()
        self.title.owner = self
        self.life = LifeHandler()
        self.life.owner = self
        self.menus = MenusHandler()
        self.menus.owner = self


    @property
    def state(self):
        return self.state_handler.superstate

    def take_ownership(self):
        self.world.owner = self
        self.dialogue.owner = self
        self.time.owner = self
        self.encounter.owner = self
        self.reward.owner = self
        self.party.owner = self
        self.log.owner = self
        self.interface.owner = self

    def preplay(self, dungeons, world, overworld_tiles, party):
        loot = Loot()
        self.view.screen.fill(BLACK)
        self.view.world_tiles = overworld_tiles
        self.world = world
        self.dungeons = dungeons
        self.dialogue = DialogueHandler([party.journal])
        self.time = TimeHandler([party])
        self.encounter = EncounterHandler(loot)
        self.reward = RewardHandler(loot)
        self.party = party
        self.log = LogHandler()
        self.interface = InterfaceHandler()
        self.take_ownership()
        self.view.camera.refocus(party.p1.x, party.p1.y)
        self.view.fov.map = self.view.fov.initialize(self.world)
        self.owner.state_handler = self.owner.life

    def quit(self):
        py.quit()
        sys.exit()




