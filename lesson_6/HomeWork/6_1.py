# 1. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
# in 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample

def new_list (len_list: int) -> list:
     
    if len_list < 0:
        print("Введите положительное число")
        return []
   
    else:      
        our_list = sample (range (1, len_list * 2), k=len_list)
    
        print(our_list)
        return our_list

# def result_list(lst):
    # res_list = []
    # for i in range(1,len(lst)):
    #     if lst[i] > lst[i-1]: res_list.append(lst[i])
    # return res_list

def result_list(lst):
    res_list = []
    [res_list.append(lst[i]) for i in range(1,len(lst)) if lst[i] > lst[i-1]]
    
    return res_list

print(result_list(new_list(int(input("Введите число: ")))))