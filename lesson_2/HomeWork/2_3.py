# 3. Задайте список из n чисел,
# заполненный по формуле (1 + 1/n) ** n
# и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

n = int(input("Введите целое число: "))
num_list = []
sum = 0
for i in range (1, n + 1):
    num = round(((1 + 1/i) ** i), 3)
    sum += num
    num_list.append(num)
print(num_list)
print(sum)