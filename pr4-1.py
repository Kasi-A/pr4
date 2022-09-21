import math

# 1. Написати програму для обчислення значення функції 𝑓(𝑥)

4
def pr1(x):
    return((x + math.sin(x)/math.log(10, abs(x-math.pow(x,4)))) + math.log(4,x))

x = float(input("x = "))

print(f"F(x) = {pr1(x)}")



