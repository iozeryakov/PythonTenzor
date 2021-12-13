import l8_1
'''Задача 2'''
class Student(l8_1.Human):
    def __init__(self,weight,gender,age,name,numberHomework):
        self.numberHomework=numberHomework
        super().__init__(weight,gender,age,name)

    def getInfo(self):
        '''Функция для вывода информации'''
        print(' Класс:', self.clas_s,
              '\n Вид:', self.type,
              '\n Имя:', self.name,
              '\n Количество сданных дз:',self.numberHomework,
              '\n Вес:', self.weight,
              '\n Пол:', self.gender,
              '\n Возраст', self.age, '\n')
print('Зание 2:')
S=Student(80,'M',20,'Иван',8)
S.getInfo()