def function(x):
    if isinstance(x, tuple):
        return "Длина всех строк:",sum([len(x)])
    elif isinstance(x, list):
        print("Количество букв:", sum(map(str.isalpha, x)))
        print("Количество цифр:", sum(map(str.isdigit, x)))
    elif isinstance(x, int):
        return "Количество нечетных цифр:",len([i for i in str(x) if i in '13579'])
    elif isinstance(x, str):
        return ("Количество букв:", sum(map(str.isalpha, x)))
    else:
      print("Укажите верные данные:")
print(function([1,2,3,'a','bc8?']))
print(function((1,2,3,'a','bc8?',7,8,9)))
print(function(38555))
print(function('k55l2p'))
