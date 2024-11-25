from dataclasses import dataclass


@dataclass
class User:
    username: str = None
    password: str = None
    name: str = None
    last_name: str = None
