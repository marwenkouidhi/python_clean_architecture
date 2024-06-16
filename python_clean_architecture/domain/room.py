import uuid
from dataclasses import asdict, dataclass


@dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return asdict(self)
