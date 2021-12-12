'''Задача 1'''
class Animals:
    '''Класс животные с минимальным общим кол-м признаков!'''
    def __init__(self,weight,gender,age):
        self.weight=weight
        self.gender=gender
        self.age=age
class Mammals(Animals):
    '''Класс млекопитающие (наследник животных) с минимальным общим кол-м признаков!'''
    def __init__(self,weight,gender,age):
        self.clas_s='Млекопитающее'
        super().__init__(weight,gender,age)
class Human(Mammals):
    '''Класс Человек(наследник млекопитающего) с минимальным общим кол-м признаков!'''
    def __init__(self,weight,gender,age,name,amountOfMoney):
        self.type='Человек'
        self.name=name
        self.amountOfMoney=amountOfMoney
        super().__init__(weight,gender,age)
    def getInfo(self):
        '''Функция для вывода информации'''
        print(' Класс:', self.clas_s,
            '\n Вид:', self.type,
            '\n Имя:', self.name,
            '\n Кол-во денег:', self.amountOfMoney,
            '\n Вес:',self.weight,
            '\n Пол:',self.gender,
            '\n Возраст',self.age,'\n')
class Cat(Mammals):
    '''Класс Кошка(наследник млекопитающего) с минимальным общим кол-м признаков!'''
    def __init__(self,weight,gender,age,breed,name,woolLength):
        self.type = 'Кошка'
        self.name=name
        self.breed=breed
        self.woolLength=woolLength
        super().__init__(weight,gender,age)
    def getInfo(self):
        '''Функция для вывода информации'''
        print(' Класс:', self.clas_s,
            '\n Вид:', self.type,
            '\n Порода:', self.breed,
            '\n Кличка:', self.name,
            '\n Длина шерсти:', self.woolLength,
            '\n Вес:', self.weight,
            '\n Пол:', self.gender,
            '\n Возраст', self.age,'\n')
class Dog(Mammals):
    '''Класс Собака(наследник млекопитающего) с минимальным общим кол-м признаков!'''
    def __init__(self,weight,gender,age,breed,name,woolLength):
        self.type = 'Собака'
        self.name=name
        self.breed=breed
        self.woolLength=woolLength
        super().__init__(weight,gender,age)
    def getInfo(self):
        '''Функция для вывода информации'''
        print(' Класс:',self.clas_s,
              '\n Вид:',self.type,
              '\n Порода:',self.breed,
              '\n Кличка:',self.name,
              '\n Длина шерсти:',self.woolLength,
              '\n Вес:', self.weight,
              '\n Пол:', self.gender,
              '\n Возраст', self.age,'\n')
print('Зание 1:')
H=Human(80,'М',20,'Иван',54415)#рандомное число
D=Dog(20,'М',3,'Пикинес','Ричард',10)
C=Cat(10,'Ж',5,'Мейн-кун','Саймон',5)
H.getInfo()
D.getInfo()
C.getInfo()