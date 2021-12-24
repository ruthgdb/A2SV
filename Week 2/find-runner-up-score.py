if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    fir = arr[0]
    sec = -101
    for i in range(1,n):
        if(fir > arr[i]):
            if(sec < arr[i]):
                sec = arr[i]     
        elif fir < arr[i]:
            fir, sec = arr[i], fir
    print(sec)
