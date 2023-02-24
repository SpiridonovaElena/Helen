# Д/З №10

# 1.
# Матрица 5 х 5.
# 1. Найти строку с максимальной суммой элементов и вывести её НОМЕР (индекс)
# 2. Найти максимальный элемент главной диагонали матрицы.
# 3. Вычислить количество отрицательных элементов ПОД главной диагональю матрицы row>col
# 4. Найти сумму каждой строки
# A = 5
# B = 5
# C = [[0]*B for i in range(A)]
# D = []
# E = 0
# import random
# for i in range(A):
#     for j in range(B):
#         C[i][j] = random.randint(-9,9)
#         print(C[i][j], end='\t')
#     print()
# for i in range(len(C)):
#     D.append((sum(C[i])))
# print(C[D.index(max(D))])
# el = [C[i][j] for i in range(len(C))
#       for j in range(len(C))]
# print('Мах. элемент главной диагонали:',max(el))
# print(sum([C[i][j] for i in range(1,len(C)) for j in range(i)])) # Cчитает сумму всех элементов под главной диагональю,
# for i in range(len(C)):
#     x = sum(C[i])
#     print('Сумма строки:', x)

       # ИЛИ

# M = [
#     [1,2,3],
#     [4,5,6]
# ]
# # print(*M, sep='\n')
# for i in M: #обход по количеству строк
#     for j in i: #обход по количеству столбцов
#         print(j, end=' ')
#     print()
# 1.Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её НОМЕР (индекс)
import random
# my_matrix = [[random.randint(20,100) for j in range(5)] for i in range(5)]
# print(*my_matrix, sep='\n')
# max_sum = sum(my_matrix[0])
# max_row = 0
# for m in range(len(my_matrix)):
#     if sum(my_matrix[m])>max_sum:
#         max_sum = sum(my_matrix[m])
#         max_row = m
# print(max_row)




# 2. Найти максимальный элемент главной диагонали матрицы.
# my_matrix = [[random.randint(20,100) for j in range(5)] for i in range(5)]
# print(*my_matrix, sep='\n')
# max_el = my_matrix[0][0]
# for r in range(len(my_matrix)):
#     if my_matrix[r][r] > max_el:
#         max_el = my_matrix[r][r]
# print(max_el)

# 3. Вычислить количество отрицательных элементов ПОД главной диагональю матрицы row>col
# my_matrix = [[random.randint(-100,100) for j in range(5)] for i in range(5)]
# print(*my_matrix, sep='\n')
# count = 0
# for i in range(len(my_matrix)):
#     for j in range(len(my_matrix[i])):
#         if j<i and my_matrix[i][j]<0:
#             count+=1
# print(count)

#2.
# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль.
# Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
#  Придумать и обработать исключения на TypeError и ValueError, IndexError, SyntaxError,

# while True:
#   try:
#     a = int(input('Введите Делимое число:'))
#     b = int(input('Введите делитель:'))
#     c = a/b
#     print('Частное:', c)
#   except ValueError:
#      print('Введите лучше число')
#   except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#     a = int(input('Введите Делимое число:'))
#     b = int(input('Введите делитель:'))
#     c = a / b
#     print('Частное:', c)


# # TypeError
# try:
#       a = 10
#       b = 'Hello'
#       c = a/b
#       print(c)
# except TypeError:
#       print("Не соответствует")
# finally:
#     print("ОК")

# IndexError
# try:
#     List = [1,2,'abc']
#     print(List[4])
# except IndexError:
#     print('Нет такого')


# SyntaxError
try:
    a = 1)
    b = 5
    c = a + b
    print(c)
except SyntaxError:
    print('Ошибка в переменной')
else:
    print("Ошибка")
finally:
    print("ОК") # Почему ошибку видит, но не видит обход ошибки?