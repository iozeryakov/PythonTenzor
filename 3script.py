import math
import cmath
#Задача 1
d=input('Задача 1:\nВведите куда шагнуть персонажу (Пример: Вправо 15): ').split()
try:
    d[0]=d[0].lower()
    d[1]=int(d[1])
    if d[0]=='вправо':
        print('Ответ: координаты персонажа = (',d[1],', 0 ).')
    elif d[0]=='влево':
        print('Ответ: координаты персонажа = (',(-d[1]),', 0 ).')
    elif d[0]=='вверх':
        print('Ответ: координаты персонажа = ( 0 ,',d[1],').')
    elif d[0]=='вниз':
        print('Ответ: координаты персонажа = ( 0 ,',(-d[1]),').')
    else:
        print('Команда не найдена')
except:
    print('Команда не найдена.')
#Задача 2
print('\nЗадача 2:')
x=0
y=0
while True:
    d=input('Введите куда шагнуть персонажу (Пример: Вправо 15; Для остановки напиши: стоп): ').split()
    try:
        d[0]=d[0].lower()
        d[1]=int(d[1])
        if d[0]=='вправо':
            x+=d[1]
            print('Ответ: координаты персонажа = (',x,',', y,').')
        elif d[0]=='влево':
            x-=d[1]
            print('Ответ: координаты персонажа = (',x,',', y,').')
        elif d[0]=='вверх':
            y+=d[1]
            print('Ответ: координаты персонажа = (',x,',', y,').')
        elif d[0]=='вниз':
            y-=d[1]
            print('Ответ: координаты персонажа = (',x,',', y,').')
        else:
            print('Команда не найдена')
    except:
        if d[0].lower()=='стоп':
            print('Ответ: координаты персонажа = (',x,',', y,').')
            break
        else:
            print('Команда не найдена.')
#Задача 3
print('\nЗадача 3:\nВведите коэф-ты для уравнения \nax^2 + bx + c = 0:')
try:
    a=float(input('a= '))
    b=float(input('b= '))
    c=float(input('c= '))
    if a == 0 and b == 0 and c == 0:
        print("X-принимает любое число")
    else:
        if a == 0 and b == 0:
            print("решений нет")
        else:
            if a == 0 and c == 0:
                print("x=", 0)
            else:
                if a == 0:
                    x = (-c / b)
                    print("x= %.2f" % x)
                else:
                    d = b * b - 4 * a * c
                    if d > 0:
                        x1 = (-b + math.sqrt(d)) / (2 * a)
                        x2 = (-b - math.sqrt(d)) / (2 * a)
                        if x1 == x2:
                            print('x1= %.2f' % x1)
                        else:
                            print('x1= %.2f \nx2= %.2f' % (x1,x2))
                    elif d==0:
                        x = -b / (2 * a)
                        print('x= %.2f' % x)
                    else:
                        print("решений нет")

except:
    print('Данные введены не верно!')
#4
print('\nЗадача 4:\nНужно ввести комплексные коэффициенты?')
Ot=input('Ваш ответ(Y/N) = ')
print('Введите коэф-ты для уравнения \nax^2 + bx + c = 0:')
try:
    if Ot.lower() == 'y':
        a = complex(input('a= '))
        b = complex(input('b= '))
        c = complex(input('c= '))
        if a==0 and b==0 and c==0:
            print('X-принимает любое число')
        else:
            if a == 0 and b == 0:
                print('решений нет')
            else:
                if a == 0 and c == 0:
                    print("x=", 0)
                else:
                    if a == 0:
                        x = (-c / b)
                        print('x= ', x)
                    else:
                        if b == 0:
                            print('x= ', math.sqrt(-c / a))
                        else:
                            d = b * b - 4 * a * c
                            x1 = (-b + cmath.sqrt(d)) / (2 * a)
                            x2 = (-b - cmath.sqrt(d)) / (2 * a)
                            print('x1=', x1,'\nx2=', x2)
    else:
        a = float(input('a= '))
        b = float(input('b= '))
        c = float(input('c= '))
        if a == 0 and b == 0 and c == 0:
            print('X-принимает любое число')
        else:
            if a == 0 and b == 0:
                print('решений нет')
            else:
                if a == 0 and c == 0:
                    print('x=', 0)
                else:
                    if a == 0:
                        x = (-c / b)
                        print('x= %.2f' % x)
                    else:
                        d = b * b - 4 * a * c
                        if d > 0:
                            x1 = (-b + math.sqrt(d)) / (2 * a)
                            x2 = (-b - math.sqrt(d)) / (2 * a)
                            if x1 == x2:
                                print('x1= %.2f' % x1)
                            else:
                                print('x1= %.2f \nx2= %.2f' % ( x1, x2))
                        else:
                            x1 = (-b + cmath.sqrt(d)) / (2 * a)
                            x2 = (-b - cmath.sqrt(d)) / (2 * a)
                            print('x1=', x1,'\nx2=', x2)
except:
    print('Ошибка введеных данных!')