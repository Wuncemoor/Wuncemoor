from enums.game_states import GameStates
from handlers.logic.logic_chunks import Move, Interact


class LogicHandler:

    def __init__(self):
        self.move = Move
        self.interact = Interact
        self.response = None



    @property
    def mapping(self):
        state = self.owner.state
        maps = {
            GameStates.TITLE: self.title,
            GameStates.LIFE: self.life,
            # GameStates.ENCOUNTER: self.encounter,
            # GameStates.DIALOGUE: self.dialogue,
            # GameStates.MENUS: self.menus,
            # GameStates.REWARD: self.loot,
            # GameStates.SHOW_MAP: self.map,
        }
        return maps.get(state)

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

    def mutate(self, changes):
        print(changes)
        for change in changes:
            print(change)
            if 'message' in change:
                self.owner.log.messages.add_message(change.get('message'))
            elif 'item_added' in change:
                print(len(self.owner.world.current_map.entities))
                self.owner.world.current_map.entities.remove(change.get('item_added'))
                print(len(self.owner.world.current_map.entities))

