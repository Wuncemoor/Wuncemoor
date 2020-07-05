from enums.game_states import GameStates
from handlers.input_handler import InputHandler
from handlers.state_handlers import MenusHandler


class GameHandler:

    def __init__(self, view):
        self.state = GameStates.MAIN_MENU
        self.view = view
        self.view.owner = self
        self.input = InputHandler()
        self.input.owner = self
        self.menus = MenusHandler()
        self.menus.owner = self

    def take_ownership(self):
        self.world.owner = self
        self.dialogue.owner = self
        self.time.owner = self
        self.encounter.owner = self
        self.reward.owner = self




