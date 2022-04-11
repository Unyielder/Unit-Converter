class ConversionError(Exception):
    def __init__(self, message):
        self.message = message


class UnitNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
