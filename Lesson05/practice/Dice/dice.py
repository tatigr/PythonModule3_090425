import random

class Dice:
    def __init__(self, sides=6):
        # _ protected
        # __ private
        self.__sides = sides

    def roll(self) -> int:
        return random.randint(1, self.__sides)

    # сеттер
    def set_sides(self, new_sides):
        if isinstance(new_sides, int) and new_sides > 0:
            self.__sides = new_sides
        else:
            raise ValueError("Количество граней должно быть целым положительным числом")

    # геттер
    def get_sides(self):
        return self.__sides


if __name__ == "__main__":
    dice1 = Dice()
    dice2 = Dice(8)

    print(dice2.get_sides())
    dice2.set_sides(20)
    print(dice2.get_sides())

# TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте

# TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
#   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков

# TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
#   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
#   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError

# TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
#   Пример: dice6 = Dice(6) - создаем шестигранный кубик
#   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
