"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from .fixtures import sample_items


def test_calculate_total_price(sample_items):
    item1, item2 = sample_items
    assert item1.calculate_total_price() == 4000
    assert item2.calculate_total_price() == 10000
    assert isinstance(item1.apply_discount(), float)


def test_apply_discount(sample_items):
    item1, item2 = sample_items
    assert item1.apply_discount() == 850
    assert item2.apply_discount() == 4250
    assert isinstance(item2.apply_discount(), float)


def test_item_all(sample_items):
    assert len(Item.all) == 2


def test_instantiate_from_csv():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    assert Item.all[3].name == "Мышка"


def test_string_to_number():
    Item.instantiate_from_csv("src/items.csv")
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('6.7') == 6


def test_item_name(sample_items):
    item1, item2 = sample_items
    item1.name = "СуперСмартфон"
    assert item1.name == 'СуперСмарт'