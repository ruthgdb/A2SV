s = input()
pow = 0
sum = 0
for i in range(len(s)-1,-1,-1):
    sum += (26 ** pow) * (ord(s[i])-64)
    pow += 1
    print(sum)
print(sum)
