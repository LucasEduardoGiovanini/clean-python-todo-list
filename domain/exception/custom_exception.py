class todoListError(Exception):
    def __init__(self, message: str, line: int, cause_message: str):
        self.message = message
        self.line = line
        self.cause_message = cause_message

    def __str__(self):
        return "Error: {}.".format(self.message) + " line error: {}.".format(self.line)+" caused by: {}".format(self.cause_message)