from pprint import pprint

class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self) -> str:
        return f"{self.surname} {self.name}"


# Совет: не забывайте, вы можете добавлять в список и удалять из него любых людей, это просто пример!
peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 27),
    People("Ольга", "Подгорная", 32),
    People("Петр", "Иванов", 32),
    People("Кирилл", "Подгорный", 30),
    People("Анна", "Подгорная", 39),
]

# TODO-1: найдите самого молодого человека и выведите его Фамилию и Имя
#  Примечание: Если самых молодых несколько, выведите всех
youngest_people = min(peoples, key=lambda people: people.age)
for people in peoples:
    if people.age == youngest_people.age:
        print(people.full_name())

# TODO-2: найдите всех одногодок и выведите их Фамилии и Имена
#  Примечание: Если одногодок нет, выведите сообщение "одногодок нет"
peoples_age = {}
for people in peoples:
    if people.age in peoples_age.keys(): # уже есть человек с таким возрастом
        peoples_age[people.age].append(people)
    else: # Впервые встречаем человека с таким возрастом
        peoples_age[people.age] = [people]

for people_list in peoples_age.values():
    if len(people_list) > 1:
        for people in people_list:
            print(f"{people.name} {people.surname} {people.age}")