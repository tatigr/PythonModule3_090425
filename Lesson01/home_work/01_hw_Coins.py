import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(["heads", "tails"])  # random: heads/tails

    def __str__(self):
        return f"coin: {self.side}"


num_coins = 10
coins = [Coin() for _ in range(num_coins)]

for coin in coins:
    coin.flip()

num_heads = 0
num_tails = 0
for coin in coins:
    if coin.side == "heads":
        num_heads += 1
    else:
        num_tails += 1

...