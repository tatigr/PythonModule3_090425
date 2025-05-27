class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        extra_rub = self.kop // 100
        kop = self.kop % 100
        return f"{self.rub + extra_rub}руб {kop}коп"

    def __add__(self, other) -> 'Money':
        new_rub = self.rub + other.rub
        new_kop = self.kop + other.kop
        return Money(new_rub, new_kop)

    def __sub__(self, other) -> 'Money':
        new_rub = self.rub - other.rub
        new_kop = self.kop - other.kop
        return Money(new_rub, new_kop)

if __name__ == "__main__":
    money1 = Money(3, 60)
    money2 = Money(5, 60)
    money3 = money1 + money2 # money1.__add__(money2)
    print(money3) # 9 20
