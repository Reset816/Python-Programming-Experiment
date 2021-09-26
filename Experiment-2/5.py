import random
article = ("the", "a")
subject = ("cat", "dog", "man", "woman")
verb = ("sang", "ran", "jump")
adverb = ("loud", "quiet", "well", "bad")


def fun():
    print(random.choice(article), random.choice(
        subject), random.choice(verb), end=' ')
    if random.randint(0, 1) == True:
        print(random.choice(adverb), end='')
    print()


try:
    x = int(input("enter a number:"))
    if x == '':
        tmp = 5
    elif 1 <= x <= 10:
        tmp = x
    else:
        raise ValueError(x)
    for i in range(1, tmp + 1):
        fun()

except ValueError as err:
    print(err, "is not a vaild parameter")
