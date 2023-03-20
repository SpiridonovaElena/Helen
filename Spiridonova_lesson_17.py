# Д/З №17
# В задаче про класс Human дописать 2 класса: класс House для создания дома,
# класс Buy_House для его покупки. Для того, чтобы в классе Human свойство __house сделать True,
# нужно использовать наследование классов. Но каких? :)


class Human:
    default_name = 'USER'
    default_age = None

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__house = False
        self.__money = 0

    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}, наличие дома: {self.__house}, денег: {self.__money}')
    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}, возраст по умолчанию: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Получили {amount} рублей. Текущий счет: {self.__money} рублей')

class House(Human):
    stena = 'Брус'
    material_krishi = 'Черепица'
    kolvo_okon = 10
    kolvo_dverei = 6
    def postroit(self):
        print("Построил дом")
class Buy_House(Human):
    def __init__(self, t):
        super().__init__(t)
        self.__house = True
    def buy(self):
         print(f'наличие дома:{self.__house}')

Human.default_info()
Evgeniy = Human('Евгений',29)
Evgeniy.info()
Evgeniy.earn_money(100)
Evgeniy.info()
print(Evgeniy._Human__money)
House.postroit(1)
Y = Buy_House(1)
Y.buy()
