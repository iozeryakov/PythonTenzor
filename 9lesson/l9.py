def xorCipher(strr,key):
    """
       Функция производит
       шифрование/расшифрование XOR
       """
    cipherStr=''
    for i in strr:
        cipherStr+=chr(ord(i)^key)
    return cipherStr
rem_er={0:0,1:1}
def fibonacci(x):
    '''
       Функция возвращает  значение числа фибоначи по порядковому номеру
       '''
    if x in rem_er:
        return rem_er[x]
    rem_er[x]=fibonacci(x-1)+fibonacci(x-2)
    return rem_er[x]