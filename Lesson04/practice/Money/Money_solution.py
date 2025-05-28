class Money:
    def __init__(self, rub, kop):
        self.kop = rub * 100 + kop

    def __str__(self):
        kop = abs(self.kop)
        rub = kop // 100
        kop = kop % 100
        if self.kop < 0:
            return f"-{rub}руб {kop}коп"
        else:
            return f"{rub}руб {kop}коп"

    def __add__(self, other) -> 'Money':
        new_kop = self.kop + other.kop
        return Money(0, new_kop)

    def __sub__(self, other) -> 'Money':
        new_kop = self.kop - other.kop
        return Money(0, new_kop)

    def __mul__(self, number):
        new_kop = self.kop * number
        return Money(0, new_kop)

    def __rmul__(self, other):
        return self.__mul__(other)


# TDD - разработка через тестирование
if __name__ == "__main__":
    money1 = Money(3, 60)
    money2 = Money(5, 60)
    money3 = money1 * 3  # money1.__mul__(3)
    print(money3)  # 9 20


str(obj) # obj.__str__()
iter(obj) # obj.__iter__()
next(obj) # obj.__next__()
len(obj)  # obj.__len__()

list = []
list.__count = 0

list.append(12)
list.__count = 1