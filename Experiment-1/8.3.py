def cal_factorial(x):
    factorial = 1
    for i in range(1, x + 1):
        factorial = factorial * i
    return factorial


for i in range(1, 11):
    print("Factorial of ", str(i), " is ", cal_factorial(i))
