class DialogueHandler():
    def __init__(self, observers):
        self.partner = None
        self.observers = observers
        self.real_talk = None

    def set_real_talk(self):
        responses = []
        for observer in self.observers:
            response = observer.transduce_all(self.partner.name)
            for res in response:
                responses.append(res)
        options = self.partner.noncombatant.dialogue.graph_dict.get(self.partner.noncombatant.dialogue.current_convo).options
        self.real_talk = [i for i in options if i.condition is None or i.condition in responses]

    def broadcast_choice(self, signal):
        if signal is not None:
            for observer in self.observers:
                observer.update_plot(signal)

