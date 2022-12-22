# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

n = int(input("Input your number: "))
if 5 < n < 8:
    print("It is a Weakend")
elif 0 < n < 6:
    print("It is a workday")
else:
    print("Input number from 1 to 7")