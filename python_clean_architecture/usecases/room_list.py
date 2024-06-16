"""This module contains use case functions related to rooms."""

from python_clean_architecture.domain.room import Room
from python_clean_architecture.interfaces.memrepo import IMemRepo


def room_list_usecase(repo: IMemRepo) -> list[Room]:
    """Fetches a list of rooms from the repository.

    Args:
        repo (RoomRepository): The repository object implementing RoomRepository.

    Returns:
        List[Room]: A list of Room objects fetched from the repository.
    """
    return repo.list()
