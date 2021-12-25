import re

n = int(input())
for x in range(n):
    s = input()
    res = True
    try:
        reg = re.compile(s)
    except re.error:
        res = False
    print(res)