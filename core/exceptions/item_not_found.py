class ItemNotFoundException(Exception):
    def __init__(self, item_name: str):
        super().__init__("Item {} not found.".format(item_name))
