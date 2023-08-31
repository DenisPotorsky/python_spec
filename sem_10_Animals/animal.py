'''
📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
   Задание No6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс
    Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.

📌 Задача 1. Решить задания, которые не успели решить на семинаре.

📌Задача 2. Доработаем задания 5-6. Создайте класс-фабрику.
    - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

📌Задача 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
    которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
    Задания должны решаться через вызов методов экземпляра.
'''


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


class Factory:
    def __init__(self, animal_class, **kwargs):
        self.animal = animal_class
        self.params = kwargs

    def make_animal(self):
        params = list(item for item in self.params.values())
        if self.animal == 'Bird' or 'bird':
            return Bird(*params)
        elif self.animal == "Reptiles" or 'reptiles':
            return Reptiles(*params)
        else:
            return Fish(*params)


class Fish(Animal):

    def __init__(self, name, age, color, fins_count):
        super().__init__(name, age, color)
        self.fins_count = fins_count

    def show_special_attributes(self):
        print(self.fins_count)


class Bird(Animal):

    def __init__(self, name, age, color, can_fly=True):
        super().__init__(name, age, color)
        self.flying = can_fly

    def show_special_attributes(self):
        print(f'can fly = {self.flying}')


class Reptiles(Animal):

    def __init__(self, name, age, color, body_size):
        super().__init__(name, age, color)
        self.size = body_size

    def show_special_attributes(self):
        print(f'length of body = {self.size}')


factory = Factory('bird', name='sd', age=9, color='green', d=False)
animal = factory.make_animal()
print(animal.age)
