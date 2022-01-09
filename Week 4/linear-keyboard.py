t = int(input())
for x in range(t):
    s = input()
    letter = input()
    if(len(letter)==1):
        print(0)
        continue
    alpha = dict()
    n = 1
    for i in range(len(s)):
        alpha[s[i]] = n
        n += 1
    count = 0
    for i in range(len(letter)-1):
        count += abs(alpha[letter[i]] - alpha[letter[i+1]])
    print(count)
