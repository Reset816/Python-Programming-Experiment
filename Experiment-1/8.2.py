def cal_factorial(x):
    factorial = 1
    tmp = 1
    while tmp <= int(x):
        factorial = factorial * tmp
        tmp = tmp + 1
    return factorial


i = 1
while i <= 10:
    print("Factorial of ", str(i), " is ", cal_factorial(i))
    i = i + 1
