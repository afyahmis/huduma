import uuid
from dataclasses import dataclass


class ValueObject:
    """base value object"""

    pass


@dataclass
class BaseEntity:
    def __post_init__(self):
        self.id = uuid.uuid1()


@dataclass
class AggregateRoot(BaseEntity):
    """base aggregate root"""

    pass


class BusinessError(Exception):
    """Base class for other exceptions"""

    pass
