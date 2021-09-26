list = []

while(True):
    try:
        x = input("enter a number or Enter to finish:")
        if x == '':
            break
        elif x.isdigit():
            list.append(int(x))
        else:
            raise TypeError(x)

    except TypeError as err:
        print(err, "is not a number or Enter")
        break


try:
    if len(list) == 0:
        raise Exception()

    sum = 0
    lowest = 9
    highest = 0

    for item in list:
        sum += item
        if item < lowest:
            lowest = item
        if item > highest:
            highest = item

    if len(list) % 2 == 0:
        median = (list[int(len(list) / 2) - 1] + list[int(len(list) / 2)]) / 2
    else:
        median = list[int((len(list) - 1)/2)]

    print('numbers:', list)
    print('count:', len(list), end=" ")
    print('sum:', sum, end=" ")
    print('lowest:', lowest, end=" ")
    print('highest:', highest, end=" ")
    print('mean:', sum/len(list))

    print('median:', median)

except Exception:
    print("no number in list")
