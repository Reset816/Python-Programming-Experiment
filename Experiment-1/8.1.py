def cal(x):
    if (x <= 0):
        return 3 * x + 5
    elif (0 < x <= 1):
        return x + 5
    elif (x > 1):
        return -2 * x + 8


try:
    x = input("Please input x:")
    print("f(x)=", cal(float(x)))
except ValueError as err:
    print(err, "is not a number")
