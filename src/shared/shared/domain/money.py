from dataclasses import dataclass

from shared.domain.common import ValueObject


@dataclass(frozen=True, order=True)
class Money(ValueObject):
    amount: float
    currency: str
