from enums.game_states import GameStates


class GameHandler:

    def __init__(self, view, input):
        self.state = GameStates.MAIN_MENU
        self.view = view
        self.view.owner = self
        self.input = input
        self.input.owner = self
        self.dungeons = None

    def take_ownership(self):
        self.map.owner = self




