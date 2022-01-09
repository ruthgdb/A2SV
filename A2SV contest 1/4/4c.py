def gen_patt(n):
    num = (n * 9) - 1
    for i in range(1, num):
        if i % 2 == 0:
            print(" " *2, end="")
        else:
            print("#" * 2, end="")
    
        if(i % 5 == 0):
            print()
gen_patt(3)
