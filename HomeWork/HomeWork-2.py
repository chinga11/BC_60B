
class Animal:
    def __init__(self, name:str, age:int , health:int):
        super().__init__()
        self.name = name
        self.age = age
        self.health = health

    def info (self):
       return f"{self.name} , {self.age} лет , {self.health} хп"

    def ability (self):
        return f"{self.name} использует базовую способность "

class Flyable:

    def ability (self):
        return super().ability()+" летает"

class Swimmably:
    def ability (self):
        return super().ability()+" плавает"

class Invisible:
    def ability (self):
        return super().ability()+" становится невидимым"

class Duck(Swimmably, Flyable,Animal):
    def __init__(self, name:str, age:int , health:int):
        super().__init__(name, age,health)

class Bat(Flyable,Invisible,Animal):
    def __init__(self, name:str, age:int , health:int):
        super().__init__(name,age,health)

class Frog(Swimmably, Invisible,Animal):
    def __init__(self, name:str, age:int , health:int):
        super().__init__(name,age,health)

class Fhoenix(Flyable,Invisible,Animal):
    def __init__(self, name:str, age:int , health:int):
        super().__init__(name,age,health)

class Zoo():
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def info (self):

        for i in self.animals:
            print(i.info())

    def ability (self):

        for i in self.animals:
            print(i.ability())

if __name__ == "__main__":
   zoo = Zoo()

   duck = Duck("Дональд", 3, 80)
   bat = Bat("Бэтти", 5, 60)
   frog = Frog("Кермит", 2, 50)
   phoenix = Fhoenix("Феникс", 100, 200)

   for animal in (duck, bat, frog, phoenix):
       zoo.add_animal(animal)

   print("=== Информация о животных ===")
   zoo.info()

   print("\n=== Шоу суперспособностей ===")
   zoo.ability()

   print("\nMRO для Duck:", Duck.__mro__)
   print("MRO для Phoenix:", Fhoenix.__mro__)
