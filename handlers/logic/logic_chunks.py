from abc import ABC, abstractmethod

from loader_functions.data_loaders import load_game
from loader_functions.initialize_new_game import get_game_variables


class Logic(ABC):

    @abstractmethod
    def logic(self):
        pass


class Option(Logic):

    @property
    @abstractmethod
    def display(self):
        pass


class NewGame(Option):

    display = 'Start A New Game'

    def logic(self):
        dungeons, world, overworld_tiles, party = get_game_variables()
        self.owner.preplay(dungeons, world, overworld_tiles, party)


class LoadGame(Option):

    display = 'Continue A Previous Game'

    def logic(self):
        dungeons, world, overworld_tiles, party = load_game()
        self.owner.preplay(dungeons, world, overworld_tiles, party)


class QuitGame(Option):

    display = 'Quit'

    def logic(self):
        self.owner.quit()


class Move(Logic):

    def logic(self, output):
        dx, dy = output
        x, y = self.owner.party.x, self.owner.party.y
        destination_x = x + dx
        destination_y = y + dy

        if not self.owner.world.is_blocked(destination_x, destination_y):

            self.owner.party.move(dx, dy)
            self.handler.camera.refocus(x, y)

            self.handler.fov.needs_recompute = True

            if self.owner.world.dangerous:
                self.owner.time.goes_on()
                encountering = self.owner.encounter.check()
                if encountering:
                    tile = self.owner.world.tiles[destination_x][destination_y]
                    options = ['FIGHT', 'ITEM', 'RUN']
                    self.owner.encounter.new(tile, options)
                    self.owner.state_handler = self.encounter
                else:
                    self.owner.encounter.steps_since += 1



