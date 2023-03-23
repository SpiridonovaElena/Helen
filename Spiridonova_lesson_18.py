# Написать программу для учета животных в зоопарке
# В родительском абстрактном классе Animals создать абстрактные методы для любого животного
# От родительского класса наследовать классы для конкретных видов животных
# Также использовать полиморфизм, инкапсуляцию
# При печати объектов определенного класса выводить информацию об этом объекте.
from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def inhabit(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def drink(self):
        pass
class Birds(Animals):
    def __init__(self, name, eat, drink):
        self.name = name
        self.eat = eat
        self.drink = drink
def inhabit(self):
     print(f'{self.name}Обитают на земле и воздухе')
     def eat(self):
        print(f'{self.eat}Питаются семечками, орешками, крупами, свежими плодами и ягодами')
     def drink(self):
         print(f'{self.drink} Пьют с помощью клюва')
class Insects(Animals):
    def __init__(self):
     super().__init__()
     def inhabit(self):
         print(" Насекомые освоили практически все пространства земли")

     def eat(self):
         print('Питаются с помощью грызущего ротового аппарата')

     def drink(self):
         print("Всеядны")
class Mammals(Animals):
    def __init__(self):
     super().__init__()

     def inhabit(self):
         print("На земле, в воде и в воздухе")

     def eat(self):
         print("Всеядны")

     def drink(self):
         print("Всеядны")


синица = Birds()
print(синица.eat())