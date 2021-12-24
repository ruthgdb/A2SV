from collections import deque

n = int(input())
d = deque()
for x in range(n):
    inst = input().split()
    if inst[0] == 'append':
        d.append(inst[1])
    elif inst[0] == 'appendleft':
        d.appendleft(inst[1])
    elif inst[0] == 'pop':
        d.pop()
    elif inst[0] == 'popleft':
        d.popleft()
for x in range(len(d)):
    print(d[x], end = ' ')
