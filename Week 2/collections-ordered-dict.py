from collections import OrderedDict

n = int(input())
od = OrderedDict()
for i in range(n):
    name, other, price = input().rpartition(' ')
    od[name] = od.get(name, 0) + int(price)
for n, p in od.items():
    print(n, p)  
