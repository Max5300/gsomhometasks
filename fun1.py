def fun1(a):
    if -2.4 <= a <= 5.7:
        return pow(a, 2)
    else:
        return 4

x = float(input())
print(fun1(x))
