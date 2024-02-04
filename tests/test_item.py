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
