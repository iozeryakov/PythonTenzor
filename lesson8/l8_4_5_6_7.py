import time
def decorator1(func):
    '''Декоратор: логирование выполнения функции'''
    def wapper(a,b):
        print('Сумма',a,'и',b,'равна:',end=' ')
        func(a,b)
    return wapper
def decorator2(func):
    '''Декоратор: время выполнения функции'''
    def wapper(a,b):
        start_time=time.clock()
        func(a,b)
        print('Время выполнение функции:','%.5f' % (time.clock()-start_time),'секунд.')
    return wapper
def decorator3(times):
    '''Декоратор: замедление выполнения кода'''
    def decorator(func):
        def wapper(a,b):
            time.sleep(times)
            func(a,b)
            print('Выполнение функции было замедлено на', times,'секунды.')
        return wapper
    return decorator
@decorator2
@decorator3(2)
@decorator2
@decorator1
def sum(a,b):
    '''Функция возвращает сумму 2-х чисел'''
    print(a+b)
sum(5,6)
