class PortalLocked(Exception):
    def __init__(self):
        super().__init__("Portal Locked.")
