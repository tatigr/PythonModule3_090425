# "Сортировка собак"
# Создайте список объектов класса Dog. Отсортируйте этот список по возрасту (от самого молодого до самого старого).

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
        return f"Dog: {self.name} | {self.breed} | {self.age}"


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

dogs.sort(key=lambda dog: dog.age)

print(dogs)