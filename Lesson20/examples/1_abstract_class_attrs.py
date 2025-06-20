from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Абстрактный базовый класс для животных.
    Требует обязательные свойства 'name' и 'species'.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Обязательное свойство: имя животного."""
        pass  # Заглушка, реализация должна быть в подклассах

    @property
    @abstractmethod
    def species(self) -> str:
        """Обязательное свойство: вид животного."""
        pass  # Заглушка

    @abstractmethod
    def make_sound(self) -> str:
        """Обязательный абстрактный метод: издает звук."""
        pass

    def describe(self) -> None:
        """Неабстрактный метод: описывает животное."""
        print(f"Это {self.species}, по имени {self.name}.")


# --- Конкретный класс, реализующий все обязательные элементы ---
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        self._name = name
        self._breed = breed

    @property
    def name(self) -> str:
        return self._name

    @property
    def species(self) -> str:
        return "Собака"

    def make_sound(self) -> str:
        return "Гав-гав!"


# --- Класс, который НЕ реализует все обязательные атрибуты ---
class Cat(Animal):
    def __init__(self, name: str):
        self._name = name
        # Отсутствует свойство 'species'

    @property
    def name(self) -> str:
        return self._name

    # Метод make_sound реализован, но свойство species отсутствует
    def make_sound(self) -> str:
        return "Мяу!"


# --- Демонстрация ---
if __name__ == "__main__":
    # Попытка инстанцировать абстрактный класс (вызовет TypeError)
    try:
        my_animal = Animal()
    except TypeError as e:
        print(f"Ошибка при создании Animal: {e}")

    # Создаем объект Dog - все обязательные свойства и методы реализованы
    my_dog = Dog("Рекс", "Немецкая овчарка")
    my_dog.describe()
    print(f"{my_dog.name} говорит: {my_dog.make_sound()}")

    # Попытка создать объект Cat (вызовет TypeError, т.к. отсутствует 'species')
    try:
        my_cat = Cat("Мурка")
        # Эта строка не будет достигнута, если не реализовано свойство species
        my_cat.describe()
    except TypeError as e:
        print(f"\nОшибка при создании Cat: {e}")
        print("Cat не может быть инстанцирован, так как не реализовал все абстрактные свойства.")


    # Если бы Cat реализовал 'species':
    class ValidCat(Animal):
        def __init__(self, name: str):
            self._name = name

        @property
        def name(self) -> str:
            return self._name

        @property
        def species(self) -> str:  # Теперь свойство species реализовано
            return "Кошка"

        def make_sound(self) -> str:
            return "Мяу!"


    print("\n--- Корректная кошка ---")
    valid_cat = ValidCat("Пушок")
    valid_cat.describe()
    print(f"{valid_cat.name} говорит: {valid_cat.make_sound()}")
