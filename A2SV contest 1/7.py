s = input()
r = {"I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000
    }
sum = 0
for i in range(len(s)):
    if i < (len(s) - 1) and r[s[i]] < r[s[i + 1]]:
        sum -= r[s[i]]
    else:
        sum += r[s[i]]
print(sum)
