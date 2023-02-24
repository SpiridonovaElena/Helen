# 7 Д/з

# # 1. Допишите скрипт для расчета средней температуры
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = len(week_temp)
# mean_temp = sum_temp / days
# print(int(mean_temp))
#              # ПОПРОБОВАЛА И ТАК...
# week_temp = tuple([26, 29, 34, 32, 28, 26, 23])
# sum_temp =0
# for i in week_temp:
#     if i >=0:
#         sum_temp += i
# print("Сумма температур за неделю:", sum_temp, "градусов")
# print("Средняя температура:", sum_temp//len(week_temp), "градусов")
#
# # 2. Найти самое длинное слово в кортеже ('a', 'z', 'hello_world!')
# world = ('a', 'z', 'hello_world!')
# print(max(world,key=len))

# 3. Преобразовать текст в кортеж слов с удалением знаков препинания.
# if i in ''' :;[]{}=+-_"' '''

list_1 ='Hello!"Вау";кто?КАК!?'
punctuation = '''."",?!&()[]{}\+-*=;:><%'''
list_2 = []
no_punct = " "
for i in list_1:
    if i in punctuation:
       i = no_punct
    list_2.append(i)
print(" ".join(list_2))
print(tuple(list_2))
