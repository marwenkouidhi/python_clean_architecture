"""Module defining an abstract base class for in-memory repositories."""

from abc import ABC, abstractmethod

from python_clean_architecture.domain.room import Room


class IMemRepo(ABC):
    """Abstract base class for in-memory repositories."""

    @abstractmethod
    def list(self) -> list[Room]:
        """Retrieve a list of rooms from the repository.

        Returns:
            List[Room]: List of Room objects.
        """
        pass
