from unittest import mock
from uuid import uuid4
from python_clean_architecture.usecases.room_list import room_list_usecase
from pytest import fixture
from python_clean_architecture.domain.room import Room


@fixture
def domain_rooms():
    rooms = [
        {
            "code": uuid4(),
            "size": 10,
            "price": 100,
            "longitude": 10.25555,
            "latitude": 11.033333,
        },
        {
            "code": uuid4(),
            "size": 15,
            "price": 150,
            "longitude": 12.25555,
            "latitude": 10.33333,
        },
        {
            "code": uuid4(),
            "size": 20,
            "price": 200,
            "longitude": 9.25555,
            "latitude": 9.33333,
        },
        {
            "code": uuid4(),
            "size": 11,
            "price": 110,
            "longitude": 11.25555,
            "latitude": 8.933333,
        },
    ]

    return [Room.from_dict(room) for room in rooms]


def test_list_rooms_without_params(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms
    results = room_list_usecase(repo)
    repo.list.assert_called_with()

    assert results == domain_rooms
