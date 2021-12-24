from collections import namedtuple
n = int(input())
names = list(input().split())
sums = 0
Marks = namedtuple('Marks', [names[0], names[1], names[2], names[3]])
for i in range(n):  
    temp = list(input().split())
    avg = Marks(temp[0], temp[1], temp[2], temp[3])
    sums += int(avg.MARKS)
sums = sums / n
print("{:.2f}".format(sums))