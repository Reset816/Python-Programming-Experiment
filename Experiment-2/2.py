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


sum = 0
lowest = 9
highest = 0

for item in list:
    sum += item
    if item < lowest:
        lowest = item
    if item > highest:
        highest = item

print('numbers:', list)
print('count:', len(list), end=" ")
print('sum:', sum, end=" ")
print('lowest:', lowest, end=" ")
print('highest:', highest, end=" ")
print('mean:', sum/len(list))
