# Д/З № 16
# Калькулятор. Создать класс, где реализованы методы математических операция (+-/*)
# и функция (вне класса) для ввода данных.


class Calculator:
    a = float(input('Введите первое число:'))
    b = float(input('Введите второе число:'))
    sign = str(input('Введите операцию(+-*/):'))
    def add(self, a, b):
        if  sign == '+': print(a+b)
        return a+b
    def sub(self, a, b):
        if sign == '-': print(a-b)
        return a - b
    def mult(self, a, b):
        if sign == '*':print(a*b)
        return (a,"*",b)
    def div(self, a, b):
        if b!= 0: print(a/b)
        return (a,"/", b)
        # else:
        # print (a, "/",b,'На ноль делить нельзя!')

calculator = Calculator()
a = Calculator().a
b = Calculator().b
sign = Calculator().sign
calculator.div(a,b)
calculator.add(a,b)
calculator.sub(a,b)
calculator.mult(a,b)
