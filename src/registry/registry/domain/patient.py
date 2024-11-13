from dataclasses import dataclass
from shared.domain.common import AggregateRoot
from datetime import date


@dataclass
class Patient(AggregateRoot):
    id: int
    name: str
    dob: date
