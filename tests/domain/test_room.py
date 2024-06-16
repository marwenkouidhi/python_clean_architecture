"""Tests for the Room model and related functionalities."""

import uuid

from python_clean_architecture.domain.room import Room


def test_room_model_init() -> None:
    """Test the initialization of the Room model."""
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

    assert room.code == code
    assert room.size == size
    assert room.price == price
    assert room.longitude == longitude
    assert room.latitude == latitude


def test_room_from_dict() -> None:
    """Test creating a Room object from a dictionary."""
    code = uuid.uuid4()
    size = 5
    price = 5
    longitude = 0.4
    latitude = 0.7
    init_dict = {
        'code': code,
        'size': size,
        'price': price,
        'longitude': longitude,
        'latitude': latitude,
    }
    room = Room.from_dict(init_dict)

    assert room.code == code
    assert room.size == size
    assert room.price == price
    assert room.longitude == longitude
    assert room.latitude == latitude


def test_room_to_dict() -> None:
    """Test converting a Room object to a dictionary."""
    init_dict = {
        'code': uuid.uuid4(),
        'size': 5,
        'price': 5,
        'longitude': 0.4,
        'latitude': 0.7,
    }
    room = Room.from_dict(init_dict)

    assert Room.to_dict(room) == init_dict


def test_room_model_comparison() -> None:
    """Test equality comparison of Room objects."""
    init_dict = {
        'code': uuid.uuid4(),
        'size': 5,
        'price': 5,
        'longitude': 0.4,
        'latitude': 0.7,
    }
    room1 = Room.from_dict(init_dict)
    room2 = Room.from_dict(init_dict)

    assert room1 == room2
