# Because Exception is the parent class for all exception types
class InvalidPin(Exception):
    def __init__(self, msg):
        self.msg = msg
