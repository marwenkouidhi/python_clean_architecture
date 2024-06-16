"""This module defines the RoomJsonEncoder class, which is a JSON encoder for serializing Room objects."""

import json


class RoomJsonEncoder(json.JSONEncoder):
    """JSON encoder for serializing Room objects."""

    def default(self, o: object) -> dict:
        """Serialize a Room object to a dictionary for JSON serialization.

        Args:
            o (object): The object to serialize. Should be an instance of Room.

        Returns:
            dict: A dictionary representation of the Room object.

        Raises:
            TypeError: If the object is not a Room or does not have required attributes.
        """
        try:
            to_serialize = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                'latitude': o.latitude,
                'longitude': o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
