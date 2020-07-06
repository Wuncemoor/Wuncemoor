from enums.game_states import GameStates


class InterfaceHandler:

    @property
    def mapping(self):
        state = self.owner.state
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            GameStates.ENCOUNTER: self.encounter,
            GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            GameStates.REWARD: self.loot,
            GameStates.SHOW_MAP: self.map,
        }
        return maps.get(state)

    def title(self):
