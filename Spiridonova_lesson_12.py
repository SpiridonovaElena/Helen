# Д/З №12
# 1. Напишите функцию, которая принимает на вход два аргумента и
# возвращает их сумму.

# def summa(a, b):
#   return a+b
# s = summa(int(input("Введите первое число:")), int(input("Введите второе число:")))
# print("Результат:", s)

# 2. Напишите функцию, которая принимает на вход список чисел
# и возвращает их среднее значение.
# def Spisok (L):
#     summa = 0
#     for i in L:
#         summa += int(i)
#     return summa/len(L)
# my_list = list(input("Введите несколько чисел:"))
# print("Среднее значение:", Spisok(my_list))



# 3. Напишите функцию, которая принимает на вход число
# и возвращает True, если оно четное, и False, если оно нечетное.
# def chislo(num):
#     if num % 2 == 0:
#      return True
#     else:
#      return False
# print(chislo(int(input("Введите число:"))))


# 4. Напишите функцию, которая принимает на вход список
# и возвращает новый список, содержащий только уникальные элементы
# из исходного списка.
# def list(l):
#     a = []
#     for i in l:
#         if i not in a:
#             a.append(i)
#     return a
# print(list(input("Введите несколько чисел:")))


# 5. Решите задачу с использованием вложенной функции is_square.
# Предположим, у нас есть список чисел и мы хотим найти все числа,
# которые являются квадратами других чисел в этом списке.
# def find_square_numbers(numbers):
#     def is_square(number):
#         return number**0.5 in numbers
#     new_list = []
#     for i in numbers:
#         if is_square(i): new_list.append(i)
#     return new_list
#
# print(find_square_numbers([1,3,2,5,6,7,8,9]))

