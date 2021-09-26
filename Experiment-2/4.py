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


for i in range(1, 6):
    fun()
