from enums.game_states import MenuStates


class Map:
    def __init__(self):
        self.superstate = MenuStates.MAP
        self.options = []