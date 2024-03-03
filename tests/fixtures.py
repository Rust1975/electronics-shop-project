import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def sample_items():
    Item.all = []
    Item.pay_rate = 0.85
    item1 = Item("Iphone", 1000, 4)
    item2 = Item("TV", 5000, 2)
    return item1, item2

@pytest.fixture
def item_and_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    return item1, phone1

