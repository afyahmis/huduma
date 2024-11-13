import pytest
from domain.money import Money

def test_money_init():
    kes = Money(1, "kes")
    assert kes.amount == 1
    assert kes.currency == "kes"
