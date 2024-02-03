class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.pay_rate


def run_tests():
    item1 = Item("Iphone", 1000, 4)
    Item.all.append(item1)
    item2 = Item("TV", 5000, 2)
    Item.all.append(item2)
    Item.pay_rate = 0.85

    # TestCase1
    assert item1.calculate_total_price() == 4000
    assert item1.apply_discount() == 850

    # TestCase2
    assert item2.calculate_total_price() == 10000
    assert item2.apply_discount() == 4250

    # TestCase3
    assert len(Item.all) == 2


run_tests()
