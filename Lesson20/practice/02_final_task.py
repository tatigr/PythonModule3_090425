from typing import Protocol, List, Tuple, Dict, Any, Optional, runtime_checkable


# --- Протоколы ---

@runtime_checkable
class Product(Protocol):
    """
    Протокол для любого элемента, который может быть частью меню.
    Он должен иметь имя и цену.
    """
    name: str
    price: float

    def __str__(self) -> str:
        ...


@runtime_checkable
class Orderable(Product, Protocol):
    """
    Протокол для элемента, который может быть добавлен в заказ.
    Расширяет Product и добавляет метод для получения стоимости
    с учетом количества.
    """

    # name и price наследуются от Product
    # __str__ наследуется от Product

    def get_item_price_with_quantity(self, quantity: int) -> float:
        """
        Возвращает общую стоимость элемента с учетом заданного количества.
        """
        ...


# --- Классы ---

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"

    # Метод, необходимый для соответствия протоколу Orderable
    def get_item_price_with_quantity(self, quantity: int) -> float:
        return self.price * quantity


class Order:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        # Список кортежей: (Orderable, quantity) - теперь типизирован протоколом
        self.items: List[Tuple[Orderable, int]] = []
        self.is_completed = False

    def add_item(self, item: Orderable, quantity: int = 1):
        # TODO: Добавить логику для добавления элемента в заказ.
        # Если элемент уже есть в заказе, увеличить его количество.
        # Если нет, добавить новый.
        # Убедитесь, что item соответствует протоколу Orderable с помощью isinstance().
        if not isinstance(item, Orderable):
            raise TypeError("Добавляемый элемент должен соответствовать протоколу Orderable.")
        print(f"Adding {quantity}x {item.name} to {self.customer_name}'s order.")  # Временная заглушка

    def get_total_price(self) -> float:
        total = 0.0
        # TODO: Подсчитать общую стоимость заказа.
        # Убедиться, что учтено количество каждого элемента, используя get_item_price_with_quantity.

        return total

    def __str__(self) -> str:
        items_str = ", ".join([f"{item.name} x {qty}" for item, qty in self.items])
        status = "Завершен" if self.is_completed else "В процессе"
        return f"Заказ для {self.customer_name}. Элементы: {items_str}. Всего: ${self.get_total_price():.2f}. Статус: {status}"


class Cafe:
    def __init__(self, name: str):
        self.name = name
        # Словарь: {menu_item_name: Product_object} - теперь типизирован протоколом
        self.menu: Dict[str, Product] = {}
        self.orders: List[Order] = []

    def add_menu_item(self, item: Product):
        # TODO: Добавить элемент меню.
        # Убедиться, что не добавляются дубликаты по имени.
        # Убедитесь, что item соответствует протоколу Product с помощью isinstance().
        if not isinstance(item, Product):
            raise TypeError("Добавляемый элемент должен соответствовать протоколу Product.")
        print(f"Adding {item.name} to menu.")  # Временная заглушка

    def create_order(self, customer_name: str) -> Order:
        new_order = Order(customer_name)
        self.orders.append(new_order)
        print(f"Создан новый заказ для клиента: {customer_name}. ID заказа: {len(self.orders) - 1}")
        return new_order

    def process_order(self, order_id: int) -> bool:
        # TODO: Отметить заказ как завершенный по его ID (индексу в списке orders).
        # Проверить, что order_id действителен и заказ ещё не завершен.
        # Возвращает True, если успешно, False в противном случае.
        print(f"Processing order with ID: {order_id}")  # Временная заглушка
        return False

    def list_all_orders(self):
        print(f"\n--- Заказы в {self.name} ---")
        if not self.orders:
            print("Заказов пока нет.")
            return
        for i, order in enumerate(self.orders):
            print(f"[{i}] {order}")
        print("--------------------------")

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        # Дополнительная функция: получить заказ по ID
        if 0 <= order_id < len(self.orders):
            return self.orders[order_id]
        return None


# --- Код для тестирования (не менять, использовать для проверки) ---
if __name__ == "__main__":
    my_cafe = Cafe("Уютное Кафе")

    # Добавление элементов в меню
    latte = MenuItem("Латте", 3.50)
    croissant = MenuItem("Круассан", 2.00)
    sandwich = MenuItem("Сэндвич", 7.80)
    water = MenuItem("Вода", 1.50)

    my_cafe.add_menu_item(latte)
    my_cafe.add_menu_item(croissant)
    my_cafe.add_menu_item(sandwich)
    my_cafe.add_menu_item(water)
    my_cafe.add_menu_item(MenuItem("Латте", 4.00))  # Попытка добавить дубликат

    print("--- Меню ---")
    for item_name, item_obj in my_cafe.menu.items():
        print(item_obj)
    print("------------")

    # Создание заказов
    order1 = my_cafe.create_order("Анна")
    order1.add_item(my_cafe.menu.get("Латте"), 2)
    order1.add_item(my_cafe.menu.get("Круассан"), 1)

    order2 = my_cafe.create_order("Иван")
    order2.add_item(my_cafe.menu.get("Сэндвич"), 1)
    order2.add_item(my_cafe.menu.get("Вода"), 3)
    order2.add_item(my_cafe.menu.get("Латте"), 1)  # Добавление нового элемента
    order2.add_item(my_cafe.menu.get("Сэндвич"), 1)  # Повторное добавление (должно увеличить кол-во)

    my_cafe.list_all_orders()

    # Обработка заказов
    print(f"\nОбработка заказа [0]: {my_cafe.process_order(0)}")
    print(f"Обработка заказа [0] еще раз: {my_cafe.process_order(0)}")  # Повторная попытка
    print(f"Обработка несуществующего заказа [99]: {my_cafe.process_order(99)}")

    my_cafe.list_all_orders()

    # Проверка доступности элементов
    print(f"\nОбщая стоимость заказа 1: ${order1.get_total_price():.2f}")
    print(f"Общая стоимость заказа 2: ${order2.get_total_price():.2f}")

    # Проверка, что MenuItem соответствует протоколам во время выполнения
    print(f"\nMenuItem соответствует Product: {isinstance(latte, Product)}")
    print(f"MenuItem соответствует Orderable: {isinstance(latte, Orderable)}")
