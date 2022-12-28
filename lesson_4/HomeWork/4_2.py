# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]

def simple_num(num):
    simple_list = []
    i = 2
    while i * i <= num:
       while num % i == 0:
           simple_list.append(i)
           num = num / i
       i = i + 1
    if num > 1:
        simple_list.append(round(num))
    return simple_list

print(simple_num(int(input("Enter number: "))))