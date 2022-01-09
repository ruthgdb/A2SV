n = 5
x = 4
for i in range(n):
    print("*"*i,end='')
    print(" "*x,end='')
    print(" "*x,end='')
    print("*"*i,end='')
    x -= 1
    print()
    