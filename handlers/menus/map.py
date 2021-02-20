from enums.game_states import MenusStates


class Map:
    def __init__(self):
        self.superstate = MenusStates.MAP
        self.options = []
        self.menu = None
        self.submenu = None
