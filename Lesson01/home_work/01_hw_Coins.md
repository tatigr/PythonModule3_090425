# Задание:
1. Создайте список из n-монеток, n - вводится с клавиатуры
2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
3. Выведите соотношение выпавших орлов и решек в процентах

Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
она находится у вас в руке и не выпала ни орлом ни решкой. \
Монетка "определеяется" со стороной(орел/решка), только после того, как вы ее подбрасываете(вызываете метод flip())

import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])

number_of_coins = int(input("Введите число монеток: "))

print(random.choice(['heads', 'tails']))

coins = []
for _ in range(number_of_coins):
    coin = Coin()
    coin.flip()
    coins.append(coin)
print([coin.side for coin in coins])

count_of_heads = 0
for coin in coins:
    if coin.side == 'heads':
        count_of_heads += 1

percent_heads = round(count_of_heads * 100 / number_of_coins, 2)
percent_tails = round((number_of_coins - count_of_heads) * 100 / number_of_coins, 2)

print(f"Процент монет, выпавших орлом: {percent_heads}%")
print(f"Процент монет, выпавших решкой: {percent_tails}%")
