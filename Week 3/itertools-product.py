from itertools import product

x = list(product(list(map(int, input().split())), list(map(int, input().split()))))
for i in x:
    print(i, end=" ")