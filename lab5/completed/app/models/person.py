class Person:
    def __init__(self, id: int, firstname: str, lastname: str, url: str) -> None:
        self._id = id
        self._firstname = firstname
        self._lastname =lastname
        self._url = url

    @property
    def id(self) -> int:
        return self._id

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def lastname(self) -> str:
        return self._lastname

    @property
    def url(self) -> str:
        return self._url
