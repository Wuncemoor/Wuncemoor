from enums.game_states import MenuStates


class CharSheet:
    def __init__(self):
        self.superstate = MenuStates.CHAR_SHEET
        self.menu = None
        self.submenu = None
