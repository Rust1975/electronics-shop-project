from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int = None):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim


    @property
    def number_of_sim(self):
        return self._number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value


    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return NotImplemented




# phone1 = Phone("iPhone 14", 120_000, 5, 2)
# phone1.number_of_sim = 0

# print(str(phone1))
# print(repr(phone1))
#
# item1 = Item("Смартфон", 10000, 20)
# print(item1 + phone1)
