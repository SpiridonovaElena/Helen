# Д/з №14

# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0 букв
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой тип данных
def Tip (fn):
    def wrapper(W):
        print(f"Введенный тип данных:{type(W)}")
        return fn(W)
    return wrapper
@Tip
def function (x):
    if isinstance(x, tuple):
        len_count_string = 0 # Счетчик длины всех строк
        for i in x:
            if type(i) is str: len_count_string += len(i)
        return f"Длина всех строк: {len_count_string}"
    elif isinstance(x, list):
        letters = 0 # Счетчик букв
        numbers = 0 # Счетчик цифр
        for i in str(x):
            if i.isalpha():
                letters +=1
            if i.isdigit():
                numbers +=1
        return f"Количество букв:{letters} Количество цифр: {numbers}"
    elif isinstance(x, int):
        return f"Количество нечетных цифр: {len([i for i in str(x) if i in '13579'])}"
    elif isinstance(x, str):
        return f"Количество букв: {len([i for i in x if str(i).isalpha()])}"
    else:
      print("Укажите верные данные:")
print(function([1,2,3,'a',8,'bc8?']))
print(function((1,2,3,'a','bc8?',7,8,9)))
print(function(38525))
print(function('k55l2p'))

