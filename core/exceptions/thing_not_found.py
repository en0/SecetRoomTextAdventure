class ThingNotFound(Exception):
    def __init__(self, thing_name: str):
        super().__init__("{} not found.".format(thing_name))
