n = int(input())
# arr = [str(input()) for x in range(n)]
arr = [] 
for i in range(n): 
    arr.append(input())
arr = set(arr)
print(len(arr))
