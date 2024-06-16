"""Repository module for managing in-memory Room data."""

from python_clean_architecture.domain.room import Room
from python_clean_architecture.interfaces.memrepo import IMemRepo


class MemRepo(IMemRepo):
    """Repository class for managing in-memory Room data.

    Attributes:
    ----------
        data : list
            The list containing the in-memory Room data.

    Methods:
    -------
        __init__(data: list) -> None
            Initialize the MemRepo with initial data.

        list() -> list[Room]
            Retrieve a list of rooms from the repository.
    """

    def __init__(self: 'MemRepo', data: list) -> None:
        """Initialize the MemRepo with initial data.

        Args:
            data (list): Initial data to populate the repository.
        """
        self.data = data

    def list(self: 'MemRepo') -> list[Room]:
        """Retrieve a list of rooms from the repository.

        Args:
            filters (dict, optional): Filters to apply on the room list. Defaults to None.

        Returns:
            list[Room]: List of Room objects matching the filters (if any).
        """
        result = [Room.from_dict(i) for i in self.data]
        return result
