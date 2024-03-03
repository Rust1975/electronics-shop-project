import pytest

from tests.fixtures import item_and_phone


def test_item_and_phone(item_and_phone):
    item1, phone1 = item_and_phone
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_invalid_number_of_sim(item_and_phone):
    item1, phone1 = item_and_phone
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0  # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
