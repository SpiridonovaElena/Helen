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

#IndexError
# try:
#     List = [1,2,'abc']
#     print(List[4])
# except IndexError:
#     print('Нет такого')


# SyntaxError
try:
    a = 1)
    b = 5
    c = a+b
    print(c)
except SyntaxError:
 print('Ошибка в переменной')
else:
    print("Ошибка")
finally:
    print("ОК")

# Почему ошибку видит, но не видит исправления?