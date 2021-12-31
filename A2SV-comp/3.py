def gen_patt(num):
    x = num - 1
    for i in range(2):
        for j in range(1,num+1):
            print("#"*x,end="")
            print(" ",end="")
        print()
n = int(input())
gen_patt(n)