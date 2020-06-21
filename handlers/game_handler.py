from enums.game_states import GameStates


class GameHandler:

    def __init__(self, screen):
        self.screen = screen
        self.state = GameStates.PLAYERS_TURN



