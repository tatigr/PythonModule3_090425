from classes import Card

def sum_points(cards: list[Card]) -> int:
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    num_aces = 0
    for card in cards:
        sum_points += card.points()
        if card.value == "A":
            num_aces += 1
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        sum_points -= num_aces * 10

    return sum_points


if __name__ == "__main__":
    assert sum_points([Card("Q", Card.DIAMONDS), Card("K", Card.DIAMONDS), Card("A", Card.DIAMONDS)]) == 21
    assert sum_points([Card("8", Card.DIAMONDS), Card("A", Card.DIAMONDS)]) == 19
    assert sum_points([Card("A", Card.HEARTS), Card("A", Card.DIAMONDS)]) == 2
    assert sum_points([Card("K", Card.HEARTS), Card("A", Card.DIAMONDS)]) == 21
    # Q(10) + K(10) + A(11->1) - 21
    # 8 + A(11) - 19
    # A(11->1) + A(11->1) -> 2
    # K(10) + A(11) -> 21
