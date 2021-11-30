import colorsys
from random import randint
#Задание 1
list = [randint(-100,100) for i in range(20)]
print('Задание 1:\nСписок:',list)
flag=True
iter=0
while(flag):
    flag=False
    for i in range(len(list)-iter-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
            flag=True
    iter+=1
print('Отсортированный список:',list)
#Задание 2
print('Задание 2:(чуть-чуть придется подождать)')
d={}
for r in range(256):
    for g in range(256):
        for b in range(256):
            if r<16:
                r1='0'+hex(r)[2:]
            else:
                r1=hex(r)[2:]
            if g<16:
                g1='0'+hex(g)[2:]
            else:
                g1=hex(g)[2:]
            if b<16:
                b1='0'+hex(b)[2:]
            else:
                b1=hex(b)[2:]
            d['#'+r1+g1+b1]=(r,g,b)
print(d)
#Задание 3
set1 = {randint(-100,100) for i in range(20)}
set2 = {randint(-100,100) for i in range(20)}
print('Задание 3:\n',set1,'\n',set2)
print('1:',set1 & set2)
print('2:',set1.difference(set2))
print('3:',set2.difference(set1))
print('4:',set1.difference(set2).union(set2.difference(set1)))
#Задание 4
print('Задание 4:')
inventory=[]
max=float(15)
wt=0
while True:
    if wt==0:
        print('Ваш инвентарь: свободно -',max,'\n    Предметов нет!')
    else:
        print('Ваш инвентарь: свободно -', max-wt)
        for i in range(len(inventory)):
            print(' ',i+1,'-',inventory[i][0]+'; вес -',inventory[i][1])
    action=input('Выберите действие:\n  1-Добавить пердмет;\n  2-Удалить предмет;\n  3-Увеличить объем инвенторя;\n  4-Выход;\nВведите номер выбранного действия: ')
    while True:
        try:
            action=int(action)
            if action>4 or action<1:
                raise ValueError
            break
        except:
            action=input('Действие не найдено, введите номер действия из списка выше: ')
    if action==1:
        name = input('Введите название предмета: ')
        w_t = input('Введите вес предмета: ')
        while True:
            try:
                w_t = float(w_t)
                if w_t<=0:
                    raise ValueError
                break
            except:
                w_t = input('Вес указан не верно, введите число: ')
        if wt + w_t <= max:
            inventory.append([name,w_t])
            wt+=w_t
            print('Предмет успешно добавлен!\n')
        else:
            print('Вес предмета превышает свободное место, предмет не добавлен!\n')
    elif action==2:
        if wt>0:
            obj=input('Введите номер предмета: ')
            while True:
                try:
                    obj=int(obj)
                    if obj<1 or obj>len(inventory):
                        raise ValueError
                    break
                except:
                    obj = input('Предмет не найден, введите номер предмета из списка выше: ')
            wt-=inventory[obj-1][1]
            inventory.pop(obj-1)
            print('Предмет успешно удален!\n')
        else:
            print('Предметов нет!\n')
    elif action==3:
        y=input('Для увеличения объема инвенторя необходимо пригласить создателя на стажировку;)\nПриглашен?(Y/N): ')
        if y.lower()=='y':
            max+=1000
            print('Объем успешно увеличен!')
        else:
            print('Объем невозможно увеличить!')
    elif action==4:
        break


