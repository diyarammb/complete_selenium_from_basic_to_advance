def bubblesort(arr) :
    n=len(arr)
    s=False
    for i in range (n-1):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                s=True

