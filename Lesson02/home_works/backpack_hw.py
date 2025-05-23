class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self) -> str:
        return f"{self.name} - вес: {self.weight} кг, цена: {self.cost} руб."


class BackPack:
    def __init__(self, max_weight):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, items: list[Item]) -> None:
        # Сортируем предметы по весу, чтобы положить в рюкзак максимальное количество
        items = sorted(items, key=lambda item: item.weight)

        for item in items:
            if self.sum_weight() + item.weight <= self.max_weight:
                self.items.append(item)
            else:
                print(f"Предмет {item.name} слишком тяжелый, не добавили в рюкзак.")

    def show_items(self) -> None:
        print("Содержимое рюкзака:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.show()}")
        print(f"Общий вес в рюкзаке: {self.sum_weight():.2f} кг.\n")

    def max_weight_item(self) -> None:
        max_weight_item = max(self.items, key=lambda item: item.weight)
        print(f"Самый тяжелый предмет: {max_weight_item.show()}")

    def max_valuable(self) -> None:
        max_valuable_item = max(self.items, key=lambda item: item.cost / item.weight)
        print(f"Самый ценный предмет (цена/вес): {max_valuable_item.show()}")

    def sum_weight(self) -> float:
        return sum(item.weight for item in self.items)



backpack = BackPack(max_weight=8.5)

items = [
    Item("Вода", 2.5, 150),
    Item("Спички", 0.01, 30),
    Item("Фонарик", 0.5, 250),
    Item("Батарейки", 0.1, 250),
    Item("Палатка", 7, 15000),
    Item("Книга", 1, 750),
    Item("Носки", 0.3, 500),
    Item("Соль", 0.1, 25),
]

backpack.add_item(items)
backpack.show_items()
backpack.max_weight_item()
backpack.max_valuable()


