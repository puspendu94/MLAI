# -*- coding: utf-8 -*-
# Taking input file from user and read it
name = input('Enter file:    ')
handle = open(name, "r")
#creating a dictinary of words and respective frequency
counts = dict()
lineCount = 0
for line in handle:
    words = line.split()
    print(line.strip())
    lineCount += 1;
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(lineCount, " Lines")
#finding most common word appears in the input file
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    print(word, " : ", count)
#Final output
print("MAX => ", bigword, " : ", bigcount)
#Exit with thank you
input("Enter any to EXIT...................Thank you")
