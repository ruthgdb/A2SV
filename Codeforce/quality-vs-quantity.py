t = int(input())
 
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left, right = 1, len(arr) - 1
    blueSum = arr[0] + arr[1]
    redSum = arr[-1]
    
    result = "NO"
    
    while left < right:
        if blueSum < redSum:
            result = "YES"
            break
        left += 1
        right -= 1
        blueSum += arr[left]
        redSum += arr[right]
            
    print(result)
