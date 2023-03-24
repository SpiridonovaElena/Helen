# EXAMEN №3

# 1.	Создайте класс "Студент", который имеет атрибуты имя и возраст, а также методы
# "изменить_имя" и "изменить_возраст". Напишите функцию, которая создает объект класса "Студент",
# запрашивая у пользователя его имя и возраст, а затем предлагает пользователю изменить
# имя и возраст.
#
# class Student:
#     name = None
#     age = None
#     def change_name(self):
#         print(input('Введите другое имя:'))
#     def change_age(self):
#         print(input('Введите другой возраст:'))
#
#     def greet(self,name,age):
#         self.name = name
#         self.age = age
#         print(f'Ваше имя: {self.name}, Ваш возраст:{self.age}')
# student = Student()
# student.greet('Helen',25)
# student.change_name()
# student.change_age()


# 2.	Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов
# всех четных чисел в списке.
# def get_even_numbers(numbers):
#     even_numbers = []
#     for i in numbers:
#         if i % 2 == 0:
#             even_numbers.append(i)
#     return (sum(i **2 for i in even_numbers))
# numbers = [1,2,6,5,8,4]
# print(get_even_numbers(numbers))


# 3.	Создайте класс "Калькулятор", который имеет атрибуты "значение" и методы "сложить",
# "вычесть", "умножить" и "разделить". Напишите функцию, которая создает объект класса
# "Калькулятор" и позволяет пользователю выполнить несколько арифметических операций с его помощью.

# class Calculator:
#     a = float(input('Введите первое число:'))
#     b = float(input('Введите второе число:'))

#     def add(self):
#         return self.a + self.b

#     def sub(self):
#         return self.a - self.b

#     def mult(self):
#         return self.a * self.b

#     def div(self):
#         return self.a / self.b
#
# sign = input('Введите операцию(+-*/):')
# calculator = Calculator()
# if sign == "/": print(calculator.div())
# elif sign == "+": print(calculator.add())
# elif sign == "-": print(calculator.sub())
# elif sign == "*": print(calculator.mult())
# else: print('Такой операции нет')



# 4.	Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска",
# "цвет" и метод "описание", который выводит описание автомобиля в виде строки.
# Напишите функцию, которая создает объект класса "Автомобиль", запрашивая у пользователя
# информацию о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.

# class Car:
#     marka = 'volkswagen passat B3'
#     model ='universal'
#     year = 1993
#     color ='white'

#     def description(self):
#         print(f'Марка:{Car.marka}, модель: {Car.model}, год выпуска:{Car.year},цвет:{Car.color}')

#     def create_car(self):
#         print(f'Ваша марка автомобиля:{B3.marka}, модель: {B3.model}, год выпуска:{B3.year},цвет:{B3.color}')
#
# B3 = Car
# B3.description(1)

# B3.marka = input('Введите марку автомобиля:')
# B3.model = input('Введите модель автомобиля:')
# B3.year = int(input('Введите год автомобиля:'))
# B3.color = input('Введите цвет автомобиля:')
# B3.create_car(1)

# 5.	Создайте класс "Сотрудник", который имеет атрибуты "имя", "фамилия", "должность" и метод
# "описание", который выводит описание сотрудника в виде строки. Создайте класс "Отдел",
# который имеет атрибуты "название" и "список_сотрудников", а также методы "добавить_сотрудника"
# и "удалить_сотрудника". Напишите функцию, которая создает объект класса "Отдел",
# запрашивая у пользователя его название, а затем предлагает пользователю добавить
# несколько сотрудников в отдел, после чего выводит список всех сотрудников в отделе
# и их описания. Затем функция предлагает пользователю удалить одного из сотрудников и
# выводит обновленный список сотрудников и их описания.

# class Sotrudnik():
#     name = input('Ваше имя:')
#     surname = input('Ваша фамилия: ')
#     dolghnost = input('Ваша должность: ')
#     # @ abstractmethod
#     def description(self):
#         print(f'Имя-{Sotrudnik.name}, Фамилия- {Sotrudnik.surname}, Должность-{Sotrudnik.dolghnost}')
# class Otdel(Sotrudnik):
#     title = None # (название)
#     list_sotrudnik = None
#
#     def __init__(self, name, surname, dolghnost):
#         self.name = name
#         self.surname = surname
#         self.dolghnost = dolghnost
#
#     def add_sotrudnika(self):
#         print(input(f'Добавьте несколько сотрудников в отдел: {self.name},{self.surname},{self.dolghnost}'))
#     def delete_sotrudnika(self):
#         print(input(f'Удалите одного из сотрудников:{self.name},{self.surname},{self.dolghnost}'))
#
#
# chel = Sotrudnik()
# chel.description()
# chel1 = Otdel('анна', 'котяк', 'врач')
# chel1.add_sotrudnika()
# chel1.delete_sotrudnika()

# С ЭТОЙ ЗАДАЧЕЙ ПРОБЛЕМНО, Я ПРОБОВАЛА ЗАВОДИТЬ НАЗВАНИЯ ЧЕРЕЗ СПИСОК, СЛОВАРЬ, АРГСЫ И КРАВГСЫ, МОЖЕТ
#ПРОСТО НИ ТАК СТАВЛЮ, НО...