import pytest
from src.item import Item


@pytest.fixture
def sample_items():
    Item.pay_rate = 0.85
    item1 = Item("Iphone", 1000, 4)
    Item.all.append(item1)
    item2 = Item("TV", 5000, 2)
    Item.all.append(item2)
    return item1, item2
