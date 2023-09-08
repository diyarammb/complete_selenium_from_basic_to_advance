def bubblesort(arr):
    n=len(arr)

    swappped = False
    for i in range(n-1):
        for j in  range(0, n-i -1):

            if arr[j] > arr[j+1]:

               swappped = True

               arr[j] , arr[j+1] = arr[j+1] ,arr[j]

        if not swappped:
            return
arr= [ 3478 ,734687 ,72346 ,743346 ,32871]
bubblesort(arr)
print("sorted array is")
for i in range(len(arr)):
     print("%d" %arr[i],end=" ")



