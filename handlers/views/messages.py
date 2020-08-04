from config.constants import WHITE


class Message:
    def __init__(self, text, color=WHITE):
        self.text = text
        self.color = color

    @staticmethod
    def placeholder():
        return Message('PLACEHOLDER')


class MessageLog:
    def __init__(self, capacity):
        self.messages = []
        self.capacity = capacity
        
    def add_message(self, message):

        if len(self.messages) == self.capacity:
            del self.messages[0]

        self.messages.append(message)
