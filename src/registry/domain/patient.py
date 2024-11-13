from dataclasses import dataclass
from datetime import date


@dataclass
class Patient:
    id: int
    name: str
    dob: date
