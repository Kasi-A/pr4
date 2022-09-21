import math

#2 Написати  програму,  яка  обчислює  значення  виразу F= 


def pr2(a,b,x):
    return(x*math.tan(x) * math.pow(math.e,a-b) + math.log(4,(math.pow(x,2)+0.7)))

a = int(input("a = "))
b = int(input("b = "))
x = int(input("x = "))

print(f"F = {pr2(a,b,x)}")


