from dataclasses import dataclass

from shared.domain.common import ValueObject, BusinessError


@dataclass(frozen=True, order=True)
class Money(ValueObject):
    amount: float
    currency: str

    @property
    def amount_curr(self):
        return f"{self.amount:,.2f} {self.currency}"

    @property
    def curr_amount(self):
        return f"{self.currency} {self.amount:,.2f}"

    def __post_init__(self):
        if self.amount < 0:
            raise InvalidAmountError(self.amount)

        object.__setattr__(self, "currency", self.currency.upper())

    def __str__(self):
        return self.amount_curr


class InvalidAmountError(BusinessError):
    def __init__(self, amount):
        super().__init__(f"Invalid amount {amount} ,cannot be less than zero")
