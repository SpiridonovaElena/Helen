# №1.
# Есть список состоящий из слов и чисел,
# нужно записать в файл построчно сначала
# слова в порядке их длины, а после слов числа в порядке возрастания.

with open('Lena.txt', 'w', encoding='utf8') as f:
    list = [55, 'Hello', 8, 'Five', 3, 'One', 12]
    chisla = []
    strings = []
    for i in list:
        if type(i) == str:
            strings.append(i)
            strings.sort(key=len)
        else:
            chisla.append(i)
            chisla.sort()
            print(strings,chisla)
    for i in strings:
        f.write(f'{i}\n')
    for i in chisla:
        f.write(f'{i}\n')
# №2.
# Добавьте на свой РАБОЧИЙ СТОЛ папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
# Создаем именно на РАБОЧЕМ СТОЛЕ!!!

import os
os.chdir('C:/Users/sao13/Desktop')
os.mkdir('Helen')
os.makedirs('text_1.txt/text_2.txt/text_3.txt')
os.renames('text_1.txt/text_2.txt/text_3.txt', 'rename_1.txt/rename_2.txt/rename_3.txt')
os.removedirs('rename_1.txt/rename_2.txt/rename_3.txt')
os.rmdir('Helen')
