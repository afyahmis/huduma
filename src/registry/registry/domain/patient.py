from dataclasses import dataclass
from shared.domain.common import AggregateRoot
from datetime import date


@dataclass
class Patient(AggregateRoot):
    name: str
    dob: date
