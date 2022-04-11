t = int(input())
 
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left = 1
    right = len(arr) - 1
    blueSum = sum(arr[:left + 1])
    redSum = sum(arr[right:])
    
    result = "NO"
    
    while left < right:
        if blueSum < redSum:
            result = "YES"
            break
        else:
            left += 1
            right -= 1
            blueSum += arr[left]
            redSum += arr[right]
            
    print(result)