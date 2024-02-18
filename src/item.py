import csv
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(istr: str):
        return int(istr)

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        # self.__name = name
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        Item.all.append(self)  # добавляем созданный экземпляр в список all

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     if len(value) > 10:
    #         self.__name = value[:9]
    #     else:
    #          self.__name = value

    @classmethod
    def instantiate_from_csv(cls, ipath: str):
        current_dir = os.path.dirname(__file__)
        ipath = os.path.join(current_dir, ipath.split("/")[-1])
        with open(ipath, encoding='windows-1251', newline='') as csvfile:
        # with open(ipath, encoding='utf-8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # cls.all.clear()
            for row in reader:
                # iname, iprice, iquantity = row
                # cls(iname, iprice, iquantity)
                # print(new_item.price)
                # Item().init(iname, iprice, iquantity)
                iname = row["name"]
                iprice = row["price"]
                iquantity = row["quantity"]
                cls(iname, iprice, iquantity)
            return cls

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
        self.price *= self.pay_rate
        return self.price


def run_tests():
    item1 = Item("Iphone", 1000, 4)
    item2 = Item("TV", 5000, 2)
    Item.pay_rate = 0.85

    # TestCase1
    assert item1.calculate_total_price() == 4000
    assert item1.apply_discount() == 850
    assert isinstance(item1.apply_discount(), float)

    # TestCase2
    assert item2.calculate_total_price() == 10000
    assert item2.apply_discount() == 4250
    assert isinstance(item2.apply_discount(), float)

    # TestCase3
    assert len(Item.all) == 2


# run_tests()
# print(Item.all)
# print(Item.instantiate_from_csv("src/items.csv"))
Item.instantiate_from_csv("src/items.csv")
print(len(Item.all))
print(Item.all[0].name)