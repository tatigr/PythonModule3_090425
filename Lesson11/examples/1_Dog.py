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


dog1 = Dog("Buddy", "Retriever", 3)
dog2 = Dog("Lucy", "Labrador", 2)

print(dog1.__dict__)
dog1.color = "black"
dog1._Dog__is_hungry = False

print(dog1.__dict__)
# print(dog2.__dict__)
# print(Dog.__dict__)

dog1.eat("meat")
Dog.eat(dog1, "meat")