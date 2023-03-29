# EXAMEN №3

# 1.	Создайте класс "Студент", который имеет атрибуты имя и возраст, а также методы
# "изменить_имя" и "изменить_возраст". Напишите функцию, которая создает объект класса "Студент",
# запрашивая у пользователя его имя и возраст, а затем предлагает пользователю изменить
# имя и возраст.
#
# class Student:
#     name = 'Юрий'
#     age = 26
#     def change_name(self):
#         print(input('Введите другое имя:'))
#     def change_age(self):
#         print(input('Введите другой возраст:'))
# def func():
#    student = Student()
#    student.change_name()
#    student.change_age()
# print(f'Ваше имя: {Student.name} и возраст: {Student.age}')
# func()

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
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mult(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
# def func():
#     chislo = Calculator()
#     znak = input('Введите операцию(+-*/):')
#     if znak == "/": print(chislo.div())
#     elif znak == "+": print(chislo.add())
#     elif znak == "-": print(chislo.sub())
#     elif znak == "*": print(chislo.mult())
#     else: print('Такой операции нет')
# func()


# 4.	Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска",
# "цвет" и метод "описание", который выводит описание автомобиля в виде строки.
# Напишите функцию, которая создает объект класса "Автомобиль", запрашивая у пользователя
# информацию о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.
#
# class Car:
#     marka = 'volkswagen passat B3'
#     model ='universal'
#     year = 1993
#     color ='white'
#
#     def description(self):
#         print(f'Марка:{Car.marka}, модель: {Car.model}, год выпуска:{Car.year},цвет:{Car.color}')
#
# def func():
#     auto = Car()
#     auto.marka = input('Введите марку автомобиля:')
#     auto.model = input('Введите модель автомобиля:')
#     auto.year = int(input('Введите год автомобиля:'))
#     auto.color = input('Введите цвет автомобиля:')
#     print(f'Марка:{auto.marka}, модель: {auto.model}, год выпуска:{auto.year},цвет:{auto.color}')
# Car.description(1)
# func()


# 5.	Создайте класс "Сотрудник", который имеет атрибуты "имя", "фамилия", "должность" и метод
# "описание", который выводит описание сотрудника в виде строки. Создайте класс "Отдел",
# который имеет атрибуты "название" и "список_сотрудников", а также методы "добавить_сотрудника"
# и "удалить_сотрудника". Напишите функцию, которая создает объект класса "Отдел",
# запрашивая у пользователя его название, а затем предлагает пользователю добавить
# несколько сотрудников в отдел, после чего выводит список всех сотрудников в отделе
# и их описания. Затем функция предлагает пользователю удалить одного из сотрудников и
# выводит обновленный список сотрудников и их описания.
#
# class Sotrudnik:
#     name = 'USERNAME'
#     surname = None
#     dolghnost = None
#     def description(self):
#         print(f'Имя-{Sotrudnik.name}, Фамилия- {Sotrudnik.surname}, Должность-{Sotrudnik.dolghnost}')
# class Otdel:
#     title = None # (название)
#     list_sotrudnik = []
#
#     def add_sotrudnika(self,name_s):
#         self.list_sotrudnik.append(name_s)
#     def delete_sotrudnika(self,name_s):
#         self.list_sotrudnik.remove(name_s)
# def creat_sort(dep_name):
#     dep_object = Otdel()
#     dep_object.department_name = dep_name
#     a = input('Хотите ли добавить сотрудника? ')
#     if a: dep_object.add_sotrudnika(input('Введите имя: '))
#     print(dep_object.list_sotrudnik)
#     b = input('Хотите ли удалить сотрудников?')
#     if b: dep_object.delete_sotrudnika(input('Введите имя: '))
#     print(dep_object.list_sotrudnik)
#
# creat_sort('Ambulance')
