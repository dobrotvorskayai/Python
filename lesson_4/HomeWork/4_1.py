# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000

from decimal import Decimal
 
def dess(num, accuracy):
    return num.quantize(Decimal(accuracy))

print(dess(Decimal(input("Enter a real number: ")), Decimal(input("Enter the required accuracy '0.0001': "))))