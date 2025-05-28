import random

class Dice:
    def __init__(self, sides=6):
        # _ protected
        # __ private
        self.__sides = sides
        self.side = None
        self.__rolls_history = []

    def roll(self) -> int:
        self.side = random.randint(1, self.__sides)
        self.__rolls_history.append(self.__rolls_history)
        return self.side

    # геттер
    def get_history(self):
        return self.__rolls_history

    # сеттер
    def set_sides(self, new_sides):
        if not isinstance(new_sides, int) or new_sides < 0:
            raise ValueError("Количество граней должно быть целым положительным числом")

        self.__sides = new_sides

    # геттер
    @property
    def sides(self):
        return self.__sides

    def __eq__(self, other_dice):
        if self.side is None or other_dice.side is None:
            raise TypeError("Можно сравнивать только подброшенные кубики")

        return self.side == other_dice.side


if __name__ == "__main__":
    dice1 = Dice()
    dice1.sides = 12
    # dice2 = Dice(8)
    #
    # print(dice2.get_sides())
    # dice2.set_sides(20)
    # print(dice2.get_sides())

    # TODO-1: Найти некорректные значение, которые можно записать в атрибут .side и исправьте

    # TODO-2: Создать список из N кубиков, подбросить все и посмотреть количество выпадений каждой стороны
    #   Формат: 2-ка выпала у 3 кубиков, 3-ка выпала у 2 кубиков
    # n = 10
    # dices = [Dice() for _ in range(n)]
    # roll_results = {}
    # for dice in dices:
    #     side = dice.roll()
    #     if side in roll_results.keys():
    #         roll_results[side] += 1
    #     else:
    #         roll_results[side] = 1
    #
    # print(roll_results)

    # TODO-3: Добавить три операции сравнения кубиков(< > ==). Кубики можно сравнивать только после подбрасывания.
    #   Если кубик выпал 5-кой, то он больше чем кубик выпавший 3-кой
    #   При сравнении кубиков до подбрасывание выбрасываем исключение TypeError
    dice1 = Dice(10)
    dice2 = Dice(12)
    dice1.roll()
    dice2.roll()
    if dice1 == dice2:
        print(f"Кубики равны | {dice1.side} | {dice2.side}")
    else:
        print(f"Кубики НЕ равны | {dice1.side} | {dice2.side}")
    # TODO-4: Добавить возможность создавать кубики с произвольным количеством граней:
    #   Пример: dice6 = Dice(6) - создаем шестигранный кубик
    #   Пример: dice20 = Dice(20) - создаем двадцатигранный кубик
