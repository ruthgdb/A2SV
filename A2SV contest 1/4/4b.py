def gen_patt(num):
    x = num - 1
    for i in range(1, num+1):
        print(" "*x,end="")
        for j in range(1, i+1):
            print(j,end="")
            y = j
        rev = y
        for m in range(y,1,-1):
            y -= 1
            print(y,end="")
        print()
        x -= 1
    r = 1
    for z in range(rev, 0, -1):
        print(" "*(r),end="")
        r += 1
        for g in range(1,z):
            print(g,end="")
        for b in range(z-2,0,-1):
            print(b,end="")
        print()
h = int(input())
gen_patt(h)
