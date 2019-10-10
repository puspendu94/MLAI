# -*- coding: utf-8 -*-

name = input('Enter file:    ')
handle = open(name, "r")

counts = dict()
lineCount = 0
for line in handle:
    words = line.split()
    print(line.strip())
    lineCount += 1;
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(lineCount, " Lines")
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    print(word, " : ", count)
print("MAX => ", bigword, " : ", bigcount)