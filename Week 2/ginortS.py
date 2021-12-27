l = []
e = []
u = []
o = []
for x in input():
    if x.isdigit():
        e.append(x) if int(x)%2 == 0 else o.append(x)
    else:
        u.append(x) if x.isupper() else l.append(x)
l.sort()
e.sort()
u.sort()
o.sort()
print("".join(l+u+o+e))