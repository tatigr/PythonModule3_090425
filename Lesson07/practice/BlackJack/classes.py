# Возьмите классы Deck и Card с GIST'а занятия. Доработайте классы, если требуется.
class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'

    def __init__(self, value: str, suit: str):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self) -> str:
        suits_icons = {
            'Diamonds': '\u2666',
            'Hearts': '\u2665',
            'Spades': '\u2660',
            'Clubs': '\u2663',
        }
        return f"{self.value}{suits_icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def __gt__(self, other_card) -> bool:
        index_value1 = Deck.values.index(self.value)
        index_value2 = Deck.values.index(other_card.value)
        if index_value1 > index_value2:
            return True
        elif index_value1 < index_value2:
            return False
        else:  # если значения равны
            index_suit1 = Deck.suits.index(self.suit)
            index_suit2 = Deck.suits.index(other_card.suit)
            return index_suit1 > index_suit2

    def __lt__(self, other_card) -> bool:
        return not self.__gt__(other_card)

    # Добавляем метод, возвращающий кол-во очков для каждой карты
    def points(self):
        return Deck.card_points[self.value]


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card

        self.cards = []
        self.card_index = 0
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(value, suit))

    def __str__(self) -> str:
        return f"cards[{len(self.cards)}]" + ", ".join([card.__str__() for card in self.cards])

    def __iter__(self):
        self.card_index = 0
        return self

    def __next__(self):
        try:
            card = self.cards[self.card_index]
        except IndexError:
            raise StopIteration
        self.card_index += 1
        return card

    def draw(self, x: int) -> list[Card]:
        cards = self.cards[:x]
        self.cards = self.cards[x:]
        return cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)