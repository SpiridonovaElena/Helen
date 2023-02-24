# # Задание №1
#
# age = int (input("Введите год"))
# if (age % 400 ==0 or age % 100 !=0) and age % 4 ==0:
#     print("Высокосный")
# else:
#     print("Не высокосный")

#
# # Задание №2
#
# a = int(input("a="))
# b = int(input("b="))
# c = int(input('c='))
# if a + b > c and b + c > a and c + a > b:
#     print(" Верно")
# else:
#     print("Не верно")
#
# Задание №3

# x = float(input("x="))    # Координаты оси Х к точке
# y = float(input("y="))    # Координаты оси У к точке
# r = float(input("r="))   # Радиус окружности
# if x**2+y**2>r**2:
#     print("Точка лежит снаружи")
# else:
#     print("Точка лежит внутри")


 # 4. Придумать свою задачу на тему if-elif-else
number = int(input("Введите число от 0 до 10:"))
b = 7
if number < b:
    print("Не угадали!")
elif number > b:
    print("Не угадали!")
else:
 print(" Поздравлям! Вы угадали.")