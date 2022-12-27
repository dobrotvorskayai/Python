# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample

def new_list (len_list: int):

    if len_list < 0:
        print("Введите положительное число")
        return []
   
    else:      
        our_list = sample (range (1, len_list * 2), k=len_list)
    
    return our_list

def product (our_list: list):
    prod_list = []
    len_list = len(our_list) // 2

    for i in range (0, len_list, 1):
        prod_list.append (our_list[i] * (our_list[len(our_list) - i - 1]))
    
    if len(our_list) % 2:
        prod_list.append (our_list[len_list])

    return prod_list

list_1 = new_list(int (input('Введите длину списка: ')))
print(list_1)
print(product(list_1))