# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
#
# in
# 88
# out
# 1011000

def bin(num: int):
    temp_list = []
    while num:
        temp_list.append(num % 2)
        num = num // 2
    num_bin = 0
    for i in range(0, len(temp_list)):
        num_bin += temp_list[len(temp_list) - 1 - i] * (10 ** (len(temp_list) - i))
    
    return num_bin // 10
 
res = bin(int (input('Введите десятичное число: ')))
print(res)