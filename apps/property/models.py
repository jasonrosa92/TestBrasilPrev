from dataclasses import dataclass
from apps.user.models import Player
import random


@dataclass
class Property:
    player: Player = None
    sale_price: float = 0.0
    rent_value: float = 0.0

    @classmethod
    def create(cls, min_value: float = 300, max_value: float = 30000.0):
        assert min_value < max_value  # TODO: handle exception
        sale_price = random.uniform(min_value, max_value)
        rent_value = random.uniform(1, 100)
        return cls(sale_price=sale_price, rent_value=rent_value)


if __name__ == '__main__':
    property = Property.create()
    print(property)
    