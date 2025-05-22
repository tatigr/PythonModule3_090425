import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Circle:
    def __init__(self, center_coords: tuple, radius: int):
        self.center_coords = Point(*center_coords)
        self.radius = radius

    def length(self):
        """
        :return: длину окружности
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        :return: площадь окружности
        """
        return math.pi * self.radius ** 2

    def move(self, new_coord):
        self.center_coords = Point(*new_coord)


# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)

print(f"Длина окружности радиусом {...} = {...}")
print(f"Длина окружности радиусом {...} = {...}")

print(f"Площадь окружности радиусом {...} = {...}")
print(f"Площадь окружности радиусом {...} = {...}")
