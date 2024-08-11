import csv
import os
import chardet

class InstantiateCSVError(Exception):
    """Ошибка целостности данных."""
    def __init__(self, message="Ошибка целостности данных"):
        super().__init__(message)

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
        super().__init__() # Подмешиваем __init__ из Mixinlog
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # добавляем созданный экземпляр в список all

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return NotImplemented

    @staticmethod
    def string_to_number(istr: str):
        return int(float(istr))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, ipath: str):
        current_dir = os.path.dirname(__file__)
        ipath = os.path.join(current_dir, ipath.split("/")[-1])
        try:
            with open(ipath, encoding='windows-1251', newline='') as csvfile:
            # with open(ipath, encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                for row in reader:
                    iname = row.get("name")
                    iprice = row.get("price")
                    iquantity = row.get("quantity")
                    if not iname or not iprice or not iquantity:
                        raise InstantiateCSVError("_Файл item.csv поврежден_")
                    cls(iname, iprice, iquantity)
                return cls
        except FileNotFoundError:
            print("_Отсутствует файл item.csv_")

    def get_encoding(ipath):
        with open(ipath, 'rb') as f:
            raw_data = f.read()
        return chardet.detect(raw_data)['encoding']

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

    # TestCase4
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    assert Item.all[3].name == "Мышка"

# run_tests()
# print(Item.all)
# print(Item.instantiate_from_csv("src/items.csv"))
# Item.instantiate_from_csv("src/items.csv")
# print(len(Item.all))
# print(Item.all[3].name)
# item1 = Item("Iphone", 1000, 4)
# print(item1)
# print(repr(item1))

# file_path = "src/items.csv"
# Item.instantiate_from_csv("src/items.csv")
# encoding = Item.get_encoding("src/items.csv")
# print(f"Detected encoding: {encoding}")
