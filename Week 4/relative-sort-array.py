c = Counter(arr1)
        newarr = []
        for i in arr2:
            if i in c:
                newarr.extend([i]*c[i])
                c.pop(i) 

        notarr = []
        for i in c:
            notarr.extend([i]*c[i])   
        notarr.sort()
        newarr.extend(notarr)

        return newarr