from random import randint
#Задача 2(3,4,5,6)
def password(strr):
    try:
        assert len(strr)>5 and not(strr.isdigit()) \
               and any(map(str.isdigit,strr)) and not('password' in strr.lower())
        return True
    except:
        return False
strr=input('Задание 1:\n Введите пароль: ')
if password(strr):
    print('  Пароль подходит!')
else:
    print('  Пароль не подходит!')
#Задача 7
def summ(*number):
    sum=0
    try:
        for i in number:
            sum+=i
        return sum
    except TypeError:
        return 0
print('Задание 2:\n  Исходные данные: 3,5,7; Сумма =',summ(3,5,7),
    '\n  Исходные данные(нет переменных): ; Сумма =',summ(),
        '\n  Исходные данные(с ошибкой):5,6,j; Сумма =',summ(5,6,'j'))
#Задача 8
rem_er={0:0,1:1}
def fibonacci(x):
    if x in rem_er:
        return rem_er[x]
    rem_er[x]=fibonacci(x-1)+fibonacci(x-2)
    return rem_er[x]
i=randint(0,30)
print('Задание 3:\n',i,'число Фибоначчи =',fibonacci(i))