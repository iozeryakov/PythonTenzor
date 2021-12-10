#Задача 1:
def byte(strr):
    """
    Функция преобразовывает список строк в список байт
    """
    byt=[]
    for i in strr:
        try:
            byt.append(bytes(i,encoding='utf-8'))
        except:
            print('    Невозможно преобразовать в байты:',i)
    return byt
def debyte(byt):
    """
    Функция преобразовывает список байт в список строк
    """
    strr=[]
    for i in byt:
        try:
            strr.append(i.decode())
        except:
            print('    Невозможно декодировать:',i)
    return strr
strr=['Добрый день!','Зима очень снежная!',1]
print('Задание 1:\n  Первоначальный список: ',strr)
byt=byte(strr)
print('  Преобразованный список: ',byt)
strrr=debyte(byt)
print('  Декодированный список:',strrr)
#Задача 2:
try:
    f=open('Input.txt','r',encoding='utf-8')
    try:
        c,h,o=map(int,f.read().split())
        f.close()
        c=c//2
        h=h//6
        try:
            f=open('Output.txt','w',encoding='utf-8')
            f.write(str(min(c,h,o)))
            f.close()
            print('Здание 2:\n  Ответ был записан в файл - Output.txt')
        except:
            print('Здание 2:\n  Невозможно записать ответ в файл!')
    except:
        print('Здание 2:\n  Ошибка входных данных!')
except:
    print('Здание 2:\n  Невозможно открыть файл!')
#Задача 3:
def xorCipher(strr,key):
    """
    Функция производит
    шифрование/расшифрование XOR
    """
    cipherStr=''
    for i in strr:
        cipherStr+=chr(ord(i)^key)
    return cipherStr
try:
    f=open('Input3.txt','r',encoding='utf-8')
    strg=f.read()
    f.close()
    try:
        key=int(input('Здание 3:\n  Введите ключ: '))
        try:
            f=open('Output3.txt','w',encoding='utf-8')
            f.write(xorCipher(strg,key))
            f.close()
            print('  Ответ был записан в файл - Output3.txt')
        except:
            print('  Невозможно записать ответ в файл!')
    except:
        print('  Ключ неверного формата!')
except:
    print('Здание 3:\n  Невозможно открыть файл!')

