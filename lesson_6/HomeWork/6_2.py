# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.
# Use comprehension.
# in 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

from random import sample

def new_list (end_list: int) -> list:
     
    if end_list < 20:
        print("Введите число больше 20")
        return []
   
    else:      
        our_list = [i for i in range (20, end_list+1)]
    
    return our_list

def result_list(lst):
    res_list = []
    [res_list.append(lst[i]) for i in range(0,len(lst)) if lst[i] % 20 == 0 or lst[i] % 21 == 0]
    
    return res_list

print(result_list(new_list(int(input("Введите число: ")))))
