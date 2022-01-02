from itertools import groupby

s = input()
lis = [x for x in s]
grouped = groupby(lis)
 
for i, j in grouped:
    temp = [len(list(j)),int(i)]
    print(tuple(temp), end=" ")
