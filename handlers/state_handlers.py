class MenuHandler:
    def __init__(self):
        self.state = None
        self.display = None
        self.options = None
        self.current_option = 0
        self.menu = None

    def handle_menu(self, menu_obj):
        self.menu = menu_obj
        self.state = menu_obj.superstate
        self.options = menu_obj.options
        self.current_option = 0


class DialogueHandler:
    def __init__(self, observers):
        self.partner = None
        self.observers = observers
        self.real_talk = None
        self.real_io = None

    def set_real_talk(self):
        responses = []
        for observer in self.observers:
            response = observer.transduce_all(self.partner.name)
            for res in response:
                responses.append(res)
        current_node = self.partner.noncombatant.dialogue.graph_dict.get(
            self.partner.noncombatant.dialogue.current_convo)
        options = current_node.options_text
        self.real_talk = [i for i in options if i.condition is None or i.condition in responses]
        self.set_real_io()

    def set_real_io(self):
        real = {}
        q = 1
        for option in self.real_talk:
            real[str(q)] = option.path
            q += 1
        self.real_io = real

    def broadcast_choice(self, signal):
        if signal is not None:
            for observer in self.observers:
                observer.update_plot(signal)


class TimeHandler:

    def __init__(self):
        self.year = -65
        self.month = 1
        self.day = 1
        self.hour = 8


    def time_goes_on(self):
        self.hour += 1
        self.new_day()

    def new_day(self):
        if self.hour > 23:
            self.hour -= 24
            self.day += 1
            self.new_month()

    def new_month(self):
        if self.day > 30:
            self.day -= 30
            self.month += 1
            self.new_year()

    def new_year(self):
        if self.month > 12:
            self.month -= 12
            self.year += 1

    def time_travel(self, time):
        self.year += time[0]
        self.month += time[1]
        self.new_year()
        self.day += time[2]
        self.new_month()
        self.hour += time[3]
        self.new_day()


