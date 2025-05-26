import random


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        suits_icons = {
            'Diamonds': '\u2666',
            'Hearts': '\u2665',
            'Spades': '\u2660',
            'Clubs': '\u2663',
        }
        return f"{self.value}{suits_icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    def more(self, other_card) -> bool:
        index_value1 = Deck.values.index(self.value)
        index_value2 = Deck.values.index(other_card.value)
        if index_value1 > index_value2:
            return True
        elif index_value1 < index_value2:
            return False
        else: # если значения равны
            index_suit1 = Deck.suits.index(self.suit)
            index_suit2 = Deck.suits.index(other_card.suit)
            return index_suit1 > index_suit2


    def less(self, other_card) -> bool:
        return not self.more(other_card)

class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card

        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))

    def show(self) -> str:
        return f"cards[{len(self.cards)}]" + ", ".join([card.to_str() for card in self.cards])

    def draw(self, x: int) -> list[Card]:
        cards = self.cards[:x]
        self.cards = self.cards[x:]
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
# card1, card2 = deck.draw(2)
card1 = Card("K", "Hearts")
card2 = Card("K", "Diamonds")

# Тестируем методы .less() и .more()
if card1.less(card2):
    print(f"{card1.to_str()} меньше  {card2.to_str()}")
else:
    print(f"{card1.to_str()} больше {card2.to_str()}")
# if card1.less(card2):
#     print(f"{card1.to_str()} меньше {card2.to_str()}")
