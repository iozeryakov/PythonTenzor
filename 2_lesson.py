from datetime import datetime #Для второй задачи, решил разнообразить задание)
import math #Для 4 задачи.
#Задание 1
try:
    a,b=map(float,input('Задание 1:\nВведите 2 числа через пробел: ').split())
except:
    print('Ошибка входных данных!')
else:
    print('Ответ:\n    Сложение:','%.2f'%(a+b),'\n    Вычитание:','%.2f'%(a-b),'\n    Умножение:','%.2f'%(a*b),
        '\n    Деление:','%.2f'%(a/b),'\n    Возведение в степень:','%.2f'%(a**b),'\n    Деление по модулю:','%.2f'%(a%b),
        '\n    Целочисленое деление:',int(a//b))
#Задание 2
name=input('Задание 2:\nВведите свое имя: ')
time=int(datetime.now().strftime('%H'))
if time<6:
    print('    Доброй ночи, '+name+'!')
elif time<12:
    print('    Доброе утро, '+name+'!')
elif time<18:
    print('    Добрый день, '+name+'!')
else:
    print('    Добрый вечер, '+name+'!')
#Задание 3*
strg=input('Задание 3*:\nВведите строку: ')
print('    Ответ: '+strg[-2:][::-1])
#Задание 4*
try:
    R=float(input('Задание 4*:\nВведите радиус круга: '))
except:
    print('Ошибка входных данных!')
else:
    print("    Площадь круга = "+'%.2f'%(math.pi*R**2))