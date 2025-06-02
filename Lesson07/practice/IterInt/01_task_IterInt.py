# Разработать класс IterInt, который наследует функциональность стандартного типа int, но добавляет
# возможность итерировать по цифрам числа

class MyIterator:
    def __init__(self, number):
        self.number = number  # 123
        self.length = 0
        number = self.number
        while number != 0:
            number //= 10
            self.length += 1

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        digit = self.number // 10 ** (self.length - 1)
        self.number = self.number % 10 ** (self.length - 1)
        self.length -= 1
        return digit


class IterInt(int):
    def __iter__(self):
        return MyIterator(self)


# Iterable - итерируемый объект (контейнер для хранения элементов)
# Iterator - итератор (инструмент для обхода элементов ин.объекта)


n1 = IterInt(12)
n2 = IterInt(24)

n1.is_integer()

for digit1 in n:  # d1 = 4 | 3 | 2 | 2 | 1
    # for digit2 in n:  # d2 = 4 | 3 | 2 | 1
    #     print("digit2 = ", digit2)
    print("digit1 = ", digit1)
    # print("-----")

# __iter__() -> iterator
# iterator.__next__() -> 1 | 2 |3 | 4 | 6
# iterator.__next__() -> 1 | 2 |3 | 4 | 6

# Выведет:
# digit = 1
# digit = 2
# digit = 3
# digit = 4
# digit = 6
