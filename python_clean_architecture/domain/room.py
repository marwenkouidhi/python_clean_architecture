"""Module representing a Room class for handling room data."""

import uuid
from dataclasses import asdict, dataclass


@dataclass
class Room:
    """Represents a room with attributes code, size, price, longitude, and latitude.

    Attributes:
        code (uuid.UUID): Unique identifier for the room.
        size (int): Size of the room in square units.
        price (int): Price of the room.
        longitude (float): Longitude coordinate of the room's location.
        latitude (float): Latitude coordinate of the room's location.
    """

    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(cls: 'Room', data: dict[str, dict]) -> 'Room':
        """Creates a Room object from a dictionary.

        Args:
            data (dict): Dictionary containing room data.

        Returns:
            Room: Instance of Room created from the dictionary data.
        """
        return cls(**data)

    def to_dict(self: 'Room') -> dict[str, dict]:
        """Converts the Room object to a dictionary.

        Returns:
            dict: Dictionary representation of the Room object.
        """
        return asdict(self)
