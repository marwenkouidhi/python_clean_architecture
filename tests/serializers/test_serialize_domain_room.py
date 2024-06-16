import json
import uuid

from python_clean_architecture.serializers.room import RoomJsonEncoder

from python_clean_architecture.domain.room import Room


def test_serialize_domain_room():
    code = uuid.uuid4()
    size = 5
    price = 5
    longitude = 0.4
    latitude = 0.7
    room = Room(
        code=code,
        size=size,
        price=price,
        longitude=longitude,
        latitude=latitude,
    )
    expected_json = f"""
        {{
            "code": "{code}",
            "size": {size},
            "price": {price},
            "latitude": {latitude},
            "longitude": {longitude}
        }}
     """
    json_room = json.dumps(room, cls=RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)