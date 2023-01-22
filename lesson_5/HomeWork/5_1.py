# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def create_list ():
    len_list = int(input("Введите длинну списка (кол-во слов): "))
    if len_list < 1 : print ("Введенны некорректные данные")
    else:
        letters = 'абв'
        new_list = []
        for i in range(len_list): new_list.append(''.join(sample ((letters), k=3)))
    return new_list

def deletion(lst):
    result_list = []
    for i in range (len(lst)):
        if lst[i] != 'абв': result_list.append(lst[i])
    return result_list

   
temp_list = create_list()
print(" ".join(map(str,temp_list)))
res_list = deletion(temp_list)
print(" ".join(map(str, res_list)))
