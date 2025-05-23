class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits_icons = {
            'Diamonds': '\u2666',
            'Hearts': '\u2665',
            'Spades': '\u2660',
            'Clubs': '\u2663',
        }
        return f"{self.value}{suits_icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
for value in values:
    new_card = Card(value, "Hearts")
    hearts_cards.append(new_card)
hearts_cards_str = [card.to_str() for card in hearts_cards[::-1]]
print(",".join(hearts_cards_str))
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = []
for value in values:
    new_card = Card(value, "Diamonds")
    diamonds_cards.append(new_card)

diamond_cards_str = [card.to_str() for card in diamonds_cards]
print(",".join(diamond_cards_str))
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥


# cards = [
#     Card("2", "Hearts"),
#     Card("3", "Hearts"),
#     Card("4", "Hearts"),
#     ...]