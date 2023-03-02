# # Задача №1
# a = [2,-3,6,1,-5,-8,-4]
# sum = 0
# for i in a:
#     if i >=0 and i % 2 == 0:
#         sum += i
# print("Сумма положительных четных чисел: = ", sum)

# Задача№2
a = [3,6,1,2]
sum = 0
for i in a:
    if i >=0:
        sum += i
print("Сумма =", sum)
print("Средее арифметическое = ", sum/len(a))
for i in a:
    if i < sum/len(a):
        print(i, end=' , ')
