from enums.game_states import GameStates
from handlers.logic.logic_chunks import Move, Interact, ShowMenus, Exit


class LogicHandler:

    def __init__(self):
        self.move = Move
        self.interact = Interact
        self.show_menus = ShowMenus
        self.exit = Exit
        self.response = None

    @property
    def state(self):
        return self.owner.state

    @property
    def handler(self):
        return self.owner.state_handler

    @property
    def mapping(self):
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            # GameStates.ENCOUNTER: self.encounter,
            # GameStates.DIALOGUE: self.dialogue,
            GameStates.MENUS: self.menus,
            # GameStates.REWARD: self.loot,
            # GameStates.SHOW_MAP: self.map,
        }
        return maps.get(self.state)

    @property
    def handler(self):
        return self.owner.state_handler

    def translate(self, output):
        self.mapping(output)

    def title(self, output):
        options = self.owner.options

        if 'traverse_menu' in output:
            options.traverse(output.get('traverse_menu'))
        elif 'choose_option' in output:
            self.response = options.choose()
            self.response(self)

    def life(self, output):

        if 'move' in output:
            self.response = self.move.logic
            self.response(self, output.get('move'))
        elif 'interact' in output:
            self.response = self.interact.logic
            changes = self.response(self)
            self.mutate(changes)
        elif 'show_menus' in output:
            self.response = self.show_menus.logic
            self.response(self, output.get('show_menus'))

    def menus(self, output):
        if 'exit' in output:
            self.response = self.exit.logic
            self.response(self)
        elif 'show_menus' in output:
            self.response = self.show_menus.logic
            self.response(self, output.get('show_menus'))

    def mutate(self, changes):
        for change in changes:
            if 'message' in change:
                self.owner.log.messages.add_message(change.get('message'))
            elif 'item_added' in change:
                self.owner.world.current_map.entities.remove(change.get('item_added'))

