# Создайте список объектов класса Dog с различными породами и возрастами.
# Необходимо вычислить и вывести средний возраст для каждой уникальной породы, представленной в списке.

# Примечание: исходный класс Dog, можно взять в examples
class Dog:
    species = "Canis familiaris"
    paws = 4

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.__is_hungry = True

    def bark(self):
        print(f"{self.name} says Woof! Woof!")

    def eat(self, food):
        if self.__is_hungry:
            print(f"{self.name} is happily eating {food}.")
            self.__is_hungry = False
        else:
            print(f"{self.name} is not hungry right now.")

    def __repr__(self):
        return f"Dog: {self.name} | {self.breed}"


dogs = [
    Dog("Бадди", "Ретривер", 3),
    Dog("Люси", "Лабрадор", 2),
    Dog("Макс", "Ретривер", 5),
    Dog("Дейзи", "Лабрадор", 1),
    Dog("Чарли", "Бигль", 4),
    Dog("Молли", "Ретривер", 6),
    Dog("Рокки", "Лабрадор", 2),
    Dog("Зои", "Бигль", 7),
    Dog("Купер", "Ретривер", 3),
    Dog("Сади", "Лабрадор", 1)
]

dogs_breeds = {}

for dog in dogs:
    if dog.breed in dogs_breeds.keys():
        dogs_breeds[dog.breed].append(dog)
    else:
        dogs_breeds[dog.breed] = [dog]

print(dogs_breeds)
...