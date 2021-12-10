#Задача 2(3,4,5,6)
def password(strr):
    '''
    Функция возвращает истину если пароль
    подходит под условия задачи
    '''
    try:
        assert len(strr)>5 and not(strr.isdigit()) \
               and any(map(str.isdigit,strr)) and not('password' in strr.lower())
        return True
    except:
        return False
#Задача 7
def summ(*number):
    '''
    Функция возвращает сумму чисел
    '''
    sum=0
    try:
        for i in number:
            sum+=i
        return sum
    except TypeError:
        return 0
#Задача 8
rem_er={0:0,1:1}
def fibonacci(x):
    '''
    Функция возвращает  значение числа фибоначи по порядковому номеру
    '''
    if x in rem_er:
        return rem_er[x]
    rem_er[x]=fibonacci(x-1)+fibonacci(x-2)
    return rem_er[x]