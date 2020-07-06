from handlers.views.messages import MessageLog


class LogHandler:
    def __init__(self):
        self.messages = MessageLog(10)