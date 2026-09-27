class User:
    """Encapsulates JSON response payload from user API."""
    def __init__(self, id: int, name: str, username: str, email: str, address: dict = None, **kwargs):
        self._id = id
        self._name = name
        self._username = username
        self._email = email
        self._address = address or {}

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def address(self) -> dict:
        return self._address

    @classmethod
    def from_json(cls, json_dict: dict):
        return cls(**json_dict)