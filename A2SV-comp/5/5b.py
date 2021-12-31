def num_to_alph(colnum):
    s = []
    while colnum:
        colnum -= 1
        s.append(chr((colnum % 26) + 65))
        colnum //= 26
    print("".join(s[::-1]))

n = int(input())
num_to_alph(n)
