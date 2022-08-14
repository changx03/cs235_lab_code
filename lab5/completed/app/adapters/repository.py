import abc
from typing import List

from app.models.person import Person

# A static repository to simulate a database.
people_repo = None


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __next__(self) -> Person:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Person:
        raise NotImplementedError


class PeopleRepository(AbstractRepository):
    def __init__(self, *args):
        self._people: List[Person] = []

        for person in args:
            self._people.append(person)

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self._people):
            raise StopIteration
        else:
            self._current += 1
            return self._people[self._current - 1]

    def get(self, reference: int):
        return next((p for p in self._people if p.id == reference), None)
