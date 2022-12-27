# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def new_list (len_list: int):

    if len_list < 0:
        print("Введите положительное число")
        return []
   
    else:      
        our_list = sample (range (1, len_list * 2), k=len_list)
    
    return our_list

def sum_pos (our_list: list):
    sum = 0
    for i in range (0, len(our_list), 2):
        sum = sum + our_list[i]
    return sum

list_1 = new_list(int (input('Введите длину списка: ')))
print(list_1)
print(sum_pos(list_1))