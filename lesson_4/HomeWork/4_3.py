# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

import random

def new_list(num):
    new_list1 = []
    for i in range(0, num):
        temp = random.choice(range(1, num * 2))
        new_list1.append(temp)
    print(new_list1)    
    return new_list1

def nonrepeating(new_list1):
    res_list = []
    for i in range(len(new_list1)):
        if new_list1.count(new_list1[i]) == 1:
            res_list.append(new_list1[i])
    return res_list

print(nonrepeating(new_list(int(input("Enter list's length: ")))))