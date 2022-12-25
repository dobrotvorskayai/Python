# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input("Введите вещественное число: "))
sum_digit = 0

while num % 1 > 0:
    num = num * 10
else: num = int(num)

while num:
    sum_digit += num % 10
    num = num // 10
else: print(sum_digit)