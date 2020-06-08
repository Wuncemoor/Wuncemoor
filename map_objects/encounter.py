from enums.game_states import EncounterStates
class Encounter:

    def __init__(self, background, event, options):
        self.background = background
        self.event = event
        self.options = options
        self.current_option = 0
        self.state = EncounterStates.THINKING
        self.xp = 0



