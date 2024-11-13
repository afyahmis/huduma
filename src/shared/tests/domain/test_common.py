from dataclasses import dataclass

from shared.domain.common import BaseEntity, AggregateRoot


@dataclass
class TestCar(BaseEntity):
    model: str

    def __str__(self):
        return f"{self.model} [{self.id}]"


@dataclass
class TestCountry(AggregateRoot):
    code: str
    name: str

    def __str__(self):
        return f"{self.code},{self.name} [{self.id}]"


def test_entity_has_id():
    car = TestCar(model="subaru")
    carb = TestCar(model="toyota")
    assert car.id
    assert car.model == "subaru"
    assert carb.id != car.id
    print(f"\n{car}")
    print(carb)


def test_aggregateRoot_has_id():
    ke = TestCountry(code="ke", name="kenya")
    ug = TestCountry(code="ug", name="uganda")
    assert ke.id
    assert ke.name == "kenya"
    assert ke.id != ug.id
    print(f"\n{ke}")
    print(ug)
