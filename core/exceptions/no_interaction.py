class NoInteraction(Exception):
    def __init__(self) -> None:
        super().__init__("No Interaction Available.")
