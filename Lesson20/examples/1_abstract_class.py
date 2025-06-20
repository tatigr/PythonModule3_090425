from abc import ABC, abstractmethod


# Определяем абстрактный базовый класс
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры."""
        pass  # Абстрактный метод не имеет реализации

    @abstractmethod
    def perimeter(self):
        """Вычисляет периметр фигуры."""
        pass  # Абстрактный метод не имеет реализации

    def describe(self):
        """Неабстрактный метод, который может быть унаследован или переопределен."""
        print("Это геометрическая фигура.")


# Пытаемся инстанцировать абстрактный класс (вызовет ошибку)
# try:
#     my_shape = Shape()
# except TypeError as e:
#     print(f"Ошибка: {e}")

# Конкретный подкласс Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self_):
        return 2 * 3.14159 * self_.radius


# Конкретный подкласс Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Создаем объекты конкретных классов
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Площадь круга: {circle.area()}")
print(f"Периметр круга: {circle.perimeter()}")
circle.describe()

print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Периметр прямоугольника: {rectangle.perimeter()}")
rectangle.describe()


# Пример класса, который не реализует все абстрактные методы
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Попытка инстанцировать Triangle вызовет ошибку, так как perimeter не реализован
try:
    triangle = Triangle(3, 4)
except TypeError as e:
    print(f"\nОшибка при создании Triangle: {e}")
