# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20


n = int(input("Введите целое число: "))
pos_one = int(input("Введите позицию 1: "))
pos_two = int(input("Введите позицию 2: "))

num_list = list(range(-n, n + 1))
print(num_list)

if len(num_list) >= pos_one > 0 and len(num_list) >= pos_two > 0:
    result = num_list[pos_one - 1] * num_list[pos_two - 1]
    print(result)
else:
    print ("Введенной позиции не существует")