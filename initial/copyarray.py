def replaceElements(arr):
    n = len(arr)
    print(n)
    i =0
    while i<=n:
        if i==n:
            arr[-1]=-1
            break
        max =0
        j=i+1
        while j<n:
            if arr[j]>max:
                max =arr[j]
                print(i,j)
            j+=1
        arr[i]=max
        i+=1
    return arr

print(replaceElements([2,4,5,3,1,2]))
