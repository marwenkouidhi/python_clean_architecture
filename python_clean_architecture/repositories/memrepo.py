from python_clean_architecture.domain.room import Room


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        result = [Room.from_dict(i) for i in self.data]

        return result
