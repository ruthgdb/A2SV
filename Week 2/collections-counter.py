from collections import Counter
n = int(input())
size = list(map(int, input().split()))
cust = int(input())
arr = []
price = 0
for x in range(cust):
    arr.append(list(map(int, input().split(' '))))
    if arr[x][0] in size:
        price += arr[x][1]
        size.remove(arr[x][0])        
print(price)
