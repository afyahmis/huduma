import pytest

from shared.domain.money import Money, InvalidAmountError


def test_money_init():
    kes = Money(1009.12, "kes")
    assert kes.amount == 1009.12
    assert kes.currency == "KES"
    print(f"\n{kes}")


def test_money_currency_format():
    usd = Money(147000.50, "usd")
    assert usd.currency == "USD"
    print(f"\n{usd}")


def test_money_valid_only():
    with pytest.raises(InvalidAmountError) as ex:
        Money(-1, "kes")
