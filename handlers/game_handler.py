from handlers.input_handler import InputHandler
from handlers.state_handlers import MenusHandler, TitleHandler, LifeHandler
from handlers.logic_handler import LogicHandler


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




