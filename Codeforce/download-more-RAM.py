t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    RAM = [[a[i], b[i]] for i in range(n)]
    
    RAM.sort()
    
    for i in range(len(RAM)):
        if RAM[i][0] <= k:
            k += RAM[i][1]
            
    print(k)
