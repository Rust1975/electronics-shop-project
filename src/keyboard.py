from src.item import Item

class MixinLog:
    Lang_start = "EN"

class Keyboard(Item, MixinLog):

    def __init__(self, name: str, price: float, quantity: int, language=MixinLog.Lang_start):
        super().__init__(name, price, quantity)
        self.__language = language

    # свойство-геттер
    @property
    def language(self):
        return self.__language

    # свойство-сеттер
    @language.setter
    def language(self, language):
        if language in ("EN", "RU"):
            self.__language = language
        else:
            print("AttributeError: property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if MixinLog.Lang_start == "EN":
            MixinLog.Lang_start = "RU"
            self.language = MixinLog.Lang_start
        else:
            MixinLog.Lang_start = "EN"
            self.language = MixinLog.Lang_start

# kb = Keyboard('Dark Project KD87A', 9600, 5)
# print(kb.language)
# kb.language = 'CH'
# kb.change_lang()
# print(kb.language)
