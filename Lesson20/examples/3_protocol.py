from typing import Protocol, runtime_checkable

# --- 1. Определение Протокола ---
@runtime_checkable
class Counter(Protocol):
    """
    Протокол для объектов, которые могут увеличивать значение
    и возвращать текущее состояние.
    """
    def increment(self) -> None:
        """Увеличивает счетчик на единицу."""
        ... # Заглушка, показывает, что метод должен быть реализован

    def get_count(self) -> int:
        """Возвращает текущее значение счетчика."""
        ...

# 2. Классы, соответствующие Протоколу (без наследования)
class SimpleCounter:
    """Простой счетчик, реализованный как обычный класс."""
    def __init__(self):
        self._count = 0

    def increment(self) -> None:
        self._count += 1
        print(f"SimpleCounter: {self._count}")

    def get_count(self) -> int:
        return self._count

class DatabaseCounter:
    """Счетчик, имитирующий хранение значения в базе данных."""
    def __init__(self, initial_value: int = 0):
        # В реальной жизни здесь было бы подключение к БД
        self._db_value = initial_value
        print(f"DatabaseCounter: Инициализирован со значением {self._db_value}")

    def increment(self) -> None:
        self._db_value += 1
        print(f"DatabaseCounter: {self._db_value}")

    def get_count(self) -> int:
        return self._db_value

# 3. Функция, использующая Протокол
def use_counter(counter_obj: Counter, operations: int) -> None:
    """
    Принимает любой объект, соответствующий протоколу Counter,
    и выполняет на нем операции инкремента.
    """
    print(f"\nИспользуем счетчик типа: {type(counter_obj).__name__}")
    print(f"Начальное значение: {counter_obj.get_count()}")
    for _ in range(operations):
        counter_obj.increment()
    print(f"Конечное значение: {counter_obj.get_count()}")

# 4. Демонстрация
if __name__ == "__main__":
    simple_c = SimpleCounter()
    db_c = DatabaseCounter(10)

    # Используем оба счетчика через функцию, типизированную протоколом
    use_counter(simple_c, 3)
    use_counter(db_c, 2)

    # Проверка соответствия протоколу во время выполнения
    print("\n--- Проверка типов во время выполнения ---")
    print(f"SimpleCounter соответствует Counter? {isinstance(simple_c, Counter)}")
    print(f"DatabaseCounter соответствует Counter? {isinstance(db_c, Counter)}")

    class NotACounter:
        def do_something(self):
            pass

    not_a_c = NotACounter()
    print(f"NotACounter соответствует Counter? {isinstance(not_a_c, Counter)}")

    # MyPy (статический анализатор) выдаст ошибку здесь:
    # Argument "counter_obj" to "use_counter" has incompatible type "NotACounter";
    # expected "Counter"
    # use_counter(not_a_c, 1)