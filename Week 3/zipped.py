n, x = input().split()
res = list()
for i in range(int(x)):
    res.append(map(float, input().split()))
res = list(zip(*res))
for i in res:
    print(sum(i)/len(i))
