from itertools import groupby
 
for i, j in groupby(input()):
    temp = [len(list(j)),int(i)]
    print(tuple(temp), end=" ")
