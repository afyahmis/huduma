from dataclasses import dataclass

from domain.common import ValueObject


@dataclass(frozen=True)
class Money(ValueObject):
    amount:float
    currency:str
