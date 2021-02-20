from enums.game_states import MenusStates


class CharSheet:
    def __init__(self):
        self.superstate = MenusStates.CHAR_SHEET
        self.menu = None
        self.submenu = None
