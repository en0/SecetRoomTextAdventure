class UnknownRoom(Exception):
    def __init__(self):
        super().__init__("Unknown Room.")
