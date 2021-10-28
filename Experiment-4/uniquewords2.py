import collections
import string
import sys


def fun(item):
    return item[1]


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
for word, count in sorted(words.items(), key=fun):
    print("'{0}' occurs {1} times".format(word, count))
