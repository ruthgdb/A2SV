def gen_patt(num):
    x = num - 1
    for i in range(1, num+1):
        print(" "*x,end="")
        for j in range(1, i+1):
            print(j,end="")
            y = j
        for m in range(y,1,-1):
            y -= 1
            print(y,end="")
        print()
        x -= 1
h = int(input())
gen_patt(h)