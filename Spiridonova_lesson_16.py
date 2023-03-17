# Д/З № 16
# Калькулятор. Создать класс, где реализованы методы математических операция (+-/*)
# и функция (вне класса) для ввода данных.

class Calculator:
    def __init__(self,a,b):
        self.a = float(input('Введите первое число:'))
        self.b = float(input('Введите второе число:'))
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

sign = input('Введите операцию(+-*/):')
calculator = Calculator(1,2)

if sign == "/": print(calculator.div())
elif sign == "+": print(calculator.add())
elif sign == "-": print(calculator.sub())
elif sign == "*": print(calculator.mult())
else: print('Такой операции нет')
