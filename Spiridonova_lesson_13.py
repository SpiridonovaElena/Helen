# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)
#Шаблон:
# def is_palindrome(stroka):
#     if len(stroka) < 2:
#         return True
#     elif stroka[0] != stroka[-1]:
#         return False
#     else:
#         return is_palindrome(stroka[1:-1])
# a = str(input("Введите строку:"))
# if (is_palindrome(a) == True):
#     print("Данная строка палиндром!")
# else:
#     print("Данная строка не палиндром!")


#2. Написать рекурсивную функцию для подсчета количества элементов в списке.

# def list1(list):
#   if list == []:
#     return 0
#   else:
#     return count(list[1:])
#
#     print(list1(int(input("Введите несколько элементов:"))))

# def list(l):
#     if not l:
#         return 0
#     return 1 + list(l[1:])
# a = [1, 2, 3,5,8,9]
# print("Длина списка равна: ",list(a))


#3. Этот код отсортирует список строк по последнему символу в каждой строке.
    # Здесь использована лямбда-функция в качестве ключа в сортировке.
# strings = ['apple', 'banana', 'cherry', 'date']
# sorted_strings = sorted(strings, key=lambda s: s[-1])
# print(sorted_strings) # Output: ['cherry', 'date', 'apple', 'banana']

# Измените код так, чтобы сортировка была по второму символу каждой строки
# strings = ['apple', 'banana', 'cherry', 'date']
# sorted_strings = sorted(strings, key=lambda s: s[1])
# print(sorted_strings)
#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.
# def make_adder(a):
#    def adder(b):
#        return a+b
#    return adder
# print("Сумма:",make_adder(3)(9))




#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.

# def counter(n):
#     return range(1, n + 1)  #Здесь range как встроенная функция
# print(counter(7))
