import l8_1
from random import randint
'''Задача 2'''
class Student(l8_1.Human):
    def __init__(self,weight,gender,age,name,numberHomework):
        self.numberHomework=numberHomework
        super().__init__(weight,gender,age,name)

    def __lt__(self, other):
        '''Перегрузка - <'''
        return self.numberHomework<other.numberHomework
    def __le__(self,other):
        '''Перегрузка - <='''
        return self.numberHomework<=other.numberHomework
    def __eq__(self,other):
        '''Перегрузка - =='''
        return self.numberHomework==other.numberHomework
    def __gt__(self,other):
        '''Перегрузка - >'''
        return self.numberHomework>other.numberHomework
    def __ge__(self,other):
        '''Перегрузка - >='''
        return self.numberHomework>=other.numberHomework
    def getInfo(self):
        '''Функция для вывода информации'''
        print(' Класс:', self.clas_s,
              '\n Вид:', self.type,
              '\n Имя:', self.name,
              '\n Количество сданных дз:',self.numberHomework,
              '\n Вес:', self.weight,
              '\n Пол:', self.gender,
              '\n Возраст', self.age, '\n')
print('Зание 3:')
S1=Student(80,'M',20,'Иван',randint(5,10))
S2=Student(75,'Ж',19,'Карина',randint(5,10))
S1.getInfo()
S2.getInfo()
if S1==S2:
    print('У студентов одинаковое кол-во сданных дз!')
elif S1<S2:
    print('У первого студента меньше сданных дз!')
else:
    print('У второго студента меньше сданных дз!')